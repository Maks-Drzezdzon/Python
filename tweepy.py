import tweepy
import csv

consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token (access_token , access_token_secret)

api = tweepy.API(auth)

print(" ")

my_account = api.me()
print('account name ' + my_account.name)
print('account location ' + my_account.location)
print('account friends count ' + my_account.friends_count)
print('account followers count ' + my_account.followers_count)


my_retweets = api.retweets_of_me()
for tweet in my_retweets:
    print(tweet.created_at , tweet.text)


user = api.get_user('Grimmr')
print('account name ' + user.name)
print('account location ' + user.location)
print('account friends count ' + user.friends_count)
print('account followers count ' + user.followers_count)
    
user_tweets = api.user_timeline('Grimmr') 
for tweet in user_tweets:
    print(tweet.created_at , tweet.text)
    
#save output to file
csvfile = open('twitter_data.csv' , 'wb')
csvwrite = csv.writer(csvfile)

for tweet in user_tweets:
    csvwrite.writerow ([(tweet.created_at).encode("utf-8") ,
                        (tweet.text).encode("utf-8")])