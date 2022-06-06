import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

all = (stopwords.words('english'))
all.append('vit')

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# remove punctuations
text = "is! anmol vit student? ya, he is."
for ele in text:
    if ele in punc:
        text = text.replace(ele, "")

# tokenization
text_tokens = word_tokenize(text)

token_without_sw = [word for word in text_tokens if not word in all]

print(token_without_sw)


# print(token_without_sw)