#!/usr/bin/python

import tweepy
import sys
import sqlite3

#All twitter app keys and secret stored in a separate file named "config.py."
#Read README.md for specific instructions
config = {}
execfile("config.py", config)

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

#tweepy api called with tokens set
api = tweepy.API(auth)


#initializing variables that include keywords to query
query = ('-filter:retweets')
result_count = 0
search_result = []
last_id = -1

#storing resutls into sqlite database
conn = sqlite3.connect('geo_twitter.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS search_results
	(id integer PRIMARY KEY, username text, tweet text UNIQUE, tweet_date text)""")

#the actual search happens here
tweets = [status for status in tweepy.Cursor(api.search, q=query, lang="en", 
	geocode="41.884938,-87.619960,0.3km", tweet_mode="extended").items()]

result_count = len(tweets)

#inserting tweets into table
for each in tweets:
	task = (each.user.name, each.full_text, each.created_at)
	c.execute("INSERT INTO search_results(username, tweet, tweet_date) VALUES(?, ?, ?)", task)

#close db
conn.commit()
conn.close()


print "%d results stored into database" % result_count
