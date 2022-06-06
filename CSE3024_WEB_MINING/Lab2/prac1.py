# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:44:30 2022

@author: anmol
"""

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

all = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']

text = "hey this is practise question one string. this is called a string"
text_tokens = word_tokenize(text)

token_without_sw = [word for word in text_tokens if not word in all]

print(set(token_without_sw))