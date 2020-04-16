# import nltk
from nltk.tokenize import word_tokenize
import IBM1_EM
import string
import numpy as np
import Utils


def sentence_tokenizer(sentence_list, max_index):
    final_list = list()
    word_dictionary = {}    #this dictionary will keep both word and its order in its language
    reverse_dictionary = {}
    lang_order = 0
    cnt = 0
    translate_table = dict((ord(char), None) for char in string.punctuation)
    for r in sentence_list[:max_index]:
        if cnt == 0 :
            r = r.replace(u'\ufeff', '')
            cnt += 1

        r = r.translate(translate_table)            #remove punctuation
        tokens = word_tokenize(r.lower())

        produced_sentence = ""
        for token in tokens:
            if token not in word_dictionary:
                word_dictionary[token] = lang_order
                reverse_dictionary[lang_order] = token
                lang_order += 1
            produced_sentence = produced_sentence + token + " "
        produced_sentence = produced_sentence[:(len(produced_sentence) - 1)]  # remove last space

        final_list.append(produced_sentence)

    final_list[0] = final_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return final_list, word_dictionary, reverse_dictionary


def model_trainer():
    with open("English_Updated.txt", encoding="utf8") as f:
        english_data = f.readlines()
        #print("\n*****\n******\n",english_data)
        #print("\n*****\n******\n",len(english_data))

    with open("Dutch_Updated.txt", encoding="utf8") as f:
        dutch_data = f.readlines()
        #print("\n*****\n******\n",dutch_data)
        #print("\n*****\n******\n",len(dutch_data))
        

    #just use sentences with length at most 10 words.
    new_english_data = list()
    new_dutch_data = list()

    for sen_marker in range(len(english_data)):
        if sen_marker > 500000 :
            break 
        cur_en_sen = english_data[sen_marker].split()                #tokenizing current sentence
        cur_tr_sen = dutch_data[sen_marker].split()
        if len(cur_en_sen) < 25 and len(cur_tr_sen) < 25:       #considering only those sentences with less than 51 words
            new_english_data.append(english_data[sen_marker])
            new_dutch_data.append(dutch_data[sen_marker])

    english_data = new_english_data.copy()                          # english_data is now a list of tokenized sentence
    dutch_data = new_dutch_data.copy()                          # i.e. a list of sentences where each sentence is a list of words

    #max_num_of_translations = 1000
    max_num_of_translations = 3000

    # parse dutch sentences, tokenize the words
    dutch_sentences, dutch_word_dict, reverse_dutch_word_dict = sentence_tokenizer(dutch_data, max_num_of_translations)

    # parse english sentences, tokenize the words
    english_sentences, english_word_dict, reverse_english_word_dict = sentence_tokenizer(english_data, max_num_of_translations)

 
    #run the EM algorithm of IBM Model 1
    translate_eng_dutch  = IBM1_EM.expectation_maximization(dutch_word_dict,english_word_dict,dutch_sentences,english_sentences)
    

    # The following code finds out the maximum probability 
    # for translating a Dutch/English word to English/Dutch
    # from the existing e-f matrix.
    # These maximum probabilities are stored in dictionaries 
    # and saved as .npy files for being used for translation
 
    total_dutch_ocurrences = translate_eng_dutch.shape[0]
    total_eng_occurrences = translate_eng_dutch.shape[1]

    #final dictionaries for translation mapping
    english_map = {}
    dutch_map = {}

    for eng_marker in range(total_eng_occurrences): #for all foreign words f do
        maximum = -100
        i = 0
        for dutch_marker in range(total_dutch_ocurrences):
         #for all English words e do
            if translate_eng_dutch[dutch_marker][eng_marker] > maximum : 
                maximum = translate_eng_dutch[dutch_marker][eng_marker]
                i = dutch_marker

        english_map[reverse_english_word_dict[eng_marker]] = reverse_dutch_word_dict[i]
        #end for
    #end for
    for dutch_marker in range(total_dutch_ocurrences): #for all foreign words f do
        maximum = -100
        i = 0
        for eng_marker in range(total_eng_occurrences):
         #for all English words e do
            if translate_eng_dutch[dutch_marker][eng_marker] > maximum : 
                maximum = translate_eng_dutch[dutch_marker][eng_marker]
                i = eng_marker
        #end for
        dutch_map[reverse_dutch_word_dict[dutch_marker]] = reverse_english_word_dict[i]
    #end for    

    np.save("trained_data/dutch_to_english_maximised",dutch_map)
    np.save("trained_data/english_to_dutch_maximised",english_map)