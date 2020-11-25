#http://www.tweepy.org/
import tweepy
import twitter_credentials as tc
#When we invoke an API method most of the time returned back to us will be a Tweepy model class instance.
import datetime
import pytz

#Create an api object.  Establish a connection with my developer information.  api object talk to twitter, read data to Twitter, write data to Twitter.  Store information in variable api.
authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)

def convertUTCTimeToLocalTime(twitterCreateDate):
    localTimeZone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
    twitterCreateDateStrpTime = datetime.datetime.strptime(twitterCreateDate, "%a %b %d %H:%M:%S %z %Y")
    localDateTime = twitterCreateDateStrpTime.replace(tzinfo=pytz.utc).astimezone(localTimeZone)
    dateLocal = datetime.datetime.strftime(localDateTime, "%m/%d/%Y")
    timeLocal = datetime.datetime.strftime(localDateTime, "%I:%M:%S %p")
    return dateLocal, timeLocal


#Print recent tweets in your timeline
favoritetweets = api.favorites(id="inin61", count=22)
for eachfavoritetweets in favoritetweets:
    #print(eachfavoritetweets._json)
    #print(type(eachfavoritetweets._json)) #print <class 'dict'>
    #print((eachfavoritetweets._json).items())
    '''
    dict_items([('created_at', 'Mon Nov 23 00:09:56 +0000 2020'), ('id', 1330664843955691521), ('id_str', '1330664843955691521'), ('text', 'We gave everything we had.\n\n#NeverSayDie | #MLSCupPlayoffs https://t.co/rjR17eQUve'), ('truncated', False), ('entities', {'hashtags': [{'text': 'NeverSayDie', 'indices': [28, 40]}, {'text': 'MLSCupPlayoffs', 'indices': [43, 58]}], 'symbols': [], 'user_mentions': [], 'urls': [], 'media': [{'id': 1330664717891764224, 'id_str': '1330664717891764224', 'indices': [59, 82], 'media_url': 'http://pbs.twimg.com/media/End4gsEVgAA600h.jpg', 'media_url_https': 'https://pbs.twimg.com/media/End4gsEVgAA600h.jpg', 'url': 'https://t.co/rjR17eQUve', 'display_url': 'pic.twitter.com/rjR17eQUve', 'expanded_url': 'https://twitter.com/SJEarthquakes/status/1330664843955691521/photo/1', 'type': 'photo', 'sizes': {'medium': {'w': 1200, 'h': 675, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'large': {'w': 1920, 'h': 1080, 'resize': 'fit'}, 'small': {'w': 680, 'h': 383, 'resize': 'fit'}}}]}), ('extended_entities', {'media': [{'id': 1330664717891764224, 'id_str': '1330664717891764224', 'indices': [59, 82], 'media_url': 'http://pbs.twimg.com/media/End4gsEVgAA600h.jpg', 'media_url_https': 'https://pbs.twimg.com/media/End4gsEVgAA600h.jpg', 'url': 'https://t.co/rjR17eQUve', 'display_url': 'pic.twitter.com/rjR17eQUve', 'expanded_url': 'https://twitter.com/SJEarthquakes/status/1330664843955691521/photo/1', 'type': 'photo', 'sizes': {'medium': {'w': 1200, 'h': 675, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'large': {'w': 1920, 'h': 1080, 'resize': 'fit'}, 'small': {'w': 680, 'h': 383, 'resize': 'fit'}}}]}), ('source', '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>'), ('in_reply_to_status_id', None), ('in_reply_to_status_id_str', None), ('in_reply_to_user_id', None), ('in_reply_to_user_id_str', None), ('in_reply_to_screen_name', None), ('user', {'id': 16303450, 'id_str': '16303450', 'name': 'San Jose Earthquakes', 'screen_name': 'SJEarthquakes', 'location': 'San Jose, CA', 'description': 'Official account of San Jose’s Major League Soccer club, two-time Supporters’ Shield winners and two-time MLS Cup Champs. #Quakes74 | #VamosSJ', 'url': 'https://t.co/9Wq2EQCRN5', 'entities': {'url': {'urls': [{'url': 'https://t.co/9Wq2EQCRN5', 'expanded_url': 'http://www.SJEarthquakes.com', 'display_url': 'SJEarthquakes.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 275957, 'friends_count': 1972, 'listed_count': 1840, 'created_at': 'Mon Sep 15 23:04:01 +0000 2008', 'favourites_count': 10320, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 47850, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'FFFFFF', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme9/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme9/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1324033377079451648/EY3wg2LV_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1324033377079451648/EY3wg2LV_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16303450/1606090653', 'profile_link_color': '0051BA', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': '252429', 'profile_text_color': '666666', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': True, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}), ('geo', None), ('coordinates', None), ('place', None), ('contributors', None), ('is_quote_status', False), ('retweet_count', 48), ('favorite_count', 571), ('favorited', True), ('retweeted', False), ('possibly_sensitive', False), ('lang', 'en')])
    '''
    # for x in eachfavoritetweets._json.items():
    #     print(x)
    #     print("\n")
    print("favorite tweet id:", eachfavoritetweets._json["id_str"])
    # print("date favorite:", convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[0])
    # print("time favorite:", convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[1])
    # print("favorite tweet handle: " + eachfavoritetweets._json["user"]["screen_name"])
    # print("text: " + eachfavoritetweets._json["text"])
    # print("text utf-8: " + eachfavoritetweets._json["text"].encode("unicode-escape").decode("utf-8"))
    try:
        print("picture: " + eachfavoritetweets._json["entities"]["media"][0]["media_url_https"]) #print https://pbs.twimg.com/media/End4gsEVgAA600h.jpg
    except:
        pass
    try:
        print("videos data type: ", type(eachfavoritetweets._json["extended_entities"]["media"][0])) #print videos:  <class 'dict'>
    except:
        pass
    print("\n")

    #print("videos: ", eachfavoritetweets._json["extended_entities"]["media"][0].items())
    '''
    ('video_info', {'aspect_ratio': [16, 9], 'duration_millis': 57516, 'variants': [{'content_type': 'application/x-mpegURL', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/pl/MqIyiglMN8I_KIcW.m3u8?tag=13'}, {'bitrate': 832000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/640x360/r7T1rG1Ig9NkpHhy.mp4?tag=13'}, {'bitrate': 288000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/480x270/zqccBDD7Cmg8m6Ab.mp4?tag=13'}, {'bitrate': 2176000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/1280x720/yX9zzBSpINuluP8f.mp4?tag=13'}]})
    '''
    try:
        for eachvideourl in eachfavoritetweets._json["extended_entities"]["media"][0]["video_info"]["variants"]:
            print(eachvideourl["content_type"])
            if eachvideourl["content_type"] == "video/mp4":
                print(eachvideourl["url"])
    except:
        pass
