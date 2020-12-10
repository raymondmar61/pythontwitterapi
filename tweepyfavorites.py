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
#Function combine multiple urls separate by comma
def joinURLs(links):
    if len(links) == 0:
        return None
    elif len(links) == 1:
        return "".join(links)
    else:
        return ", ".join(links)


#Print recent tweets in your timeline
#favoritetweets = api.favorites(id="inin61", count=201) #maximum count 200
#for eachfavoritetweets in favoritetweets:
#for eachfavoritetweets in tweepy.Cursor(api.favorites, id="inin61", tweet_mode="extended").items(201):
#for eachfavoritetweets in tweepy.Cursor(api.favorites, id="inin61", tweet_mode="extended").items(12):
counter = 1
for eachfavoritetweets in tweepy.Cursor(api.favorites, id="inin61", tweet_mode="extended").items(550):
    #print(eachfavoritetweets._json)
    #print(type(eachfavoritetweets._json)) #print <class 'dict'>
    #print((eachfavoritetweets._json).items())
    '''
    #dict_items([('created_at', 'Thu Dec 03 23:31:02 +0000 2020'), ('id', 1334641322154725376), ('id_str', '1334641322154725376'), ('full_text', 'Feds say Facebook broke US law offering permanent jobs to H-1B workers https://t.co/XhpZTqDPEv by @binarybits'), ('truncated', False), ('display_text_range', [0, 109]), ('entities', {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'binarybits', 'name': 'Timothy B. Lee', 'id': 14165170, 'id_str': '14165170', 'indices': [98, 109]}], 'urls': [{'url': 'https://t.co/XhpZTqDPEv', 'expanded_url': 'https://arstechnica.com/tech-policy/2020/12/feds-say-facebook-broke-us-law-offering-permanent-jobs-to-h-1b-workers/?utm_brand=arstechnica&utm_source=twitter&utm_social-type=owned&utm_medium=social', 'display_url': 'arstechnica.com/tech-policy/20…', 'indices': [71, 94]}]}), ('source', '<a href="http://arstechnica.com" rel="nofollow">Ars tweetbot</a>'), ('in_reply_to_status_id', None), ('in_reply_to_status_id_str', None), ('in_reply_to_user_id', None), ('in_reply_to_user_id_str', None), ('in_reply_to_screen_name', None), ('user', {'id': 717313, 'id_str': '717313', 'name': 'Ars Technica', 'screen_name': 'arstechnica', 'location': 'NYC - Boston - Chicago - SF', 'description': 'Original news, reviews, analysis of tech trends, and expert advice on the most fundamental aspects of tech.', 'url': 'http://t.co/Ul1NPoX9hd', 'entities': {'url': {'urls': [{'url': 'http://t.co/Ul1NPoX9hd', 'expanded_url': 'http://arstechnica.com', 'display_url': 'arstechnica.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 1162904, 'friends_count': 1307, 'listed_count': 28313, 'created_at': 'Sun Jan 28 01:58:49 +0000 2007', 'favourites_count': 7932, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 114474, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '201F25', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/2215576731/ars-logo_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2215576731/ars-logo_normal.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/717313/1407516523', 'profile_link_color': 'FF5B00', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'EEEEEE', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': True, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}), ('geo', None), ('coordinates', None), ('place', None), ('contributors', None), ('is_quote_status', False), ('retweet_count', 11), ('favorite_count', 18), ('favorited', True), ('retweeted', False), ('possibly_sensitive', False), ('lang', 'en')])
    '''
    #print(counter)
    print(counter, "favorite tweet id:", eachfavoritetweets._json["id_str"])
    # # for x in eachfavoritetweets._json.items():
    # #     print(x)
    # #     print("\n")
    print("date favorite:", convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[0])
    print("time favorite:", convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[1])
    print("favorite tweet handle: " + eachfavoritetweets._json["user"]["screen_name"])
    print("text: " + eachfavoritetweets._json["full_text"])
    # # print("\n")
    # #print("text utf-8: " + eachfavoritetweets._json["full_text"].encode("unicode-escape").decode("utf-8"))
    try:
        print("urls: " + eachfavoritetweets._json["entities"]["urls"][0]["expanded_url"])
    except:
        pass
    try:
        numberofpicslinks = len((eachfavoritetweets._json["extended_entities"]["media"]))
        piclinks = [eachfavoritetweets._json["extended_entities"]["media"][x]["media_url_https"] for x in range(0, numberofpicslinks)]
        print("pic urls: " + joinURLs(piclinks))
    except:
        pass
    try:
        videolinks = [eachlist["url"] for eachlist in eachfavoritetweets._json["extended_entities"]["media"][0]["video_info"]["variants"] if ".mp4" in eachlist["url"]]
        print("video urls: " + joinURLs(videolinks))
    except:
        pass
    counter += 1
    print("\n")

    # #print("videos: ", eachfavoritetweets._json["extended_entities"]["media"][0].items())
    # '''
    # ('video_info', {'aspect_ratio': [16, 9], 'duration_millis': 57516, 'variants': [{'content_type': 'application/x-mpegURL', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/pl/MqIyiglMN8I_KIcW.m3u8?tag=13'}, {'bitrate': 832000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/640x360/r7T1rG1Ig9NkpHhy.mp4?tag=13'}, {'bitrate': 288000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/480x270/zqccBDD7Cmg8m6Ab.mp4?tag=13'}, {'bitrate': 2176000, 'content_type': 'video/mp4', 'url': 'https://video.twimg.com/amplify_video/1330653925804965888/vid/1280x720/yX9zzBSpINuluP8f.mp4?tag=13'}]})
    # '''
    # try:
    #     for eachvideourl in eachfavoritetweets._json["extended_entities"]["media"][0]["video_info"]["variants"]:
    #         print(eachvideourl["content_type"])
    #         if eachvideourl["content_type"] == "video/mp4":
    #             print(eachvideourl["url"])
    # except:
    #     pass
