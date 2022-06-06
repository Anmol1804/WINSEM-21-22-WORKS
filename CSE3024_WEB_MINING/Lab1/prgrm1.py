import nltk
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# text = "is anmol vit student"
# text_tokens = word_tokenize(text)

# token_without_sw = [word for word in text_tokens if not word in stopwords.words()]
# # print(token_without_sw)

all = (stopwords.words('english'))
all.remove('is')
print(all)

text = "is anmol vit student?"
text_tokens = word_tokenize(text)

token_without_sw = [word for word in text_tokens if not word in all]
print(token_without_sw)