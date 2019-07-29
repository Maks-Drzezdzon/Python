import tweepy 
import os
import sys
import time
from bs4 import BeautifulSoup

soup = BeautifulSoup(PLACE_HOLDER.text,'html.parser')
# finds pattern in html with tags span class short-desc
results = soup.find_all('span', attrs={'class' : 'short-desc'})


with open("C:/Users/Grim/Desktop/twitter_key.txt") as keys_file:
    text = keys_file.readlines()

consumer_key = text[0].strip().split('"')[1]
consumer_secret = text[1].strip().split('"')[1]
access_token = text[2].strip().split('"')[1]
access_token_secret = text[3].strip().split('"')[1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

time_stamp = time.ctime()
api.update_status("api test on " + time_stamp)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (f"{tweet.user.name} said {tweet.text}")
