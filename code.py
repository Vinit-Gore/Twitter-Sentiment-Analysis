import tweepy
from textblob import TextBlob
import csv
import pandas as pd

# Step 1 - Authenticate
consumer_key= 'Cy72f2w6iz5ePJmpFgFVxaQ5F'
consumer_secret= 'nt9JA6xiPiKiAOOMRNey9becf4dpCfVtY43SNCJg7TFfme05R5'

access_token='995022656-TafrOBhBOmaYGoRWXvc55eYk5h0uI0yWzCUoBHxf'
access_token_secret='FsLMYnRixkySLpuGoPbkUEU6ihOPPRtvdllMKLAYWIaKc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = input("Please enter the keyword to search : ")
public_tweets = api.search(keyword)

tweet_list = []
review_list = []

for tweet in public_tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    # print(tweet.sentiment)
    # print("")
    tweet_list.append(tweet.text)
    if analysis.sentiment.polarity > 0:
        review_list.append('positive')
    else:
        review_list.append('negative')
df = pd.DataFrame({'Tweets' : tweet_list, 'Review':review_list})
df.to_csv(keyword+'Data.csv')