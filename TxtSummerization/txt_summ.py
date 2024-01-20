import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
from string import punctuation
from heapq import nlargest


text=""" Deep learning is a subset of machine learning, which is essentially a neural network with three or more layers. These neural networks attempt to simulate the behavior of the human brain—albeit far from matching its ability—allowing it to “learn” from large amounts of data. While a neural network with a single layer can still make approximate predictions, additional hidden layers can help to optimize and refine for accuracy.

Deep learning drives many artificial intelligence (AI) applications and services that improve automation, performing analytical and physical tasks without human intervention. Deep learning technology lies behind everyday products and services (such as digital assistants, voice-enabled TV remotes, and credit card fraud detection) as well as emerging technologies (such as self-driving cars)."""

def summarizer(rawdocs):

    stopwords=list(STOP_WORDS)
    #print(stopwords)

    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)

    #print(doc)

    tokens=[token.text for token in doc]
    #print(tokens)


    word_freq={}
    word_freq = {}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    #print(word_freq)

    max_freq=max(word_freq.values())
    #print(max_freq) 

    for word in  word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq

    #print(word_freq)        

    sent_tokens=[sent for sent in doc.sents]
    #print(sent_tokens)     

    sent_scores = {}

    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    #print(sent_scores)
                    
    select_len = int(len(sent_tokens)*0.3)  
    #print(select_len)   



    summary=nlargest(select_len,sent_scores, key=sent_scores.get)
    #print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    #print(text)

    #print(summary)

    #print("length of the original text",len(text.split(' ')))

    #print("length of the summary text",len(summary.split(' ')))
     

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))





















