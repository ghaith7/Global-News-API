import tensorflow as tf
import numpy as np
import nltk

def categorize(formated_tweets,model,word2idx):
    subst_val = len(word2idx) -1
    max_len= 30

    for t in formated_tweets:
        # preprocess
        tokens=nltk.word_tokenize(t["text"].split("https:")[0])
        indexs=[]
        for token in tokens:
            if token in list(word2idx.keys()):
                indexs.append(word2idx[token])
            else:
                indexs.append(word2idx["PADword"])
        while(len(indexs)<max_len):
            indexs.append(subst_val)
        if len(indexs)>max_len:
            indexs=indexs[:max_len]
        processed=np.array(indexs).reshape((1,30))
        pred=model.predict(processed)
        tags={
           0: 'politics', 1: 'sports', 2: 'tech', 3: 'other'
        }
        res=pred.argmax()
        t["categorie"]=tags[res]
    return formated_tweets