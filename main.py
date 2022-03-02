from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk import FreqDist


def reading_in_word(file_name: str, paragraph: bool = True) -> list:
    """ reads in file and stores seperate paragraphs in list
    :param
    file_name (string): name of the file with the text
    paragraph (bool): If the text is spliced on paragraphs or not
    :return:
    paragraphs(list): list of paragraphs
    """
    paragraphs = []
    text = ""
    with open(file_name) as open_file:
        for i in open_file:
            if not paragraph:
                text += i.strip()
            else:
                paragraphs.append(i.strip())
        if not paragraph:
            paragraphs.append(text)
    return paragraphs


def preprosess(text: list) -> list:
    """ Cuts diffrent paragraphs up in sentences and words
    :param
    text(list): list of paragraphs
    :return:
    tokenized_text(list): list
    """
    # make sure you get a 3d list (now it is just a 2d list
    tokenised_text = []
    for i in text:
        tokenised_paragraph = []
        sentences = sent_tokenize(i)
        for j in sentences:
            tokenised_paragraph.append(word_tokenize(j))
        tokenised_text.append(tokenised_paragraph)

    return tokenised_text


def get_freqs(text: list):
    """ gets the frequencies from a piece of text
    :param
    text (list): raw data
    :return:

    """
    for i in text:
        tokensed_text = word_tokenize(i)
        FreqDisturb = FreqDist(tokensed_text)
        print(FreqDisturb.most_common(20))


# tokenise the work

# use an lametiser

# give data on the work

# remove basic words said etc.

# check for repetition > how to show this specifically??

def main():
    print("hello world")
    nltk.download('punkt')
    text = reading_in_word("test writing/testwriting")
    get_freqs(text)
    tokensed_text = preprosess(text)
    print(tokensed_text)


main()
