#YouTube MoreThanProgrammer
#Video Live Tweets with Python  Twitter Streaming API and Tweepy Library
#Streaming With Tweepy http://docs.tweepy.org/en/latest/streaming_how_to.html
import tweepy
import twitter_credentials as tc

#Create A StreamListener
class MaxListener(tweepy.StreamListener):
	def on_data(self, rawdata):
		self.processdata(rawdata)
		return True
	def processdata(self, rawdata):
		print(rawdata)
		'''
		{"created_at":"Thu Dec 19 03:04:53 +0000 2019","id":1207497000637231109,"id_str":"1207497000637231109","text":"i want to listen to the beatles when it\u2019s 12 am on new year\u2019s day so then i can say the first thing i did in a new\u2026 https:\/\/t.co\/z20VFX4box","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1007724483615051776,"id_str":"1007724483615051776","name":"sarah","screen_name":"siegelbeatle","location":"nowhere land","url":null,"description":"i\u2019m more than obsessed with the beatles","translator_type":"none","protected":false,"verified":false,"followers_count":683,"friends_count":609,"listed_count":4,"favourites_count":20470,"statuses_count":2976,"created_at":"Fri Jun 15 20:40:14 +0000 2018","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1190676947443027968\/jN0gAiw6_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1190676947443027968\/jN0gAiw6_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1007724483615051776\/1576024922","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"i want to listen to the beatles when it\u2019s 12 am on new year\u2019s day so then i can say the first thing i did in a new decade was listen to my favorite artist","display_text_range":[0,154],"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/z20VFX4box","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1207497000637231109","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[116,139]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1576724693818"}
		'''
		print(type(rawdata)) #print <class 'str'>
		print(rawdata.find("\"text\""), rawdata.find("\"source\"")) #print 103 270
		print(rawdata[rawdata.find("\"text\""):rawdata.find("\"source\"")])
		'''
		"text":"i want to listen to the beatles when it\u2019s 12 am on new year\u2019s day so then i can say the first thing i did in a new\u2026 https:\/\/t.co\/z20VFX4box",
		RM:  i want to listen to the beatles when it’s 12 am on new year’s day so then i can say the first thing i did in a new decade was listen to my favorite artist  
		RM:  https://t.co//z20VFX4box or https://twitter.com/i/web/status/1207497000637231109
		'''
	def on_error(self, statuscode):
		if statuscode == 420:
		#returning False in on_error disconnects the stream
			return False

#Create A Stream
class MaxStream():
	def __init__(self, auth, listener):
		self.stream = tweepy.Stream(auth=auth, listener=listener)
	def start(self, keywordlist):
		self.stream.filter(track=keywordlist)

#Start The Stream
if __name__ == "__main__":
	listener = MaxListener()
	authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
	authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
	stream = MaxStream(authenticate, listener)
	#stream.start(["snow","rain"]) #keywords to stream or keywords to get tweets
	stream.start(["the beatles"]) #keywords to stream or keywords to get tweets
