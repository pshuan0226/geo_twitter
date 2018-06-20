import tweepy
import sys

config = {}
execfile("config.py", config)

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

api = tweepy.API(auth)

query = ('bcbsil OR HCSC -filter:retweets')
max_result = 1000
result_count = 0
search_result = []
last_id = -1

search_result = [status for status in tweepy.Cursor(api.search, q=query, lang="en", geocode="41.884938,-87.619960,20km", tweet_mode="extended").items(max_result)]

result_count = len(search_result)

for each in search_result:
	print each.user.name + " "
	print each.full_text + "\n"
	

print "got %d results" % result_count

