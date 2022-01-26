import tweepy                   # Python wrapper around Twitter API
import json
import csv
from datetime import date
from datetime import datetime ,timedelta
import time
import pytz
from .keys import *

# supported twitter accounts List

accountList=[
    "BreakingNews",
    "cnnbrk",
    "TheEconomist",
    "nytimes",
    "washingtonpost",
    "BBCWorld",
    "AJENews",
    "AJEnglish"
]

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def end_datetime(n_days):
    current = datetime.now()
    past_date = current + timedelta(days = -n_days)
    utc=pytz.UTC
    past_date = utc.localize(past_date) 
    return past_date

def get_latest_tweets(screen_name,n_days):
    tweets=[]
    new_tweets = api.user_timeline(screen_name = screen_name,count=5)
    tweets.extend(new_tweets)
    
    oldest = tweets[-1].id - 1
    today=True
    past_date=end_datetime(n_days)
    while(today):
        new_tweets = api.user_timeline(screen_name = screen_name,count=5,max_id=oldest)
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1
        latest_time= tweets[-1].created_at
        if (latest_time<past_date):
            today = False
    return tweets

def getDailyTweets():
    tweetsRaw=[]
    for account in accountList:
        tweetsRaw.extend(get_latest_tweets(account,1))
    return tweetsRaw

print(len(getDailyTweets()))