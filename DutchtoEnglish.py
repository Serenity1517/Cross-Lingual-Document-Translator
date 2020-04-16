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
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    final_output = ""
    with open("input.txt") as f:
        dutch_data = f.readlines()

    dutch_lines = sentence_tokenizer(dutch_data)

    dutch_sentences = list()
    for line in dutch_lines :
        l = tokenizer.tokenize(line)
        for sen in l :
            dutch_sentences.append(sen)

    out_file = open("output.txt", "w+")
    for index in range(len(dutch_sentences)) :
        current_sen = dutch_sentences[index]
        curr_translated_sen = ModelTester.sentence_tester1(current_sen, 1)
        out_file.write(curr_translated_sen)
        out_file.write(". ")
        
    print("Successfully translated! Translated document is 'output.txt' ")
    
