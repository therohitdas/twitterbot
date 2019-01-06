from time import sleep, time, asctime,localtime
import tweepy
import random
import csv
from credentials import *

#variables
#Your username
username = "therohitdas"
#safelist
safe = ['1668100142', '864717654451474432']
#limit
lim = 40


#For authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)
un = 0


#Gets the list of your followers
followers = api.followers_ids(username)
#Gets the list of your following
following = api.friends_ids(username)



for item in following:
    #Compares them and destroys friendship., Bye Bye Unfollowers
    if item not in followers and item not in safe:
        try:
            api.destroy_friendship(item)
            print('Destroyed friendship with {}'.format(str(item)))
            sleep(random.randint(5,7))
            un = un + 1
        except tweepy.TweepError as e:
            print(e)
            sleep(20)
    if un == lim:
        break


print("Unfollowed {} Accounts".format(str(un)))