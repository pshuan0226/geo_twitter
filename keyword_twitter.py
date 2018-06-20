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

while len(search_result) < max_result:
	count = max_result - len(search_result);
	try:
		new_twt = api.search(q=query, c=count, max_id = str(last_id - 1))
		if not new_twt:
			break
		search_result.extend(new_twt)
		last_id = new_twt[-1].id
		result_count += 1
	except tweepy.TweepError as e:
		break

print "got %d results" % result_count

