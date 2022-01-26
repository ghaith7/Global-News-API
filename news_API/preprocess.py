from .scraping import *
from .named_entities_extraction import *
import nltk
from .tagging import *

def reformateTweet(tweet):
    tweet =tweet._json
    new_tweet = {
        "text" : tweet["text"], 
        "username" : tweet["user"]["name"],
        "retweet_count" : tweet["retweet_count"],
        "favorite_count" : tweet["favorite_count"], 
        "hashtags" : tweet["entities"]["hashtags"],
        "namedE" : [],
        "categorie" : "",
    }
    return new_tweet

def getFormatedTweets(tweetsRaw):
    formated_tweets=[]
    for tweet in tweetsRaw:
        formated_tweets.append(reformateTweet(tweet))
    return formated_tweets

def get_all_unique_words(formated_tweets):
    vocabulary=[]
    for t in formated_tweets:
        words=nltk.word_tokenize(t["text"].split("https:")[0] )
        vocabulary.extend(words)
    vocabulary=list(set(vocabulary))
    return vocabulary


def preprocess(tweetsRaw,model_Ner,word2indx,model_categories,word2indxcat):
    print("started preprocessing")
    formated_tweets = getFormatedTweets(tweetsRaw)
    formated_tweets = extract_named_entities(formated_tweets,model_Ner,word2indx)
    formated_tweets = categorize(formated_tweets,model_categories,word2indxcat)
    return formated_tweets

