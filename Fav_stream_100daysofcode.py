from time import sleep, time, asctime,localtime
import tweepy
import random
from credentials import *

#For authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            api.create_favorite(status.id_str)
            print("Created Favourite {}\n".format(status.id_str))

            #Uncomment the following line to enable retweeting too.
            #api.retweet(status.id_str)
            #print("Retweeted {}\n".format(status.id_str))

        except tweepy.TweepError as e:
            print(e)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#Change #100daysofcode with your hashtag or keyword, you can add any no. of keywords
myStream.filter(track=['#100daysofcode', '#js', '#nodejs', '#python'])
