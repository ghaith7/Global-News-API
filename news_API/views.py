from django.shortcuts import render
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
import tensorflow as tf
import pickle
from .scraping import *
from .paths import *
from .preprocess import *
import os 

def list2string(l):
    s = ""
    for e in l:
        s=s+e+":"
    return s

# Create your views here.
@api_view(['GET'])
def refresh(request):
    print("starting...")
    model_Ner=tf.keras.models.load_model(nerPath)
    file = open(dictionairyPath, "rb")
    word2idx = pickle.load(file)
    model_cat=tf.keras.models.load_model(categoriesPath)
    file = open(dictionairyPath2, "rb")
    word2idxcat = pickle.load(file)
    print('collecting tweets...')
    tweetsRaw = getDailyTweets()
    formated_tweets = preprocess(tweetsRaw,model_Ner,word2idx,model_cat,word2idxcat)
    for t in formated_tweets:
        ne = list2string(t["namedE"])
        ht = list2string(t["hashtags"])
        tweet = Tweet(text = t["text"], username = t["username"], retweet_count = t["retweet_count"],favorite_count = t["favorite_count"],hashtags = ht,namedE = ne,category = t["categorie"])
        tweet.save()
    print("complted and ready")
    return Response("refresh completed")

@api_view(['GET'])
def newsList(request):
    news = Tweet.objects.all()
    serializer = TweetSerializer(news,many=True)
    return Response(serializer.data)
