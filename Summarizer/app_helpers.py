import newspaper
import nltk.tokenize


def read_file(file_name):
    """Function reads text file contents
    
    Arguments:
        file_name {str} -- File name to read
    
    Returns:
        list -- List of lines in file
    """
    fp = open(file_name, "r", encoding="utf-8")
    return fp.readlines()


def read_url(url):
    """Method returns article text on this url
    
    Arguments:
        url {str} -- Url to search article
    
    Returns:
        str -- Artcile text
    """
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text


def count_sentences(text):
    """Funtion counts sentences in given text
    
    Arguments:
        text {str} -- Text to count sentences
    
    Returns:
        int -- Number of sentences
    """
    return len(nltk.sent_tokenize(text))


def get_file_menu_help():
    """Function returns file menu help
    
    Returns:
        str -- Text of file menu help
    """
    return "Through the File menu you can use two ways to open the text:\n1) First option is opening text from file: " \
           "you just need to select text file and program will read all text from that file.\n\n2) Second option is " \
           "opening text from given link: You need to choose open url and then paste your link and click ok. Program " \
           "will try to find article on that url and will show you result on left text field. You can modify this " \
           "text and then use summarize button."


def get_summarization_help():
    """Function returns summarization help
    
    Returns:
        str -- Text of summarization help
    """
    return "This program allows you to perform summarization on text in English language.\nYou can choose number of " \
           "sentences in summary.\nYou need to use grammatically correct text as input to get correct summary.\nIf " \
           "grammatically incorrect text or text in another language is entered, the result will be an error message " \
           "in the field to display the result. "


def get_general_help():
    """Function returns general help
    
    Returns:
        str -- Text of general help
    """
    return "Hello!\nThis program can summarize English text. Before using this program you need to know few important " \
           "things\n\n1) Scraping of long text using open url option in File menu can take some time\n2) Time, " \
           "that program needs to summarize input text depends on length of text, so it takes a while to summarize " \
           "long texts "
