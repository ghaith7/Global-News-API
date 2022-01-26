import tensorflow as tf
import numpy as np
import nltk


def extract_named_entities(formated_tweets,model,word2idx):


    subst_val = len(word2idx) -1
    max_len= 50

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
        processed=np.array(indexs).reshape((1,50))
        pred=model.predict(processed)
        tags=[]
        for i in range(0,len(tokens)):
            if pred[0][i]> 0.8:
                tags.append(tokens[i])
        t["namedE"]=tags
    return formated_tweets


    

