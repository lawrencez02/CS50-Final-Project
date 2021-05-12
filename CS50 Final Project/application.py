import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
import tweepy
import json
import sys
import praw
import requests
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    # Twitter
    # Guidance from https://www.geeksforgeeks.org/python-api-trends_place-in-tweepy/
    auth = tweepy.OAuthHandler("REDACTED", "REDACTED")
    auth.set_access_token("REDACTED", "REDACTED")
    api = tweepy.API(auth)
    trends = api.trends_place(id=23424977)
    gtrends = api.trends_place(id=1)

    # Reddit
    # Guidance from https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
    reddit = praw.Reddit(client_id='REDACTED', client_secret='REDACTED',
                         user_agent='REDACTED')
    hotposts = reddit.subreddit('all').hot(limit=25)
    redditposts = []
    postformat = {'title': '', 'score': '', 'subreddit': '', 'selftext': 'Image/Video'}
    for post in hotposts:
        postformat['title'] = post.title
        postformat['score'] = post.score
        postformat['subreddit'] = post.subreddit
        postformat['selftext'] = post.selftext
        redditposts.append(postformat)
        postformat = {'title': '', 'score': '', 'subreddit': '', 'selftext': 'Image/Video'}

    # News : 100 stories a day limit requests!
    # https://newsapi.org/docs/get-started
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&''apiKey=REDACTED')
    response = requests.get(url)
    news = response.json()
    articles = news['articles']

    # Google Trends
    # https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
    pytrend = TrendReq()
    dfus = pytrend.trending_searches(pn='united_states')
    dfus1 = pytrend.today_searches(pn='US')
    googleus = dfus.values.tolist()
    googleus1 = dfus1.values.tolist()

    # YouTube
    YouTubeURL = "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=US&maxResults=25&key=REDACTED"
    r = requests.get(url=YouTubeURL)
    data = r.json()

    return render_template("index.html", redditposts=redditposts, tweets=trends, gtweets=gtrends, articles=articles, gtrends=googleus, gtrends1=googleus1, ytrends=data)