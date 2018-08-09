# geo_twitter

## Purpose
A project mainly for filtering tweets using geofencing and keyword tuning.

### One time search 
`print_geo.py` directly prints to terminal

`csv_geo.py` outputs results to a csv file

`sqlite_geo.py` outputs results to a sqlite database

### Streamer
`streamer.py` streams tweets with hcsc related keywords with a location filter set as well

### Visualization
`dash_table.py` allows visualization of data in a table (with max rows set) through Dash

## Before you run any three of the scripts
1. Login to twitter and create a twitter application at https://apps.twitter.com/
2. Create a config.py and fill out your consumer and access tokens with this format

```python
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

3. Keywords and coordinates are currently set to HCSC, but feel free to include more in the `query` parameter
4. Run the following command to install the necessary packages:

```python
pip install dataset tweepy pandas dash==0.22.0 
            dash-renderer==0.13.0 dash-html-components==0.11.0 
            dash-core-components==0.26.0 plotly
```
