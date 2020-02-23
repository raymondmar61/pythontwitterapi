#tweepy.org
#Twitter API with Python_ Part 1 -- Streaming Live Tweets [720p].mp4  #RM:  delay these tutorial series
#Day 29_ Twitter API with Python [720p].mp4  #RM:  delay watching tutorial because its not tweepy module.
#Twitter API Tutorial For Beginners (Python) [720p]

import tweepy
import twitter_credentials as tc

#Create an api object.  Establish a connection with my developer information.  Store information in variable api.
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

#Find trends
trendsresults = api.trends_place(1)
print(trendsresults) #print [{'trends': [{'name': '#WilderFury2', 'url': 'http://twitter.com/search?q=%23WilderFury2', 'promoted_content': None, 'query': '%23WilderFury2', 'tweet_volume': 99792}, {'name': '#WeLoveYouJin', 'url': 'http://twitter.com/search?q=%23WeLoveYouJin', 'promoted_content': None, 'query': '%23WeLoveYouJin', 'tweet_volume': 56140}, {'name': 'Leafs', 'url': 'http://twitter.com/search?q=Leafs', 'promoted_content': None, 'query': 'Leafs', 'tweet_volume': 63464}, . . .
displaytrends = trendsresults[0]["trends"]
for eachtrends in displaytrends:
	print(eachtrends["name"]) #print #WilderFury2\n #WeLoveYouJin\n Leafs\n . . . 

