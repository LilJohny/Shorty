from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, RepeatVector
from keras.layers.wrappers import TimeDistributed
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.regularizers import l2
from recursive_loop import RecursiveLoopLayer
from keras.optimizers import Adam, RMSprop


def create_model(weight_decay, vocab_size, embedding_size, maxlen, maxlend,
                 maxlenh, p_emb, p_W, p_U, optimizer, embedding, rnn_layers,
                 rnn_size, p_dense, activation_rnn_size):
    regularizer = l2(weight_decay) if weight_decay else None
    model = Sequential()
    model.add(
        Embedding(vocab_size,
                  embedding_size,
                  input_length=maxlen,
                  W_regularizer=regularizer,
                  dropout=p_emb,
                  weights=[embedding],
                  mask_zero=True,
                  name='embedding_1'))
    for i in range(rnn_layers):
        lstm = LSTM(
            rnn_size,
            return_sequences=True,  # batch_norm=batch_norm,
            W_regularizer=regularizer,
            U_regularizer=regularizer,
            b_regularizer=regularizer,
            dropout_W=p_W,
            dropout_U=p_U,
            name=f'lstm_{i+1}')
        model.add(lstm)
    model.add(Dropout(p_dense, name='dropout_%d' % (i + 1)))
    if activation_rnn_size:
        model.add(
            RecursiveLoopLayer(maxlend,
                               rnn_size,
                               activation_rnn_size,
                               maxlenh,
                               name="simplecontext_1"))
    model.add(
        TimeDistributed(
            Dense(vocab_size,
                  W_regularizer=regularizer,
                  b_regularizer=regularizer,
                  name='timedistributed_1')))
    model.add(Activation('softmax', name='activation_1'))
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    return model
