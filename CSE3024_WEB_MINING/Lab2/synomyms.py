import nltk
#nltk.download('wordnet')

from nltk.corpus import wordnet

syns = []

for syn in wordnet.synsets('web'):
    for lm in syn.lemmas():
        syns.append(lm.name())
        
print(set(syns))

# print(token_without_sw)