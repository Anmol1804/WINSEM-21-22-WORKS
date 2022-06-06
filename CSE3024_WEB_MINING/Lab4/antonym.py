# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:49:10 2022

@author: anmol
"""
from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("men"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name()) #adding into antonyms
print(set(antonyms))