from TextRank.textrank import TextRankSummarizer
import sys
import os


def main():
    if len(sys.argv) < 2:
        path, language, sentences = get_user_data(error=0)
        sys.argv[1], sys.argv[2], sys.argv[3] = path, language, sentences
    if not os.path.isfile(os.path.abspath(sys.argv[1])):
        path, language, sentences = get_user_data(error=1)
        sys.argv[1], sys.argv[2], sys.argv[3] = path, language, sentences
    if sys.argv[2] not in ["english"]:
        path, language, sentences = get_user_data(error=2)
        sys.argv[1], sys.argv[2], sys.argv[3] = path, language, sentences
    if not str.isdigit(sys.argv[3]):
        path, language, sentences = get_user_data(error=3)
        sys.argv[1], sys.argv[2], sys.argv[3] = path, language, sentences
    else:
        path, language, sentences = sys.argv[1], sys.argv[2], sys.argv[3]
    summarizer = TextRankSummarizer(language)
    text = read_file(path)
    summarizer.set_text("".join(text))
    sentences = int(sentences)
    summary = summarizer.get_summary(sentences)
    if len(sys.argv) == 5:
        result_file = sys.argv[4]
        write_file(result_file, summary)
    else:
        result_file = input("Specify output file: ")
        write_file(result_file, summary)


def get_user_data(error):
    """Function gets data from user
    
    Arguments:
        error {int} -- Type of data, that is incorrect or misiing (0 for amount of command args, 1 for path for file with text
        2 for language and 3 for amount of sentences in summary)
    
    Returns:
        tuple -- Fixed data from user
    """
    if error == 0:
        print(
            "Specify command args: file to read text, language of this text and number of sentences in summary"
        )
        sys.exit(0)
    elif error == 1:
        print("File, that you specified does not exist")
        path = input("Type path to file: ")
        if os.path.isfile(os.path.abspath(path)):
            return path, sys.argv[2], sys.argv[3]
        else:
            print("File, that you specified does not exist")
            sys.exit(0)
    elif error == 2:
        print("You specified wrong language")
        language = input("Specify language: ")
        if language in ["english"]:
            return sys.argv[1], language, sys.argv[3]
    elif error == 3:
        print("Number of sentences in summary should be integer")
        sentences = input("Specify number of sentences in summary: ")
        if sentences.isdigit():
            return sys.argv[1], sys.argv[2], sentences
        else:
            print("Number of sentences in summary should be integer")
            sys.exit(0)


def read_file(filename):
    """Function reads contents of file
    
    Arguments:
        filename {str} -- Filename to read
    
    Returns:
        list -- List with lines of text in file
    """
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.readlines()


def write_file(filename, text):
    """Function writes given text into file
    
    Arguments:
        filename {str} -- Filename to write text
        text {list} -- List of lines to write
    """
    with open(filename, "w", encoding="utf-8") as fp:
        for line in text:
            fp.write(line + "\n")


if __name__ == "__main__":
    main()