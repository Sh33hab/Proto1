import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
from string import punctuation
from heapq import nlargest

text=""" Deep learning is a subset of machine learning, which is essentially a neural network with three or more layers. These neural networks attempt to simulate the behavior of the human brain—albeit far from matching its ability—allowing it to “learn” from large amounts of data. While a neural network with a single layer can still make approximate predictions, additional hidden layers can help to optimize and refine for accuracy.

Deep learning drives many artificial intelligence (AI) applications and services that improve automation, performing analytical and physical tasks without human intervention. Deep learning technology lies behind everyday products and services (such as digital assistants, voice-enabled TV remotes, and credit card fraud detection) as well as emerging technologies (such as self-driving cars)."""

stopwords=list(STOP_WORDS)
#print(stopwords)

#if we eliminate the words from the english words or sentences it does not effect at all : is called STOP WORDS



nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
print(doc)


