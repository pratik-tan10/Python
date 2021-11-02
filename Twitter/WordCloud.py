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
 
#Choose Keyword
keyword = 'SpaceX'+ " -filter:retweets" #excludes retweets
recent  = 3000
keyword_to_csv(keyword, recent)

#Load data for data CLeaning
df = pd.read_csv("./#spacex-filter:retweets.csv") #loads csv file into pandas dataframe
pd.options.display.max_colwidth = 200 
df.head() #prints out first few columns in a dataframe

#Remove Emoji
a = df.loc[1272].to_string() #loads the row from dataframe
print(a)
regex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
match = re.sub(regex_pattern,'',a) #replaces pattern with ''
print(match)

#Remove URL
a = df.loc[0].to_string()
print(a)
pattern = re.compile(r'(https?://)?(www\.)?(\w+\.)?(\w+)(\.\w+)(/.+)?')
match = re.sub(pattern,'',a)
print(match)

#Remove menthions and hash symbol
a = df.loc[3].to_string()
print(a
re_list = [’@[A-Za-z0–9_]+’, '#']
combined_re = re.compile( '|'.join( re_list) )
match = re.sub(combined_re,’’,a))
print(match)

#Html to plaintext
from bs4 import BeautifulSoup
a = df.loc[27].to_string()
print(a)

del_amp = BeautifulSoup(a, 'lxml')
del_amp_text = del_amp.get_text()
print(del_amp_text)

#Finally CLeal everything
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
token = WordPunctTokenizer()
def cleaning_tweets(t):
    del_amp = BeautifulSoup(t, 'lxml')
    del_amp_text = del_amp.get_text()
    del_link_mentions = re.sub(combined_re, '', del_amp_text)
    del_emoticons = re.sub(regex_pattern, '', del_link_mentions)
    lower_case = del_emoticons.lower()
    words = token.tokenize(lower_case)
    result_words = [x for x in words if len(x) > 2]
    return (" ".join(result_words)).strip()
