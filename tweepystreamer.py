#YouTube LucidProgramming

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import twitter_credentials as tc
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
#print(tc.accesstoken)

#Twitter client
class TwitterClient():
	def __init__(self, twitteruser=None):
		self.authenticater = TwitterAuthenticator().authenticatetwitterapp()
		self.twitterclient = API(self.authenticater)
		self.twitteruser = twitteruser
	def gettwitterclientapi(self):
		return self.twitterclient
	def getusertimelinetweets(self, numberoftweets):
		tweetslist = []
		for tweet in Cursor(self.twitterclient.user_timeline, id=self.twitteruser).items(numberoftweets):
			tweetslist.append(tweet)
		return tweetslist
	def getfriendlist(self, numberoffriends):
		friendlist = []
		for friend in Cursor(self.twitterclient.friends, id=self.twitteruser).items(numberoffriends):
			friendlist.append(friend)
		return friendlist
	def gethometimelinetweets(self, numberoftweets):
		hometimelinetweetslist = []
		for tweet in Cursor(self.twitterclient.home_timeline, id=self.twitteruser).items(numberoftweets):
			hometimelinetweetslist.append(tweet)
		return hometimelinetweetslist

#Twitter authenticater
class TwitterAuthenticator():
	def authenticatetwitterapp(self):
		authenticate = OAuthHandler(tc.consumerkey, tc.consumersecret)
		authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
		return authenticate

#Twitter streamer
class TwitterStreamer():
	'''
	Class for streaming and processing live tweets
	'''
	def __init__(self):
		self.TwitterAuthenticator = TwitterAuthenticator()
	def streamtweets(self, fetchedtweetsfilename, hashtaglist):
		#Twitter Authentication and the connection to the Twitter Streaming API
		listener = TwitterListener(fetchedtweetsfilename)
		authenticate = self.TwitterAuthenticator.authenticatetwitterapp()
		stream = Stream(authenticate, listener)
		#Filter twitter stream to capture data by the keywords in hashtaglist
		stream.filter(track=hashtaglist)

#Twitter stream listener
class TwitterListener(StreamListener):
	'''
	Basic listener class printing received tweets to TwitterListener
	'''
	def __init__(self, fetchedtweetsfilename):
		self.fetchedtweetsfilename = fetchedtweetsfilename
	def on_data(self, data):
		try:
			print(data)
			with open(self.fetchedtweetsfilename, "a") as ftf:
				ftf.write(data)
			return True
		except BaseException as error:
			print("Error on data: %s" %str(error)) 
		# print(data)
		return True
	def on_error(self, status):
		#Return False on_data method in case rate limit occurs; i.e., getting too much Twitter tweets
		if status == 420:
			return False
		print(status)

#
class TweetAnalyzer():
	'''
	Functionality for analyzing and categorizing content from tweets.
	'''
	def cleantweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
	def analyzesentiment(self, tweet):
		analysis = TextBlob(self.cleantweet(tweet))
		if analysis.sentiment.polarity > 0:
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1

	def tweetstodataframe(self, tweets):
		dataframevariable = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=["tweets"])
		dataframevariable["id"] = np.array([tweet.id for tweet in tweets])
		dataframevariable["len"] = np.array([len(tweet.text) for tweet in tweets])
		dataframevariable["date"] = np.array([tweet.created_at for tweet in tweets])
		dataframevariable["source"] = np.array([tweet.source for tweet in tweets])
		dataframevariable["likes"] = np.array([tweet.favorite_count for tweet in tweets])
		dataframevariable["retweets"] = np.array([tweet.retweet_count for tweet in tweets])
		return dataframevariable

if __name__ == "__main__":
	twitterclientobject2 = TwitterClient()
	tweetanalyzerobject = TweetAnalyzer()
	api = twitterclientobject2.gettwitterclientapi()
	tweetsvariable = api.user_timeline(screen_name = "realDonaldTrump", count=200)
	#print(tweetsvariable)
	dataframevariable = tweetanalyzerobject.tweetstodataframe(tweetsvariable)
	print(dataframevariable.head(15))
	'''
	                                               tweets                   id  \
	0   A great evening last night in Kentucky and Mis...  1192229368057085952   
	1   RT @RepDougCollins: Here’s Ambassador Taylor t...  1192221874752651264   
	2   RT @realDonaldTrump: Stock Markets (all three)...  1192211806665629696   
	3   Thanks to many of you here today, my Administr...  1192198480267218945   
	4   ....Also talked about their Border with Syria,...  1192173803171983362   
	5   Just had a very good call with President @RTEr...  1192173801502588928   
	6   Just had a meeting with top representatives fr...  1192157303753125888   
	7   Stock Markets (all three) hit another ALL TIME...  1192071660494565377   
	8   Thank you to Kurt Volker, U.S. Envoy to Ukrain...  1192068562682368002   
	9   “Based on the things I’ve seen, the Democrats ...  1192065660593029120   
	10  Based on the Kentucky results, Mitch McConnell...  1192062007324938240   
	11  RT @GOPChairwoman: No one energizes our base l...  1191948025746337792   
	12          Great going Tate! https://t.co/ghtl3Zmj1z  1191947934734176257   
	13  Our big Kentucky Rally on Monday night had a m...  1191947091461001216   
	14  A lot of winning in Kentucky. Check out the nu...  1191942342879666178   

	    len                date              source   likes  retweets  
	0   140 2019-11-06 23:56:46  Twitter for iPhone   23474      6674  
	1   139 2019-11-06 23:27:00  Twitter for iPhone       0      4906  
	2   144 2019-11-06 22:46:59  Twitter for iPhone       0     25850  
	3   140 2019-11-06 21:54:02  Twitter for iPhone   42829     12319  
	4   140 2019-11-06 20:15:58  Twitter for iPhone   30949      7387  
	5   140 2019-11-06 20:15:58  Twitter for iPhone   46095     11923  
	6   140 2019-11-06 19:10:25  Twitter for iPhone   37927      9244  
	7   144 2019-11-06 13:30:06  Twitter for iPhone  131782     25850  
	8   140 2019-11-06 13:17:47  Twitter for iPhone   74627     19718  
	9   140 2019-11-06 13:06:15  Twitter for iPhone   56174     14047  
	10   96 2019-11-06 12:51:44  Twitter for iPhone   54142     11334  
	11  140 2019-11-06 05:18:49  Twitter for iPhone       0     13488  
	12   41 2019-11-06 05:18:27  Twitter for iPhone   41041      9588  
	13  140 2019-11-06 05:15:06  Twitter for iPhone   53190     12399  
	14   76 2019-11-06 04:56:14  Twitter for iPhone   34363      8216  
	'''
	print("\n")

	dataframevariable["sentiment"] = np.array([tweetanalyzerobject.analyzesentiment(tweet) for tweet in dataframevariable["tweets"]])
	print(dataframevariable.head(10))
	'''
	                                              tweets                   id  \
	0  A great evening last night in Kentucky and Mis...  1192229368057085952   
	1  RT @RepDougCollins: Here’s Ambassador Taylor t...  1192221874752651264   
	2  RT @realDonaldTrump: Stock Markets (all three)...  1192211806665629696   
	3  Thanks to many of you here today, my Administr...  1192198480267218945   
	4  ....Also talked about their Border with Syria,...  1192173803171983362   
	5  Just had a very good call with President @RTEr...  1192173801502588928   
	6  Just had a meeting with top representatives fr...  1192157303753125888   
	7  Stock Markets (all three) hit another ALL TIME...  1192071660494565377   
	8  Thank you to Kurt Volker, U.S. Envoy to Ukrain...  1192068562682368002   
	9  “Based on the things I’ve seen, the Democrats ...  1192065660593029120   

	   len                date              source   likes  retweets  sentiment  
	0  140 2019-11-06 23:56:46  Twitter for iPhone   23096      6573          1  
	1  139 2019-11-06 23:27:00  Twitter for iPhone       0      4846         -1  
	2  144 2019-11-06 22:46:59  Twitter for iPhone       0     25784          1  
	3  140 2019-11-06 21:54:02  Twitter for iPhone   42496     12239          1  
	4  140 2019-11-06 20:15:58  Twitter for iPhone   30823      7358          0  
	5  140 2019-11-06 20:15:58  Twitter for iPhone   45872     11869          1  
	6  140 2019-11-06 19:10:25  Twitter for iPhone   37807      9214          1  
	7  144 2019-11-06 13:30:06  Twitter for iPhone  131485     25784          1  
	8  140 2019-11-06 13:17:47  Twitter for iPhone   74513     19695          0  
	9  140 2019-11-06 13:06:15  Twitter for iPhone   56105     14037          1  
	'''
	print(type(dataframevariable.head(10))) #print <class 'pandas.core.frame.DataFrame'>
	print("\n")
	
	#Get average length tweets
	print(np.mean(dataframevariable["len"])) #print 121.44
	#Get the highest number of likes for most liked tweet
	print(np.max(dataframevariable["likes"])) #print 289386
	#Get the highest number of retweets for most retweeted tweet
	print(np.max(dataframevariable["retweets"])) #print 52901
	#Time series line chart likes
	timelikes = pd.Series(data=dataframevariable["likes"].values, index=dataframevariable["date"])
	timelikes.plot(figsize=(16,4), title="likes", color="r")
	plt.show()
	#Time series line chart retweets
	timeretweets = pd.Series(data=dataframevariable["retweets"].values, index=dataframevariable["date"])
	timeretweets.plot(figsize=(16,4), title="retweets", color="b")
	plt.show()
	#Time series line chart combine likes and retweets
	timelikes.plot(figsize=(16,4), label="likes", color="r", legend=True)
	timeretweets.plot(figsize=(16,4), label="retweets", color="b", legend=True)
	plt.show()

	print("\n")
	#print(dir(tweetsvariable[0]))
	'''
	['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getstate__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_json', 'author', 'contributors', 'coordinates', 'created_at', 'destroy', 'entities', 'favorite', 'favorite_count', 'favorited', 'geo', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'parse', 'parse_list', 'place', 'retweet', 'retweet_count', 'retweeted', 'retweeted_status', 'retweets', 'source', 'source_url', 'text', 'truncated', 'user']
	'''
	#print(tweetsvariable[0].retweet_count) #print 3012

	# hashtaglist = ["donald trump","hiliary clinton","barack obama","bernie sanders"]
	# fetchedtweetsfilename = "tweets.json"
	# gettweets = TwitterStreamer()
	# gettweets.streamtweets(fetchedtweetsfilename, hashtaglist)
	# twitterclientobject = TwitterClient("ININ61")
	# print(twitterclientobject.getusertimelinetweets(5))  #Instructor says the default to get the tweets is from the user's Twitter timeline

	# listener = TwitterListener()
	# authenticate = OAuthHandler(tc.consumerkey, tc.consumersecret)
	# authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
	# stream = Stream(authenticate, listener)
	# stream.filter(track=["donald trump","hiliary clinton","barack obama","bernie sanders"])