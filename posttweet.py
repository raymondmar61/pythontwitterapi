#Youtube Jie Jenn
#Video How To Post A Live Tweet With Python Using Twitter API [720p]

import tweepy
import twitter_credentials as tc

def OAuth():
	try:
		authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
		authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
		return authenticate
	except Exception as e:
		return None
oauth = OAuth()
api = tweepy.API(oauth)
api.update_status("I post the tweet learning Python Twitter API using Tweepy library.")