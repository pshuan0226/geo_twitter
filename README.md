# hcsc_geo

## Purpose
A project mainly for filtering tweets using geofencing and keyword tuning.
keyword_twitter.py directly prints to terminal
geo_twitter.py outputs results to a csv file


## Before you run geo_twitter.py
1. Login to twitter and create a twitter application at https://apps.twitter.com/
2. Create a config.py and fill out your consumer and access tokens with this format

```python
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

3. Keywords and coordinates are currently set to HCSC
