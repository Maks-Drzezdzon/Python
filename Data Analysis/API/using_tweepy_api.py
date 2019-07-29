import tweepy 
import os
import sys

keys_file = open("C:/Users/Grim/Desktop/twitter_key.txt")
text = keys_file.readlines()

consumer_key = text[0].strip().split('"')[1]
consumer_secret = text[1].strip().split('"')[1]
access_token = text[2].strip().split('"')[1]
access_token_secret = text[3].strip().split('"')[1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
