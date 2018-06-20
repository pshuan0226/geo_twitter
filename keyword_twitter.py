import tweepy
import sys

config = {}
execfile("config.py", config)

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

api = tweepy.API(auth)

query = ('Blue Cross OR bcbsil')
max_result = 100
result_count = 0
search_result = []
last_id = -1

for tweet in tweepy.Cursor(api.search, q=query, count = max_result, tweet_mode = "extended").items():
	print tweet.full_text

print "got %d results" % result_count

