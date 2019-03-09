from newspaper import Article
import langdetect

def get_text(url):
    '''Function returns article text by given url

    Arguments:
        url {str} -- URL to parse

    Returns:
        str -- Article text from given url.
    '''

    article = Article(url)
    article.download()
    article.parse()
    chunks = list(filter(lambda x: x != '', article.text.split('\n')))
    chunks = list(filter(lambda x: langdetect.detect(x)
                         == article.meta_lang, chunks))
    return '\n'.join(chunks)
