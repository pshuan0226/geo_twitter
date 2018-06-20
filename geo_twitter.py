#!/usr/bin/python
#code from https://github.com/ideoforms/python-twitter-examples

from twitter import *
import sys
import csv


latitude = 41.885000
longitude = -87.619670
outfile = "results.csv"
max_range = 1

config = {}
execfile("config.py", config)

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)

row = ["user", "text", "latitude", "longitude"]
csvwriter.writerow(row)

result_count = 0
num_results = 50
last_id = None

while result_count < num_results:
	query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

	for result in query["statuses"]:
		if result["geo"]:
			user = result["user"]["screen_name"]
			text = result["text"]
			text = text.encode('ascii', 'replace')
			latitude = result["geo"]["coordinates"][0]
			longitude = result["geo"]["coordinates"][1]

			row = [ user, text, latitude, longitude ]
			csvwriter.writerow(row)
			result_count += 1
		last_id = result["id"]

	print "got %d results" % result_count

csvfile.close()

print "written to %s" % outfile
	
