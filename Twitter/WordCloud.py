import tweepy
import pandas as pd

#Authoraization
#make a CSV of keywords
#pulls text information from tweets
#creates a pandas dataframe
#creates a csv from data frame
#Choose Keyword
#Load data for data CLeaning
#Remove Emoji
#Remove URL
#Remove menthions and hash symbol
#Html to plaintext
#Finally CLeal everything
#Pass tweets to clean.
#Generate Word Cloud
#Custom mask for wordcloud

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
% matplotlib inline

# Load in the dataframe
df = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)

# Looking at first 5 rows of the dataset
df.head()

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),
                                                                           ", ".join(df.variety.unique()[0:5])))

print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),
                                                                                      ", ".join(df.country.unique()[0:5])))
