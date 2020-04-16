import numpy as np
from nltk.tokenize import word_tokenize
import string
import IBM1_EM
import Utils


def get_tokens_of_sentence(sentence):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    sentence = sentence.translate(translate_table)
    tokens = word_tokenize(sentence.lower())
    return tokens

def sentence_tester1(sentence_to_translate,translate_option):
    dutch_to_english_maximised = np.load("trained_data/dutch_to_english_maximised.npy",allow_pickle = True).item()
    english_to_dutch_maximised = np.load("trained_data/english_to_dutch_maximised.npy",allow_pickle = True).item()

    if translate_option == 1:
        f_sentence = get_tokens_of_sentence(sentence_to_translate)
        e_sentence = ""
        for word in f_sentence :
            if word in dutch_to_english_maximised:
                e_sentence = e_sentence + dutch_to_english_maximised[word] + " "
            else:
                print("word '"+ word +"' does not exist in trained language translation dictionary")
                continue
        return e_sentence
    elif translate_option == 2:
        e_sentence = get_tokens_of_sentence(sentence_to_translate)
        f_sentence = ""
        for word in e_sentence :
            if word in english_to_dutch_maximised:
                f_sentence = f_sentence + english_to_dutch_maximised[word] + " "
            else:
                print("word '"+ word +"' does not exist in trained language translation dictionary")
                continue
        return f_sentence

def test(sentence_to_translate,translate_option):
    return sentence_tester1(sentence_to_translate,translate_option)


