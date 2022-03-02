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
    """ Cuts different paragraphs up in sentences and words
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


def get_freqs(text: list) -> list:
    """ gets the frequencies from a piece of text
    :param
    text (list): raw data
    :return:
    freqs (list): list of lists with tuples. [information paragraph one,information paragraph two]
    """
    freqs=[]
    for i in text:
        tokensed_text = word_tokenize(i)
        FreqDisturb = FreqDist(tokensed_text)
        freqs.append(FreqDisturb.most_common(20))
    return freqs

def main():
    nltk.download('punkt')
    text = reading_in_word("testwriting")
    freqs = get_freqs(text)
    print("word frequencies per paragraph: ")
    print(freqs)
    tokenized_text = preprosess(text)
    print("Tokenized text: ")
    print(tokenized_text)


main()
