import ModelTrainer
import ModelTester
import DutchtoEnglish
import EnglishtoDutch
import Jaccard
import CosineSimilarity
import nltk

nltk.download('punkt')
while True:
    try:
        mode = int(input('\n\nPlease choose what you want to do: \n\t1: Train the Model\n\t2: Test sentence to translate\n\t3: Translate a Dutch document to English \n\t4: Translate an English document to Dutch \n\t5: Calculate Jaccard coefficient \n\t6: Calculate Cosine Similarity \n\t7:For exit\n'))
    except ValueError:
        print ("Not a number")

    if mode == 1:
        ModelTrainer.model_trainer()

    elif mode == 2:
        try:
            translate_option = int(input('Select translation option: \n\t1: Dutch to English \n\t2: English to Dutch\n'))
        except ValueError:
            print ("Not a number")
        if translate_option > 2 or translate_option < 1 :
            print("Invalid Option")
            exit()
        sentence_to_translate = input("Plese provide sentence to translate: ")

        translated_sentence = ModelTester.test(sentence_to_translate,translate_option)
        print(translated_sentence)

    elif mode == 3:             #translate Dutch document to English
        DutchtoEnglish.translate()

    elif mode == 4:             #translate English document to Dutch
        EnglishtoDutch.translate()

    elif mode == 5:             #Calculate Jaccard Correlation Coefficient
        try:
            language = int(input('\n\nPlease choose the language of output and actual documents \n\t1: Dutch\n\t2:English\n'))
        except ValueError:
            print ("Not a number")

        if language > 2 or language < 1 :
            print("Invalid Option")
            exit()

        Jaccard.calcJaccardCoeff(language)


    elif mode == 6:             #Calculate Cosine Similarity
        try:
            language = int(input('\n\nPlease choose the language of output and actual documents \n\t1: Dutch\n\t2:English\n'))
        except ValueError:
            print ("Not a number")

        if language > 2 or language < 1 :
            print("Invalid Option")
            exit()
            
        CosineSimilarity.calcCosineSim(language)
        
    elif mode == 7:
        break
    else:
        print("invalid mode")

print("goodbye!")