#!/usr/bin/python

import tweepy
import sys
import sqlite3
import dataset
import itertools
import logging

#connect to db thru dataset
db = dataset.connect('sqlite:///geo_twitter.db')

#set logging config
logging.basicConfig(format='%(asctime)s:%(message)s', 
	datefmt='%m/%d/%Y %I:%M:%S %p', filemode='w',
	filename='streamer_hcsc.log', level=logging.INFO)

#StreamListener subclass declaration
class myStreamListener(tweepy.StreamListener):

	def __init__(self):
		super(myStreamListener, self).__init__()
		self.counter = 0
		print 'Streaming keyword related tweets... (Ctrl+C to quit)'
	#	self.limit = 10

	def on_status(self, status):
		#prints tweets that are not retweets
		if status.retweeted:
			return

		#fetch full text if available
		try:
			content = status.extended_tweet["full_text"]
		except AttributeError:
			content = status.text

		#fetch tweet coordinates if available
		t_location = None
		if status.coordinates is not None:
			t_location = status.coordinates

		#fetch other attributes
		name = status.user.name
		u_location = status.author.location
		date = status.created_at

		table = db['stream_results']

		#insert values into the table
		try:
			table.insert(dict(
				username = name,
				tweet = content,
				tweet_date = date,	
				user_location = u_location,
				tweet_coord = t_location,
			))
			self.counter += 1

			#in case you need to set a limit to tweets retreived
			#if(self.counter >= self.limit):
				#stream.disconnect()

			#give response to user
			logging.info('%d tweets fetched', self.counter)
			print '%d tweets fetched' % self.counter
		except Exception as e:
			logging.error('Error encountered: %s', e)
			print e

	def on_error(self, status_code):
		#if rate limit reached then disconnect
		if status_code == 420:
			print 'Rate limit reached.\n'
			return False
		#if proxy authentication needed
		if status_code == 407:
			print 'Please re-enter your proxy authentication credentials.\n'
			return False

	#called when google sends a disconnect notice
	def on_disconnect(self, notice):
		print 'Disconnect notive received. Getting back at streaming...\n'
		return

	def on_timeout(self):
		print 'Timed out. Getting back at streaming...\n'
		return

def main():
	#All twitter app keys and secret stored in a separate file named "config.py."
	#Read README.md for specific instructions
	config = {}
	execfile("config.py", config)

	auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
	auth.set_access_token(config["access_key"], config["access_secret"])

	#tweepy api called with tokens set
	my_proxy = 'https://proxyserver:port/'
	api = tweepy.API(auth, proxy=myproxy)

	#Start streaming!
	#Note: filter returns tweets with the values in track XOR tweets from this location
	#Note: note that most users turn off exact locations for tweets
	while True:
		try:
			stream_listener = myStreamListener()
			stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
			stream.filter(track=['twitter'], 
				locations=[21.554928,-87.719860, 50.885049, -80.612100])
		except Exception as e:
			logging.error('Error encountered: %s', e)
			print(e)
			print('Restarting the stream...')
			continue


if __name__ == '__main__':
	try:
		main()
	#handles Clrl+C quit
	except KeyboardInterrupt as e:
		print('\nStreamer interrupted.')
		sys.exit(0)
