#http://www.tweepy.org/
import tweepy
import twitter_credentials as tc
#When we invoke an API method most of the time returned back to us will be a Tweepy model class instance.

#Create an api object.  Establish a connection with my developer information.  api object talk to twitter, read data to Twitter, write data to Twitter.  Store information in variable api.
authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)

#Print recent tweets in your timeline
downloadtimelinetweets = api.home_timeline()
print(type(downloadtimelinetweets)) #print <class 'tweepy.models.ResultSet'>
tweetynumber = 1
for eachdownloadtimelinetweets in downloadtimelinetweets:
	print(tweetynumber, eachdownloadtimelinetweets.text)
	tweetynumber += 1
	'''
	1 Having trouble reaching climax? I got you 💋
	https://t.co/GLhixsimhj
	2 Did Clementine Barnabet, priestess of a strange sacrificial cult, bludgeon seven families to death with an ax?
	https://t.co/1mdtnfVMmj
	3 RT @Cleavon_MD: (1/6) Over the past 6 weeks in NYC, I've treated 100s of patients with #COVID. My #PPE kept me healthy😷

	If the government…
	'''

#Get the user's information
userinformation = api.get_user("ININ61")
print(type(userinformation)) #print <class 'tweepy.models.User'>
print(userinformation)
'''
User(_api=<tweepy.api.API object at 0x7f88eefbe240>, _json={'id': 86863717, 'id_str': '86863717', 'name': 'Raymond Mar', 'screen_name': 'inin61', 'location': 'San Jose, CA', 'profile_location': None, 'description': "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", 'url': 'https://t.co/jXjuhIMFeG', 'entities': {'url': {'urls': [{'url': 'https://t.co/jXjuhIMFeG', 'expanded_url': 'https://www.innovateinfinitely.com', 'display_url': 'innovateinfinitely.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65 . . . 
'''
print(userinformation.name) #print Raymond Mar
print(userinformation.screen_name) #print inin61
print(userinformation.followers_count) #print 65
print(type(userinformation.friends())) #print <class 'tweepy.models.ResultSet'>
for eachfriend in userinformation.friends():
	print(eachfriend.screen_name) #print arstechnica
	print(eachfriend.location) #print NYC - Boston - Chicago - SF
	'''
	User(_api=<tweepy.api.API object at 0x7fb4e3ae41d0>, _json={'id': 717313, 'id_str': '717313', 'name': 'Ars Technica', 'screen_name': 'arstechnica', 'location': 'NYC - Boston - Chicago - SF' . . .
	'''

#Cursor Object
for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
	print(tweet.text)
	'''
	@masonasons @BrailleScreen @destructatron04 And I suppose there are also still other options. I'm not sure how up t… https://t.co/ICBEjpzNWx
	RT @tweet_bot_1729: Whole every miles as tiled at seven or.#python #bot #programming #random #code #tweepy #API https://t.co/Eb3cGBTgTI
	Een bloemetje voor het slapengaan. Trusten Tweepy's! 😴 https://t.co/0ZLblF7y0N
	Learn To Build Twitter Bot With Tweepy
	Learn About Access Token, Keys And It's Usage
	Deploy Bot Online And Run 24/7… https://t.co/SRbazSZ4mb
	@HermaineM If you ever hit a follow limit here is a plug 

	https://t.co/d4G2dWnMMM
	@Lebohang20S Have a lovely night sleep my tweepy..😍
	@PaulDashJohn @MYANC @PresJGZuma Who used Tweepy to deploy you?
	@jessphillips @RishiSunak
	Test tweet from Tweepy Python
	Sending my first tweet via Tweepy!
	'''
#print all my friends
for eachfriend in tweepy.Cursor(api.friends).items():
	print(eachfriend.name) #print Wizarding World\n BrianBanmiller\n CHP - Alerts\n . . .
#print 10 statuses in user's home timeline
for eachstatus in tweepy.Cursor(api.home_timeline).items(10):
	#print(eachstatus)
	print(eachstatus.text) #This movie was SO GOOD