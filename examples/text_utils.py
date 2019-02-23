import bs4 as bs
import urllib.request


def get_text_url(url: str):
    '''Function returns article text from given url.
    
    Arguments:
        url {str} -- URL to download article text.
    
    Returns:
        str -- Return article text from given url.
    '''

    data = urllib.request.urlopen(url).read()
    parsed_article = bs.BeautifulSoup(data, 'lxml')
    paragraphs = parsed_article.find_all('p')
    text = ''
    for p in paragraphs:
        text += p.text
    return text
