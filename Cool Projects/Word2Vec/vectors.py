from scipy.spatial.distance import cosine

import math
import numpy as np

with open("words.txt",encoding='utf-8') as f:
    words = dict()
    for i in range(50000):
        row = next(f).split()
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        words[word] = vector


def distance(w1, w2):
    return cosine(w1, w2)


def closest_words(embedding):
    distances = {
        w: distance(embedding, words[w])
        for w in words
    }
    return sorted(distances, key=lambda w: distances[w])[:2]


def closest_word(embedding):
    return closest_words(embedding)[0]

def apply_change(text, startWord, endWord):
    '''
    text = text you want modified
    startWord = the word that is measured the distance 
    away from the end word. 
    words like this will be changed to words like the end word'''
    
    changeVector = words[endWord] - words[startWord]
    
    splitText = text.split()
    
    for i in range(len(splitText)):
        if splitText[i] in words:
            wordVector = words[splitText[i]]
            newVector = wordVector + changeVector
            newWords = closest_words(newVector)
            splitText[i] = str(newWords)
            
    return " ".join(splitText)
