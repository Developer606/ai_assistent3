from newspaper import Article
import random
import string
import numpy as np
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



warnings.filterwarnings('ignore')
#download package from nltk
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)
article= Article('https://simple.wikipedia.org/wiki/flow')
article.download()
article.parse()
article.nlp()
corpus=article.text
#print
print(corpus)


text=corpus
sent_tokens=nltk.sent_tokenize(text)
# print(sent_tokens)

#creating a dictionary to remove the punctuation
remove_punct_dict=dict( (ord(punct),None) for punct in string.punctuation)
# print(string.punctuation)
# print(remove_punct_dict)

#create a function to return lower case words 
def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
# print(LemNormalize(text))
