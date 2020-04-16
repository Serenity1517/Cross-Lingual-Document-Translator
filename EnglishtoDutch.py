from nltk.tokenize import word_tokenize
import nltk.data
import string
import ModelTrainer
import ModelTester
import Utils

def sentence_tokenizer(sentence_list) :
    final_list = list()
    index = 0
    for sen in sentence_list:
        if index == 0 :
            sen = sen.replace(u'\ufeff', '')
            index += 1

        tokens = word_tokenize(sen.lower())

        output_sentence = ""

        for token in tokens :
            output_sentence += token + " "
        
        output_sentence = output_sentence[:(len(output_sentence)-1)]  #remove last space
        final_list.append(output_sentence)    

    final_list[0] = final_list[0].replace(u'\ufeff', '')  # ufeff character from document start
    return final_list    


def translate() :
    tokenizer = nltk.data.load('tokenizers/punkt/dutch.pickle')
    final_output = ""
    with open("input.txt") as f:
        english_data = f.readlines()

    english_lines = sentence_tokenizer(english_data)

    english_sentences = list()
    for line in english_lines :
        l = tokenizer.tokenize(line)
        for sen in l :
            english_sentences.append(sen)

    out_file = open("output.txt", "w+")
    for index in range(len(english_sentences)) :
        current_sen = english_sentences[index]
        curr_translated_sen = ModelTester.sentence_tester1(current_sen, 2)
        out_file.write(curr_translated_sen)
        out_file.write(". ")
        
    print("Successfully translated! Translated document is 'output.txt' ")