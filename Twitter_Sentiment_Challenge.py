# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:09:59 2019

@author: nilsh
"""

from textblob import TextBlob
import tweepy
import pandas as pd
import numpy as np

wiki=TextBlob("The FED certainly has flip-floped")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)

consumer_key = "8DJOSVDajdKJtOvkVkpZwbLnA"
consumer_secret = "WoIcFRZbEojAF5HRotF2y5HQTgdzrZnJI0zTWIdBmHnETHsAFZ"

access_token = "714807435559628800-o0JMhiqQTyY5JLAgly5I2ooXV0kesRk"
access_token_secret = "F1tm2oajhLaEB7pw2v7Bo0joIJfGXSsczZ2F00b9LGX7Y"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search("FED")

tweets = pd.DataFrame(columns=["Text","Sentiment","Polarity","Subjectivity"])

for i,tweet in enumerate(public_tweets):
    tweets.loc[i]=""
    analysis=TextBlob(tweet.text)
    tweets["Text"].loc[i]=tweet.text
    tweets["Sentiment"].loc[i]=analysis.sentiment.polarity
    tweets["Polarity"].loc[i]=np.sign(tweets["Sentiment"].loc[i])
    tweets["Subjectivity"].loc[i]=analysis.sentiment.subjectivity

    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print("-----------------------------------------------")

polarity_classifier={0:"Neutral",1:"Positive",-1:"Negative"}
tweets["Polarity"]=tweets["Polarity"].map(polarity_classifier)

tweets.to_excel("Tweet_Sentiment.xlsx",index=False)
tweets.to_csv("Tweet_Sentiment.csv",index=False)

















