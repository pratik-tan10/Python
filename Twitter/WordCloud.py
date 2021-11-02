import tweepy
import pandas as pd

#Authoraization
consumer_key = "Enter your consumer key" #Enter your key as string
consumer_secret = "Enter your consumer key secret"
access_token = "Enter your access token"
access_token_secret = "Enter your access token secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#make a CSV of keywords
