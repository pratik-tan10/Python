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
def keyword_to_csv(keyword,recent):
    try:
        tweets = tweepy.Cursor(api.search,q=keyword).items(recent) #creates query method
        tweets_list = [[tweet.text] for tweet in tweets] 
#pulls text information from tweets
        df = pd.DataFrame(tweets_list,columns=['Text']) 
#creates a pandas dataframe
        df.to_csv('{}.csv'.format(keyword), sep=',', index = False) 
 #creates a csv from data frame
    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)

        
