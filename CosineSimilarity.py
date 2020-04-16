import string
import IBM1_EM
import Utils
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk.data
import DutchtoEnglish

nltk.download('stopwords')

def calcCosineSim(language) :

    if(language==1) :

        tokenizer = nltk.data.load('tokenizers/punkt/dutch.pickle')
        
        with open("output.txt") as f:
            output = f.readlines()
        with open("actual.txt") as g:
            actual = g.readlines()

        # tokenization 

        output_lines = DutchtoEnglish.sentence_tokenizer(output)
        actual_lines = DutchtoEnglish.sentence_tokenizer(actual)

        output_sentences = list()
        actual_sentences = list()

        for line in output_lines :
            l = tokenizer.tokenize(line)
            for sen in l :
                output_sentences.append(sen)
        for line in actual_lines :
            l = tokenizer.tokenize(line)
            for sen in l :
                actual_sentences.append(sen)

        no_of_sen = len(output_sentences)
        average = 0.0

        # sw contains the list of stopwords 
        sw = stopwords.words('dutch')

        for index in range(no_of_sen) :
                    
            l1 =[];l2 =[] 
            
            X_list = word_tokenize(output_sentences[index].lower())
            Y_list = word_tokenize(actual_sentences[index].lower())

            # remove stop words from string 
            X_set = {w for w in X_list if not w in sw}  
            Y_set = {w for w in Y_list if not w in sw} 

            X_set.discard('.')
            X_set.discard('(')
            X_set.discard(')')
            X_set.discard('"')
            X_set.discard(',')
            X_set.discard('-')
            X_set.discard('\'')
            
            Y_set.discard('.')
            Y_set.discard('(')
            Y_set.discard(')')
            Y_set.discard('"')
            Y_set.discard(',')
            Y_set.discard('-')
            Y_set.discard('\'')
            
            
            # form a set containing keywords of both strings  
            rvector = X_set.union(Y_set)  
            for w in rvector: 
                if w in X_set: l1.append(1) # create a vector 
                else: l1.append(0) 
                if w in Y_set: l2.append(1) 
                else: l2.append(0) 
            c = 0
            
            # cosine formula  
            for i in range(len(rvector)): 
                    c+= l1[i]*l2[i] 
            cosine = c / float((sum(l1)*sum(l2))**0.5) 

            average += cosine/no_of_sen
            print("\ncosine =",cosine)

        print("\nfinal cosine similarity: ",average) 

    elif(language==2) :
        
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        with open("output.txt") as f:
            output = f.readlines()
        with open("actual.txt") as g:
            actual = g.readlines()

        # tokenization 

        output_lines = DutchtoEnglish.sentence_tokenizer(output)
        actual_lines = DutchtoEnglish.sentence_tokenizer(actual)

        output_sentences = list()
        actual_sentences = list()

        for line in output_lines :
            l = tokenizer.tokenize(line)
            for sen in l :
                output_sentences.append(sen)
        for line in actual_lines :
            l = tokenizer.tokenize(line)
            for sen in l :
                actual_sentences.append(sen)

        no_of_sen = len(actual_sentences)
        average = 0.0

        # sw contains the list of stopwords 
        sw = stopwords.words('english')

        for index in range(no_of_sen) :
                    
            l1 =[];l2 =[] 
            
            X_list = word_tokenize(output_sentences[index].lower())
            Y_list = word_tokenize(actual_sentences[index].lower())

            # remove stop words from string 
            X_set = {w for w in X_list if not w in sw}  
            Y_set = {w for w in Y_list if not w in sw} 

            X_set.discard('.')
            X_set.discard('(')
            X_set.discard(')')
            X_set.discard('"')
            X_set.discard(',')
            X_set.discard('-')
            X_set.discard('\'')

            Y_set.discard('.')
            Y_set.discard('(')
            Y_set.discard(')')
            Y_set.discard('"')
            Y_set.discard(',')
            Y_set.discard('-')
            Y_set.discard('\'')
            
            # form a set containing keywords of both strings  
            rvector = X_set.union(Y_set)  
            for w in rvector: 
                if w in X_set: l1.append(1) # create a vector 
                else: l1.append(0) 
                if w in Y_set: l2.append(1) 
                else: l2.append(0) 
            c = 0
            
            # cosine formula  
            for i in range(len(rvector)): 
                    c+= l1[i]*l2[i] 
            cosine = c / float((sum(l1)*sum(l2))**0.5) 

            average += cosine/no_of_sen
            print("\ncosine=",cosine)

        print("\nfinal cosine similarity: ",average) 

