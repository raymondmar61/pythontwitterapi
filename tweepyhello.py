#YouTube Anthony Sistilli
#https://github.com/tweepy/tweepy
#http://tweepy.org

import tweepy
import twitter_credentials as tc

#Getting Started https://tweepy.readthedocs.io/en/latest/getting_started.html
#Download your home timeline tweets and print each one of their texts to the console.
auth = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
auth.set_access_token(tc.accesstoken, tc.accesstokensecret)
#api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True) #https://stackoverflow.com/questions/38775997/getting-this-error-when-using-tweepy
public_tweets = api.home_timeline(count=1)
for tweet in public_tweets:
	#print(tweet.text)
	print(tweet.text.encode("utf-8"))

'''
https://developer.twitter.com/
https://developer.twitter.com/en/docs/tweets/post-and-engage/overview
Go to API Reference https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update
Find the api.home_timeline().  Do a search.
Get Tweet timelines https://developer.twitter.com/en/docs/tweets/timelines/overview, https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline
'''

#https://tweepy.readthedocs.io/en/latest/api.html#api-reference
inin61 = api.user_timeline(user_id="inin61", count=1)
for eachinin61 in inin61:
	print(eachinin61.created_at)
	print(eachinin61.text)
	print(eachinin61.entities)
	print(eachinin61.entities["urls"])
	print(eachinin61.entities["urls"][0])
	print(eachinin61.entities["urls"][0]["expanded_url"])
'''
2019-11-20 22:20:35
The Living Years by Mike + The Mechanics https://t.co/je03cuWZ87 #mysongoftheday
{'hashtags': [{'text': 'mysongoftheday', 'indices': [65, 80]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/je03cuWZ87', 'expanded_url': 'https://www.youtube.com/watch?v=5hr64MxYpgk', 'display_url': 'youtube.com/watch?v=5hr64M…', 'indices': [41, 64]}]}
[{'url': 'https://t.co/je03cuWZ87', 'expanded_url': 'https://www.youtube.com/watch?v=5hr64MxYpgk', 'display_url': 'youtube.com/watch?v=5hr64M…', 'indices': [41, 64]}]
{'url': 'https://t.co/je03cuWZ87', 'expanded_url': 'https://www.youtube.com/watch?v=5hr64MxYpgk', 'display_url': 'youtube.com/watch?v=5hr64M…', 'indices': [41, 64]}
https://www.youtube.com/watch?v=5hr64MxYpgk
'''
