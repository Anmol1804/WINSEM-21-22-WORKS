import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = '''Lorem Ipsum is simply dummy text of the printing and typesetting 
            industry and has been the standard dummy text'''
    

sw = (stopwords.words('english'))

text_tokens = word_tokenize(text)

token_without_sw = [word for word in text_tokens if not word in sw]
print(token_without_sw)


#nltk.download('averaged_perceptron_tagger')
tagged_ls = nltk.pos_tag(text_tokens)
print(tagged_ls)
