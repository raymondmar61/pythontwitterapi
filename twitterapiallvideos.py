#tweepy.org
#Twitter API with Python_ Part 1 -- Streaming Live Tweets [720p].mp4  #RM:  delay these tutorial series
#Day 29_ Twitter API with Python [720p].mp4  #RM:  delay watching tutorial because its not tweepy module.
#Twitter API Tutorial For Beginners (Python) [720p]
#Python Tweepy library (Twitter API) - part 1 [720p] YouTube Kostadin Ristovski, Python Tweepy library (Twitter API) - part 2 [720p] YouTube Kostadin Ristovski
#How to use the Twitter API v1.1 with Python to stream tweets [720p] sentdex
#Saving Tweets How to use the Twitter API v1.1 with Python to stream tweets sentdex
#Cleaning up Tweets How to use the Twitter API v1.1 with Python to stream tweets sentdex
#How To Post A Live Tweet With Python Using Twitter API [720p]
#Live Tweets with Python  Twitter Streaming API and Tweepy Library
#Python Programming - Creating A Twitter Retweet Bot w_ Tweepy [720p] YouTuber Tutorial Spot
#How To Create A Twitter Bot With Python John G Fisher
#How To Create A Twitter Bot With Python _ Build a Startup #4 [720p]

import tweepy
import twitter_credentials as tc

#Create an api object.  Establish a connection with my developer information.  api object talk to twitter, read data to Twitter, write data to Twitter.  Store information in variable api.
authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)

#https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline
public_tweets = api.home_timeline(count=1)
counter = 1
for tweet in public_tweets:
	print(counter, tweet.text,end="*end*\n")
	counter +=1

#Post a tweet
mytweet="If someone placed a cup of tea next to your bedroom door, then he or she is saying thank you.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
if len(mytweet)<=280:
	api.update_status(mytweet)
else:
	print("The number of characters is greater than 280.  Tweet not posted.")

#Create a function to create api authentication.  Post a tweet.
def APIobjectfunction():
	try:
		authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
		authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
		return authenticate
	except Exception as e:
		return None
oauth = APIobjectfunction()
api = tweepy.API(oauth)
api.update_status("A treat or a tweet")

#Get a user's Twitter information
twitteruser = "inin61"
userinformation = api.get_user(twitteruser)
print(userinformation)
'''
User(_api=<tweepy.api.API object at 0x7fcb21a7b0f0>, _json={'id': 86863717, 'id_str': '86863717', 'name': 'Raymond Mar', 'screen_name': 'inin61', 'location': 'San Jose, CA', 'profile_location': None, 'description': "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", 'url': 'https://t.co/jXjuhIMFeG', 'entities': {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65, 'friends_count': 49, 'listed_count': 9, 'created_at': 'Mon Nov 02 03:27:17 +0000 2009', 'favourites_count': 478, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 6341, 'lang': None, 'status': {'created_at': 'Sun Feb 23 01:29:32 +0000 2020', 'id': 1231390604447244288, 'id_str': '1231390604447244288', 'text': 'If someone placed a cup of tea next to your bedroom door, then he or she is saying thank you.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="https://www.innovateinfinitely.com" rel="nofollow">ININ61</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/86863717/1489186606', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none', 'suspended': False, 'needs_phone_verification': False}, id=86863717, id_str='86863717', name='Raymond Mar', screen_name='inin61', location='San Jose, CA', profile_location=None, description="Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", url='https://t.co/jXjuhIMFeG', entities={'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=65, friends_count=49, listed_count=9, created_at=datetime.datetime(2009, 11, 2, 3, 27, 17), favourites_count=478, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=6341, lang=None, status=Status(_api=<tweepy.api.API object at 0x7fcb21a7b0f0>, _json={'created_at': 'Sun Feb 23 01:29:32 +0000 2020', 'id': 1231390604447244288, 'id_str': '1231390604447244288', 'text': 'If someone placed a cup of tea next to your bedroom door, then he or she is saying thank you.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="https://www.innovateinfinitely.com" rel="nofollow">ININ61</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 2, 23, 1, 29, 32), id=1231390604447244288, id_str='1231390604447244288', text='If someone placed a cup of tea next to your bedroom door, then he or she is saying thank you.', truncated=False, entities={'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, source='ININ61', source_url='https://www.innovateinfinitely.com', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, lang='en'), contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/86863717/1489186606', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none', suspended=False, needs_phone_verification=False)
'''
print(userinformation.description)  #print Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring
print("For icons in the description which is a code "+userinformation.description.encode("unicode-escape").decode("utf-8"))  #print For icons in the description which is a code Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring
print(userinformation._json)
'''
{'id': 86863717, 'id_str': '86863717', 'name': 'Raymond Mar', 'screen_name': 'inin61', 'location': 'San Jose, CA', 'profile_location': None, 'description': "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", 'url': 'https://t.co/jXjuhIMFeG', 'entities': {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65, 'friends_count': 49, 'listed_count': 9, 'created_at': 'Mon Nov 02 03:27:17 +0000 2009', 'favourites_count': 478, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 6341, 'lang': None, 'status': {'created_at': 'Sun Feb 23 01:29:32 +0000 2020', 'id': 1231390604447244288, 'id_str': '1231390604447244288', 'text': 'If someone placed a cup of tea next to your bedroom door, then he or she is saying thank you.', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="https://www.innovateinfinitely.com" rel="nofollow">ININ61</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/86863717/1489186606', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none', 'suspended': False, 'needs_phone_verification': False}
'''
print(userinformation._json["id"]) #print 86863717
print(userinformation._json["entities"]) #print {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}
print(userinformation._json["entities"]["url"]) #print {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}
print(userinformation._json["entities"]["url"]["urls"]) #print [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]
print(type(userinformation._json["entities"]["url"]["urls"])) #print <class 'list'>
print(userinformation._json["entities"]["url"]["urls"][0]) #print {'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}
print(userinformation._json["entities"]["url"]["urls"][0]["expanded_url"]) #print https://www.innovateinfinitely.com
geturl = userinformation._json["entities"]["url"]["urls"]
print(type(geturl)) #print <class 'list'>
for eachgeturl in geturl:
	print(eachgeturl) #print {'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}
for eachgeturl in geturl:
	for x,y in eachgeturl.items():
		print(x,y)
		'''
		url https://t.co/jXjuhIMFeG
		expanded_url https://www.innovateinfinitely.com
		display_url innovateinfinitely.com
		indices [0, 23]
		'''

#Find tweets with a keyword
#findtweetskeyword = "#fullmetalalchemist"
findtweetskeyword = "harry potter"
findtweets = api.search(q=findtweetskeyword, lang="en", result_type="recent", count=10)
number = 1
for eachfindtweets in findtweets:
	eachfindtweets.text = eachfindtweets.text
	eachfindtweets.user.name = eachfindtweets.user.name
	#eachfindtweets.text = eachfindtweets.text.encode("unicode-escape").decode("utf-8")
	#eachfindtweets.user.name = eachfindtweets.user.name.encode("unicode-escape").decode("utf-8")
	print(number,eachfindtweets.user.name+":"+eachfindtweets.text,end="\n\n")	
	number += 1
	'''
	1 lil tourist:I’m smoking wax in my room feeling like Harry Potter finna take off to the hood on a broom

	2 self-portrait aloty!:@miniyerms harry potter teas

	...

	9 ✌🏻😳eve’s lerones pet😳✌🏻:i don’t have a dick either and he thought i was a harry potter twink so

	10 justintupper:@RealJamesWoods Harry Potter?
	'''

#Find trends
trendsresults = api.trends_place(1)
print(trendsresults) #print [{'trends': [{'name': '#WilderFury2', 'url': 'http://twitter.com/search?q=%23WilderFury2', 'promoted_content': None, 'query': '%23WilderFury2', 'tweet_volume': 99792}, {'name': '#WeLoveYouJin', 'url': 'http://twitter.com/search?q=%23WeLoveYouJin', 'promoted_content': None, 'query': '%23WeLoveYouJin', 'tweet_volume': 56140}, {'name': 'Leafs', 'url': 'http://twitter.com/search?q=Leafs', 'promoted_content': None, 'query': 'Leafs', 'tweet_volume': 63464}, . . .
displaytrends = trendsresults[0]["trends"]
for eachtrends in displaytrends:
	print(eachtrends["name"]) #print #WilderFury2\n #WeLoveYouJin\n Leafs\n . . .

#Display tweets text only based on keyword or keywords
keywords = ["Python","C++"]
followers = 200
following = 200
numberoftweets = 500
for tweet in tweepy.Cursor(api.search, q=keywords, lang="en", result_type="recent").items(5):
	#print(tweet.text.encode("unicode-escape").decode("utf-8"),end="\n\n")
	#print(tweet.text,end="\n\n")
	'''
	@buabaj_ Guess that shows where my interest is as far as programming languages go (except maybe the Pascal part) fo… https://t.co/T8Xr9h2x8a

	@buabaj_ Pascal, in less than 7 years jumped to the top, I guess that is testament to how good it really was in its… https://t.co/i6AWtcfnu0

	Trying some animation tools in matplotlib 🤩. Any recommendations for complementary python modules? https://t.co/B2Ug0mBVvp

	@iJacksonIsaac Well, first off, thanks a lot for the information.

	Also, I know that this will be a massive project… https://t.co/OkqQJA9NmP

	@WellPaidGeek Commodore 64 BASIC and assembler. Then C, C++, Ada, Clipper, Java (one of the first in Europe), and later Python, Perl...
	'''
	if tweet.user.followers_count > followers and tweet.user.friends_count > following and tweet.user.statuses_count > numberoftweets:
		print(tweet.text,end="\n\n")
		'''
		RT @jonhoo: Hi friends! I recently gave a talk aimed at companies that are considering adding @rustlang to their tech stack. In it, I prese…

		RT @contempediacom: #development Free Discounts
		Advanced #C Programming Course =&gt; https://t.co/flF5BhuqNM

		#100DaysOfCode #udemy #coupons #…
		'''

#Display tweets text only based on keyword no retweets
keyword = ["The Beatles","McCartney"]
for tweet in tweepy.Cursor(api.search, q=keyword, lang="en", result_type="recent").items(5):
	if tweet.text.startswith("RT @") == True:
		pass
	else:
		print(tweet.text,end="\n\n")
	'''
	i was just trying to remember all the names of the members of the beatles and tell me why i said ringo starr, john… https://t.co/Ene6HXo0M2
	'''

#Get tweets from user with user's tweet keyword
#RM:  I can't get the code to work with multiple twitterid.  If multiple twitterid, then multiple twitterid must tweet the same tweet.
#keyword is case sensitive
twitterid = "elonmusk"
keyword = "coronavirus"
tweetswithkeyword = []
for eachtweet in tweepy.Cursor(api.user_timeline, screen_name=twitterid, tweet_mode="extended").items(50):
	#eachtweet.full_text = eachtweet.full_text.encode("unicode-escape").decode("utf-8")
	if keyword in eachtweet.full_text:
		print(eachtweet.full_text) #print The coronavirus panic is dumb
		tweetswithkeyword.append(eachtweet.full_text)
print(tweetswithkeyword) #print ['The coronavirus panic is dumb']

#Textblob.  Check polarity -1 to +1 negative tweet to positive tweet sentiment.
from textblob import TextBlob
twitterid = "cnnbrk"
keywordiscasesensitive = "Trump"
sentimentnumber = 0.3
positivesentiment = []
negativesentiment = []
neutralsentiment = []
for eachtweet in tweepy.Cursor(api.user_timeline, screen_name=twitterid, tweet_mode="extended").items(50):
	#eachtweet.full_text = eachtweet.full_text.encode("unicode-escape").decode("utf-8")
	if keywordiscasesensitive in eachtweet.full_text:
		if TextBlob(eachtweet.full_text).sentiment.polarity > +sentimentnumber:
			positivesentiment.append(eachtweet.full_text)
		elif TextBlob(eachtweet.full_text).sentiment.polarity < -sentimentnumber:
			negativesentiment.append(eachtweet.full_text)
		else:
			neutralsentiment.append(eachtweet.full_text)
print("POSITIVE",positivesentiment) #print POSITIVE []
print("\n")
print("NEGATIVE",negativesentiment) #print NEGATIVE []
print("\n")
print("NEUTRAL",neutralsentiment)
'''
NEUTRAL ['RT @CNNPolitics: BREAKING: President Trump replaces Mick Mulvaney with Rep. Mark Meadows as chief of staff https://t.co/HjpbzaqB0b https://…', 'President Trump will visit the Centers for Disease Control and Prevention in Atlanta, after earlier reports by officials that the visit was cancelled https://t.co/p6EXWhfnsS https://t.co/qugUmF9Jx8']
'''

#Donwload Tweets to a csv file based on a keyword and English Language
import time
keyword = ["Harry Potter"]
class listener(tweepy.StreamListener):
	try:
		def on_data(self, data):
			print(data)
			print("\n")
			tweet = data.split(",\"text\":\"")[1].split("\",\"source")[0]
			print(tweet)
			print("\n")
			#print(type(data)) #print <class 'str'>
			savetweet = str(time.time())+"::"+tweet
			savefile = open("twitterstreams.csv","a")
			savefile.write(savetweet)
			savefile.write("\n")
			savefile.close()
	except BaseException as message:
		print("Failed on_data likely internet connection interrupted",str(message))
		time.sleep(5)
	def on_error(self, status):
		print(status)
twitterstream = tweepy.Stream(authenticate, listener())
twitterstream.filter(track=keyword, languages=["en"])  #English only.  Source:  https://stackoverflow.com/questions/26890605/filter-twitter-feeds-only-by-language
'''
{"created_at":"Sun Mar 15 01:31:19 +0000 2020","id":1239001197312454656,"id_str":"1239001197312454656","text":"RT @comoelesestao: Daniel Radcliffe  (Harry Potter)\n\n12 anos \/\/ 30 anos https:\/\/t.co\/epPWNy677X","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1206661476351696896,"id_str":"1206661476351696896","name":"\ud835\udc78\ud835\udc96\ud835\udc86\ud835\udc8e \ud835\udc8e\ud835\udc86 \ud835\udc85\ud835\udc86\ud835\udc93\ud835\udc82\u2077 \u2661","screen_name":"Sugaryyblue","location":null,"url":null,"description":"\ud835\udc78\ud835\udc96\ud835\udc86\ud835\udc8e \ud835\udc8e\ud835\udc86 \ud835\udc85\ud835\udc86\ud835\udc93\ud835\udc82 \n\ud835\udc03\ud835\udc22\ud835\udc1c\ud835\udc1a\ud835\udc2c&\ud835\udc02\ud835\udc2e\ud835\udc2b\ud835\udc22\ud835\udc28\ud835\udc2c\ud835\udc22\ud835\udc1d\ud835\udc1a\ud835\udc1d\ud835\udc1e\ud835\udc2c \n\ud835\udd6d\ud835\udd9a\ud835\udd99 \ud835\udd9c\ud835\udd8d\ud835\udd86\ud835\udd99 \ud835\udd8e\ud835\udd8b \ud835\udd99\ud835\udd8d\ud835\udd86\ud835\udd99 \ud835\udd92\ud835\udd94\ud835\udd92\ud835\udd8a\ud835\udd93\ud835\udd99'\ud835\udd98 \ud835\udd97\ud835\udd8e\ud835\udd8c\ud835\udd8d\ud835\udd99 \ud835\udd93\ud835\udd94\ud835\udd9c\ud83d\udc99","translator_type":"none","protected":false,"verified":false,"followers_count":10,"friends_count":270,"listed_count":0,"favourites_count":21,"statuses_count":545,"created_at":"Mon Dec 16 19:44:59 +0000 2019","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1220413575082258433\/YvGD5Xa4_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1220413575082258433\/YvGD5Xa4_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1206661476351696896\/1579804245","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Sat Mar 14 14:20:25 +0000 2020","id":1238832360990351360,"id_str":"1238832360990351360","text":"Daniel Radcliffe  (Harry Potter)\n\n12 anos \/\/ 30 anos https:\/\/t.co\/epPWNy677X","display_text_range":[0,52],"source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1236377679366098946,"id_str":"1236377679366098946","name":"como os famosos eram\/est\u00e3o?","screen_name":"comoelesestao","location":"Hollywood","url":null,"description":"como os famosos eram anos atr\u00e1s?                                  \ne os de anos atr\u00e1s, como est\u00e3o hoje em dia?                             \nsugest\u00f5es via DM \ud83d\udce9","translator_type":"none","protected":false,"verified":false,"followers_count":68349,"friends_count":1,"listed_count":7,"favourites_count":76,"statuses_count":37,"created_at":"Sat Mar 07 19:46:32 +0000 2020","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1236634896497598469\/imwAFIsS_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1236634896497598469\/imwAFIsS_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1236377679366098946\/1583760408","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":65,"reply_count":43,"retweet_count":243,"favorite_count":5512,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[],"media":[{"id":1238832350353592321,"id_str":"1238832350353592321","indices":[53,76],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":480,"h":480,"resize":"fit"},"medium":{"w":480,"h":480,"resize":"fit"},"large":{"w":480,"h":480,"resize":"fit"}}}]},"extended_entities":{"media":[{"id":1238832350353592321,"id_str":"1238832350353592321","indices":[53,76],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":480,"h":480,"resize":"fit"},"medium":{"w":480,"h":480,"resize":"fit"},"large":{"w":480,"h":480,"resize":"fit"}}},{"id":1238832352832434176,"id_str":"1238832352832434176","indices":[53,76],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dhbWsAA2Day.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dhbWsAA2Day.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1024,"h":1280,"resize":"fit"},"medium":{"w":960,"h":1200,"resize":"fit"},"small":{"w":544,"h":680,"resize":"fit"}}}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"comoelesestao","name":"como os famosos eram\/est\u00e3o?","id":1236377679366098946,"id_str":"1236377679366098946","indices":[3,17]}],"symbols":[],"media":[{"id":1238832350353592321,"id_str":"1238832350353592321","indices":[72,95],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":480,"h":480,"resize":"fit"},"medium":{"w":480,"h":480,"resize":"fit"},"large":{"w":480,"h":480,"resize":"fit"}},"source_status_id":1238832360990351360,"source_status_id_str":"1238832360990351360","source_user_id":1236377679366098946,"source_user_id_str":"1236377679366098946"}]},"extended_entities":{"media":[{"id":1238832350353592321,"id_str":"1238832350353592321","indices":[72,95],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dYMWkAEcrzV.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":480,"h":480,"resize":"fit"},"medium":{"w":480,"h":480,"resize":"fit"},"large":{"w":480,"h":480,"resize":"fit"}},"source_status_id":1238832360990351360,"source_status_id_str":"1238832360990351360","source_user_id":1236377679366098946,"source_user_id_str":"1236377679366098946"},{"id":1238832352832434176,"id_str":"1238832352832434176","indices":[72,95],"media_url":"http:\/\/pbs.twimg.com\/media\/ETE3dhbWsAA2Day.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/ETE3dhbWsAA2Day.jpg","url":"https:\/\/t.co\/epPWNy677X","display_url":"pic.twitter.com\/epPWNy677X","expanded_url":"https:\/\/twitter.com\/comoelesestao\/status\/1238832360990351360\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":1024,"h":1280,"resize":"fit"},"medium":{"w":960,"h":1200,"resize":"fit"},"small":{"w":544,"h":680,"resize":"fit"}},"source_status_id":1238832360990351360,"source_status_id_str":"1238832360990351360","source_user_id":1236377679366098946,"source_user_id_str":"1236377679366098946"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1584235879625"}

RT @comoelesestao: Daniel Radcliffe  (Harry Potter)\n\n12 anos \/\/ 30 anos https:\/\/t.co\/epPWNy677X
'''

#Stream tweets based on keywords
#Create a StreamListener
class ININ61StreamListener(tweepy.StreamListener):
	def on_data(self, raw_data):
		self.process_data(raw_data)
		return True
	def process_data(self, raw_data):
		print(raw_data)
	def on_error(self, status_code):
		#Clients exceed limited number of attempts to connect receives 420 error
		if status_code == 420:
			#return False in on_data disconnects the stream
			return False
#Create a Stream
class ININ61Stream():
	def __init__(self, auth, listener):
		self.stream = tweepy.Stream(auth=auth, listener=listener)
	def start(self, keywordlist):
		self.stream.filter(track=keywordlist)
#Start the Stream Main Function
if __name__ == "__main__":
	listener = ININ61StreamListener()
	#Create an api object.  Establish a connection with my developer information.  Store information in variable api.
	authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
	authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
	stream = ININ61Stream(authenticate, listener)
	stream.start(["rain","snow"])  #returns tweet objects
	'''
	{"created_at":"Sun Mar 22 02:29:30 +0000 2020","id":1241552554367938561,"id_str":"1241552554367938561","text":"RT @mmmkjooo: CDTV\u30e9\u30a4\u30d6\uff01\u30e9\u30a4\u30d6\uff01\u306e\u62ab\u9732\u6f14\u76ee\nImitation Rain\u306e\u30d5\u30eb\u5730\u4e0a\u6ce2\u62ab\u9732\u3082\u6700\u9ad8\u3060\u3057Telephone\u304bNEW WORLD\u3082CD\u624b\u306b\u53d6\u308b\u30ad\u30c3\u30ab\u30b1\u306b\u306a\u308b\u3068\u601d\u3046\n\u3067\u3082\u79c1\u306fJAPONICA STYLE\u59cb\u307e\u308a\u306eJr.\u6642\u4ee3\u30aa\u30ea\u66f2\u3068Imitation Ra\u2026","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1216335589751934982,"id_str":"1216335589751934982","name":"\u3061\u3083\u3061\u3083vote","screen_name":"st_vote122","location":null,"url":null,"description":"SixTONES\u3092\u5fdc\u63f4\u3059\u308b\u305f\u3081\u306b\u4f5c\u308a\u307e\u3057\u305f\ud83d\udc8evote\u57a2\/\u30d5\u30a9\u30ed\u30fc&\u7121\u8a00RT\u5931\u793c\u3057\u307e\u3059\ud83e\udd81\ud83e\udd87\ud83e\udd94\ud83e\udd93\ud83e\udd85\ud83d\udc3b \u30b7\u30e3\u30c9\u30d0\u30f3\u2192 https:\/\/shadowban.eu\/","translator_type":"none","protected":false,"verified":false,"followers_count":379,"friends_count":404,"listed_count":3,"favourites_count":243,"statuses_count":8748,"created_at":"Sun Jan 12 12:26:26 +0000 2020","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1216335688930455552\/8IG0Y9ZT_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1216335688930455552\/8IG0Y9ZT_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1216335589751934982\/1584779521","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Sat Mar 21 16:45:33 +0000 2020","id":1241405598521913344,"id_str":"1241405598521913344","text":"CDTV\u30e9\u30a4\u30d6\uff01\u30e9\u30a4\u30d6\uff01\u306e\u62ab\u9732\u6f14\u76ee\nImitation Rain\u306e\u30d5\u30eb\u5730\u4e0a\u6ce2\u62ab\u9732\u3082\u6700\u9ad8\u3060\u3057Telephone\u304bNEW WORLD\u3082CD\u624b\u306b\u53d6\u308b\u30ad\u30c3\u30ab\u30b1\u306b\u306a\u308b\u3068\u601d\u3046\n\u3067\u3082\u79c1\u306fJAPONICA STYLE\u59cb\u307e\u308a\u306eJr.\u6642\u4ee3\u30aa\u30ea\u66f2\u3068Im\u2026 https:\/\/t.co\/72fS8focmt","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2180041292,"id_str":"2180041292","name":"pino.vote","screen_name":"mmmkjooo","location":null,"url":null,"description":"SixTONES\u3092\u611b\u3067\u308b\u3060\u3051\u306evote\u57a2\ud83d\udc8ert\u3060\u3051\u3067vote\u57a2\u3055\u3093\u304a\u8fce\u3048\u306b\u3042\u304c\u308a\u307e\u3059\ud83d\ude0f(\u7121\u8a00\u30d5\u30a9\u30ed\u30fc\u3059\u3044\u307e\u305b\u3093\ud83d\ude47\u200d\u2640\ufe0f)\u81ea\u30c4\u30a4\u306f\u3044\u3044\u306d\u6b04","translator_type":"none","protected":false,"verified":false,"followers_count":146,"friends_count":216,"listed_count":1,"favourites_count":736,"statuses_count":1391,"created_at":"Thu Nov 07 12:52:04 +0000 2013","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1221602931306221569\/CLnqrH8P_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1221602931306221569\/CLnqrH8P_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2180041292\/1580133913","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"CDTV\u30e9\u30a4\u30d6\uff01\u30e9\u30a4\u30d6\uff01\u306e\u62ab\u9732\u6f14\u76ee\nImitation Rain\u306e\u30d5\u30eb\u5730\u4e0a\u6ce2\u62ab\u9732\u3082\u6700\u9ad8\u3060\u3057Telephone\u304bNEW WORLD\u3082CD\u624b\u306b\u53d6\u308b\u30ad\u30c3\u30ab\u30b1\u306b\u306a\u308b\u3068\u601d\u3046\n\u3067\u3082\u79c1\u306fJAPONICA STYLE\u59cb\u307e\u308a\u306eJr.\u6642\u4ee3\u30aa\u30ea\u66f2\u3068Imitation Rain\u6df7\u305c\u305f\u30e1\u30c9\u30ec\u30fc\u3067\u7206\u30a4\u30b1\u30ae\u30e3\u30c3\u30d7SixTONES\u304c\u898b\u305f\u3044\uff01\n\u3053\u308c\u540c\u4e00\u30b0\u30eb\u30fc\u30d7\uff01\uff1f\u3063\u3066\u306a\u308b\u4e16\u9593\u304c\u898b\u305f\u3044\uff01\uff01","display_text_range":[0,178],"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":0,"reply_count":0,"retweet_count":50,"favorite_count":8,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/72fS8focmt","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1241405598521913344","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"ja"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"mmmkjooo","name":"pino.vote","id":2180041292,"id_str":"2180041292","indices":[3,12]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"ja","timestamp_ms":"1584844170549"}
	'''

#retweet bot
user = api.me()
print(user.name) #print Raymond Mar
def main():
	searchcriteria = ("#mysongoftheday","everything u r")
	#searchcriteria = ("harry potter","chamber of secrets")
	#searchcriteria = ("paul mccartney","beatles","hey jude")
	#limit retweets
	numberoftweets = 5
	for tweet in tweepy.Cursor(api.search, searchcriteria).items(numberoftweets):
		#prevent errors such as already retweeted the tweet
		try:
			tweet.retweet()
			print("Tweet retweeted successful")
		except tweepy.TweepError as error:
			print(error.reason)
		except StopIteration:
			break
main()

#Twitter retrieve all a Twitter user's tweet mentions
mentionsquickintroduction = api.mentions_timeline()
print(type(mentionsquickintroduction)) #print <class 'tweepy.models.ResultSet'> #RM:  instructor tweepy.models.ResultSet searched on Google
print(type(mentionsquickintroduction[0])) #print <class 'tweepy.models.Status'> #RM:  instructor tweepy.models.Status searched on Google
print(mentionsquickintroduction[0].__dict__) #converts an object to a dictionary
print(mentionsquickintroduction[0].__dict__.keys()) #The attributes of the class
'''
dict_keys(['_api', '_json', 'created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'source', 'source_url', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'author', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'lang'])
'''
print(mentionsquickintroduction[0].text) #print @inin61 @scaloy Many healthy people age 20-29, without any #COVID19 symptoms, have the #coronavirus and are contagi… https://t.co/4azHIamkWX
print(mentionsquickintroduction[0].text.lower()) #print @inin61 @scaloy many healthy people age 20-29, without any #covid19 symptoms, have the #coronavirus and are contagi… https://t.co/4azhiamkwx
print("\n")
#for loop retrieve Twitter user's tweet mentions
mentions = api.mentions_timeline()
for mention in mentions:
	print(str(mention.id) + " - " + mention.text)
	'''
	1246591721187602432 - @inin61 #helloworldtest
	1239441256465358849 - @inin61 @scaloy Many healthy people age 20-29, without any #COVID19 symptoms, have the #coronavirus and are contagi… https://t.co/4azHIamkWX
	1239417925464805376 - @inin61 just to be safe, i guess
	1237643262581600256 - @inin61 I’ve heard it floated around for a while. Figured I’d give it a shot in lieu of going to SDCC this year.
	...
	'''
	if "#helloworldtest" in mention.text.lower():
		print("found #helloworldtest")
print("\n")
#save the last tweet mention id number to the text file.  The last tweet mention id number is excluded when retrieving the newest tweet mention id
filename = "lasttweetmentionidtext.txt"
def retrievelastseenid(filename):
	filenameread = open(filename,"r")
	lasttweetmentionid = int(filenameread.read().strip())
	filenameread.close()
	return lasttweetmentionid
def updatelastseenid(lasttweetmentionid, filename):
	filenamewrite = open(filename,"w")
	filenamewrite.write(str(lasttweetmentionid))
	filenamewrite.close()
	return
lasttweetmentionid = retrievelastseenid(filename)
displaymentions = api.mentions_timeline(since_id=lasttweetmentionid, tweet_mode="extended")
#reversed to loop older tweets first or loop from older tweets to newest tweets.  twitter id 1246591721187602432 @inin61 #helloworldtest tweeted 04/04/20 is not included.  tweets after 1246591721187602432 are printed.  To get the newest tweets mention, use twitter id 1239441256465358849 on lasttweetmentionidtext.txt file
for eachdisplaymentions in reversed(displaymentions):
	print(str(eachdisplaymentions.id) + " - " + eachdisplaymentions.full_text) #print 1246606049534038016 - @inin61 ignoretweet abcdefghijklmnopqrstuvwxyz1234567890 .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 AAAAAAAAAAAAAAAAAA
	lasttweetmentionid = eachdisplaymentions.id	
	#call function to save newest tweet mention id to filename
	updatelastseenid(lasttweetmentionid, filename)
	if "#helloworldtest" in eachdisplaymentions.full_text.lower():
		print("found #helloworldtest again")
		api.update_status(status="@"+eachdisplaymentions.user.screen_name+" hello world test back to you", in_reply_to_status_id=eachdisplaymentions.id)
#create a function reply to tweets
def replytotweets():
	#save the last tweet mention id number to the text file.  The last tweet mention id number is excluded when retrieving the newest tweet mention id
	filename = "lasttweetmentionidtext.txt"
	def retrievelastseenid(filename):
		filenameread = open(filename,"r")
		lasttweetmentionid = int(filenameread.read().strip())
		filenameread.close()
		return lasttweetmentionid
	def updatelastseenid(lasttweetmentionid, filename):
		filenamewrite = open(filename,"w")
		filenamewrite.write(str(lasttweetmentionid))
		filenamewrite.close()
		return
	lasttweetmentionid = retrievelastseenid(filename)
	displaymentions = api.mentions_timeline(since_id=lasttweetmentionid, tweet_mode="extended")
	#reversed to loop older tweets first or loop from older tweets to newest tweets.  twitter id 1246591721187602432 @inin61 #helloworldtest tweeted 04/04/20 is not included.  tweets after 1246591721187602432 are printed.  To get the newest tweets mention, use twitter id 1239441256465358849 on lasttweetmentionidtext.txt file
	for eachdisplaymentions in reversed(displaymentions):
		print(str(eachdisplaymentions.id) + " - " + eachdisplaymentions.full_text) #print 1246606049534038016 - @inin61 ignoretweet abcdefghijklmnopqrstuvwxyz1234567890 .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 AAAAAAAAAAAAAAAAAA
		lasttweetmentionid = eachdisplaymentions.id	
		#call function to save newest tweet mention id to filename
		updatelastseenid(lasttweetmentionid, filename)
		if "#helloworldtest" in eachdisplaymentions.full_text.lower():
			print("found #helloworldtest again")
			api.update_status(status="@"+eachdisplaymentions.user.screen_name+" hello world test back to you", in_reply_to_status_id=eachdisplaymentions.id)
import time
while True:
	replytotweets()
	time.sleep(15) #Stop at 15 seconds and then start again