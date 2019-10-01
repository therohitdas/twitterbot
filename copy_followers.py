from time import sleep
import tweepy
import random
from credentials import *

###Variables
#Your username
username = "therohitdas"
#target username =  the followers will be copied from this account
username_target = "freecodecamp"
#limit =  no. of time the operation will be performed, 30 is good choice
lim = 5



#For authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)

#Gets the list of target's followers
followers = api.followers_ids(username_target)
#Gets the list of your following
following = api.friends_ids(username)


for item in followers:
    #Compares to find if I am following them already
    if item not in following:
        try:
            api.create_friendship(item)
            print('Created friendship with {}'.format(str(item)))
            sleep(random.randint(5,7))
            un =+ 1
        except tweepy.TweepError as e:
            print(e)
            sleep(20)
        #change un value to limit no of people to be followed in one season..
        if un >= lim:
            break
print(un)
