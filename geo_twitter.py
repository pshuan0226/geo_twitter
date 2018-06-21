#!/usr/bin/env python
#Created by Patricia Huang
#Project purpose: Geofencing/feed filter for HCSC

import tweepy
import time
import sys
import csv


#Preparing for result.csv
outfile = "result.csv"
csvfile = file(outfile, "w") 
csvwriter = csv.writer(csvfile, delimiter=' ')


#Consumer/Access tokens stored in config.py
#Please create your own config.py
config = {}
execfile("config.py", config)


auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

api = tweepy.API(auth)


#Modify query for more/fewer keywords
query = ('bcbsil OR HCSC -filter:retweets')
max_result = 1000
result_count = 0
search_result = []
last_id = -1
backoff_counter = 1


#Here is all the fun!
#Geocode coordinates set to BCBSIL HQ
while True:
	try:
		for each in tweepy.Cursor(api.search, q=query, lang="en", 	
			geocode="41.884938,-87.619960,20km", 
			tweet_mode="extended").items(max_result):
			#Printing to result.csv
			last_id += 1
			user = each.user.name 
			tweet = each.full_text.encode('utf-8')
			time = each.created_at
			row = [last_id, user, time, tweet]
			csvwriter.writerow(row)
		break
	except tweepy.TweepError as e:
		print(e.reason)
		time.sleep(60*backoff_counter)
		backoff_counter += 1
		continue
		
	
#Feedback to user
print "got %d results\n" % (last_id + 1)
print "written to %s\n" % outfile


#End
csvfile.close()
