# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:52:52 2022

@author: anmol
"""

import nltk
from nltk.tokenize import word_tokenize

sentence = "The First sentence is about Python, The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
text_tokens = word_tokenize(sentence)
print(text_tokens)

sentence_tokens = nltk.sent_tokenize(sentence)
print (sentence_tokens)