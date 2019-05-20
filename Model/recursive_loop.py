from keras.layers.core import Lambda
from keras import backend as K


class RecursiveLoopLayer(Lambda):
    """Class representing RecursiveLoop for keras"""
    def __init__(self, maxlend, rnn_size, activation_rnn_size, maxlenh, **kwargs):
        super().__init__(self.recursive_loop, **kwargs)
        self.rnn_size = rnn_size
        self.activation_rnn_size = activation_rnn_size
        self.maxlend = maxlend
        self.maxlenh = maxlenh
        self.supports_masking = True

    def compute_mask(self, inputs, mask=None):
        return mask[:, self.maxlend:]

    def compute_output_shape(self, input_shape):
        nb_samples = input_shape[0]
        n = 2*(self.rnn_size - self.activation_rnn_size)
        return (nb_samples, self.maxlenh, n)

    @staticmethod
    def recursive_loop(X, mask, n, maxlend, maxlenh):
        desc, head = X[:, :maxlend, :], X[:, maxlend:, :]
        head_activations, head_words = head[:, :, :n], head[:, :, n:]
        desc_activations, desc_words = desc[:, :, :n], desc[:, :, n:]
        activation_energies = K.batch_dot(
            head_activations, desc_activations, axes=(2, 2))
        activation_energies = activation_energies + -1e20 * \
            K.expand_dims(1. - K.cast(mask[:, :maxlend], 'float32'), 1)

        activation_energies = K.reshape(activation_energies, (-1, maxlend))
        activation_weights = K.softmax(activation_energies)
        activation_weights = K.reshape(
            activation_weights, (-1, maxlenh, maxlend))
        
        desc_avg_word = K.batch_dot(
            activation_weights, desc_words, axes=(2, 1))
        return K.concatenate((desc_avg_word, head_words))
