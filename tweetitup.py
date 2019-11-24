#YouTube Python Codex
#Application programming interface API
#Day 29_ Twitter API with Python [720p]
#A Python wrapper around the Twitter API.  GitHub Python Twitter files bear / python-twitter https://github.com/bear/python-twitter
#twitter module documentation https://python-twitter.readthedocs.io/en/latest/twitter.html
#Run code on python2.7

import twitter
import twitter_credentials as tc

#Authenticate user.  Get user's information to do stuff.  Interact with the API.  Connect with the API.  To create an instance of the twitter.Api with login credentials.
api = twitter.Api(consumer_key=tc.consumerkey, consumer_secret=tc.consumersecret, access_token_key=tc.accesstokenkey, access_token_secret=tc.accesstokensecret)
#print(api.VerifyCredentials())
'''
{"created_at": "Mon Nov 02 03:27:17 +0000 2009", "default_profile": true, "description": "Strong bodies, strong minds. Earn a good life. Desire more important than knowledge. Berra: You can observe a lot by watching. I promise my tweets aren't boring", "favourites_count": 457, "followers_count": 66, "friends_count": 49, "id": 86863717, "id_str": "86863717", "listed_count": 9, "location": "San Jose, CA", "name": "Raymond Mar", "profile_background_color": "C0DEED", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", "profile_banner_url": "https://pbs.twimg.com/profile_banners/86863717/1489186606", "profile_image_url": "http://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg", "profile_image_url_https": "https://pbs.twimg.com/profile_images/1155542053129871360/Cq6onEhB_normal.jpg", "profile_link_color": "1DA1F2", "profile_sidebar_border_color": "C0DEED", "profile_sidebar_fill_color": "DDEEF6", "profile_text_color": "333333", "profile_use_background_image": true, "screen_name": "inin61", "status": {"created_at": "Sat Nov 16 23:44:29 +0000 2019", "id": 1195850155901112320, "id_str": "1195850155901112320", "in_reply_to_screen_name": "inin61", "in_reply_to_status_id": 1195850155100012544, "in_reply_to_user_id": 86863717, "lang": "en", "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", "text": "Semaphore is making letters with a visual signal device such as hand-held flags.  You're looking at a sailor.  The\u2026 https://t.co/O2c5Rx9LJg", "truncated": true}, "statuses_count": 6227, "url": "https://t.co/jXjuhIMFeG"}
'''
#Get user's friends or following
friends = api.GetFriends()
#print(friends)
'''
[User(ID=16547458, ScreenName=BrianBanmiller), User(ID=4519121, ScreenName=Oatmeal), User(ID=1002664853847224320, ScreenName=CHPAlerts), User(ID=17790911, ScreenName=NBCSAuthentic), User(ID=377939647, ScreenName=WatchItPlayed), User(ID=4059797592, ScreenName=BackpackersCom), User(ID=16583846, ScreenName=REI), User(ID=16060397, ScreenName=billamend), User(ID=164774445, ScreenName=RattoIndy), User(ID=522005117, ScreenName=connie_macy), User(ID=3282187208, ScreenName=m1chellemar), User(ID=16303450, ScreenName=SJEarthquakes), User(ID=15741679, ScreenName=GoodVibesToys), User(ID=1582853809, ScreenName=HistoryInPics), User(ID=20726460, ScreenName=SexWithEmily), User(ID=13706192, ScreenName=agent760), User(ID=17932641, ScreenName=Phandroid), User(ID=1475106410, ScreenName=Sunara_Ishi), User(ID=90118718, ScreenName=theloafingone), User(ID=717313, ScreenName=arstechnica), User(ID=134707146, ScreenName=scaloy), User(ID=727076942, ScreenName=Ariaxlesmomma), User(ID=749725092, ScreenName=Loktera), User(ID=79271242, ScreenName=bart415), User(ID=85516619, ScreenName=tone765), User(ID=441755399, ScreenName=WakeOfWeek), User(ID=64793470, ScreenName=TravisOdyssey), User(ID=29844505, ScreenName=psychodonuts), User(ID=69651404, ScreenName=_suspi), User(ID=92318463, ScreenName=jon_t_green), User(ID=83331261, ScreenName=mortalitycheck), User(ID=258562967, ScreenName=JayKimura), User(ID=242970339, ScreenName=Thundercloud01), User(ID=104041218, ScreenName=smileybastard), User(ID=148683316, ScreenName=ChunandRice), User(ID=16319138, ScreenName=myalchod), User(ID=14865634, ScreenName=mordyan), User(ID=31521889, ScreenName=angelwitch67), User(ID=28942051, ScreenName=christian29d), User(ID=8051992, ScreenName=dakanya), User(ID=117270602, ScreenName=Seijanokiseki), User(ID=34882786, ScreenName=omgyaystars), User(ID=27139146, ScreenName=Magical_Senpai), User(ID=15076341, ScreenName=mduo13), User(ID=2431991, ScreenName=Tidus), User(ID=16158866, ScreenName=TravelValNT), User(ID=29290348, ScreenName=EliteslayerX), User(ID=74671123, ScreenName=tsubasaaki), User(ID=20536907, ScreenName=PixelatedIndex)]
'''
#for u in friends:
	#find all the methods
	#print(dir(u))
'''
	['AsDict', 'AsJsonString', 'NewFromJsonDict', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_json', 'contributors_enabled', 'created_at', 'default_profile', 'default_profile_image', 'description', 'email', 'favourites_count', 'followers_count', 'following', 'friends_count', 'geo_enabled', 'id', 'id_str', 'lang', 'listed_count', 'location', 'name', 'notifications', 'param_defaults', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_banner_url', 'profile_image_url', 'profile_image_url_https', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'protected', 'screen_name', 'status', 'statuses_count', 'time_zone', 'url', 'utc_offset', 'verified', 'withheld_in_countries', 'withheld_scope']
'''
#for u in friends:
	#print(u.name)
'''
	BrianBanmiller
	Matthew Inman
	CHP - Alerts
	NBCSAuthentic
	Watch It Played @ BGGCon
	Backpackers.com
	REI
	Bill Amend
'''

#Get user's followers
followers = api.GetFollowers()
#print(followers)
'''
[User(ID=738092675644022784, ScreenName=history_thu_pic), User(ID=1150892100105527297, ScreenName=MarkTaissa), User(ID=1050796369521377280, ScreenName=MitB83351084), User(ID=17943283, ScreenName=sleepingkyoto), User(ID=1394782590, ScreenName=Filmfan17), User(ID=1066596686984896512, ScreenName=RilShohel), User(ID=750787718087671808, ScreenName=deepakvutla9), User(ID=807416434103984128, ScreenName=sirfluteboy02), User(ID=778425813716705284, ScreenName=homeschoolmeme), User(ID=718728213686534144, ScreenName=JacoboGuerra1), User(ID=626488746, ScreenName=Kret_Pokemon), User(ID=4644194689, ScreenName=epyatiqur1), User(ID=1427073133, ScreenName=skyluxtelelink), User(ID=4503441972, ScreenName=rush29july), User(ID=1053126625, ScreenName=gallonettoa123), User(ID=4717675229, ScreenName=Ashhad_Zeeshan), User(ID=522005117, ScreenName=connie_macy), User(ID=3022520636, ScreenName=ufoee1997), User(ID=3469161312, ScreenName=pkjbadhan), User(ID=3282187208, ScreenName=m1chellemar), User(ID=3130482358, ScreenName=mbunenkov), User(ID=82133702, ScreenName=BlissAuthority), User(ID=3074262937, ScreenName=OtteFamilyIns), User(ID=2792351500, ScreenName=Zepchat), User(ID=2831514686, ScreenName=Ccash101), User(ID=274160413, ScreenName=ldao48), User(ID=223989343, ScreenName=multitrackdrift), User(ID=2649493195, ScreenName=botb_johnnyboy), User(ID=2293548181, ScreenName=vinalanda346), User(ID=1907161663, ScreenName=012Zamroney), User(ID=13706192, ScreenName=agent760), User(ID=1475106410, ScreenName=Sunara_Ishi), User(ID=90118718, ScreenName=theloafingone), User(ID=430220192, ScreenName=dd_glitch), User(ID=134707146, ScreenName=scaloy), User(ID=727076942, ScreenName=Ariaxlesmomma), User(ID=749725092, ScreenName=Loktera), User(ID=79271242, ScreenName=bart415), User(ID=85516619, ScreenName=tone765), User(ID=64793470, ScreenName=TravisOdyssey), User(ID=69651404, ScreenName=_suspi), User(ID=302230188, ScreenName=DigitalBerri), User(ID=92318463, ScreenName=jon_t_green), User(ID=83331261, ScreenName=mortalitycheck), User(ID=258562967, ScreenName=JayKimura), User(ID=242970339, ScreenName=Thundercloud01), User(ID=215132380, ScreenName=Stormfalconsj), User(ID=22712386, ScreenName=CapeBarnes), User(ID=104041218, ScreenName=smileybastard), User(ID=148683316, ScreenName=ChunandRice), User(ID=131352712, ScreenName=OtakuTheSeries), User(ID=16319138, ScreenName=myalchod), User(ID=14865634, ScreenName=mordyan), User(ID=28942051, ScreenName=christian29d), User(ID=31521889, ScreenName=angelwitch67), User(ID=117270602, ScreenName=Seijanokiseki), User(ID=8051992, ScreenName=dakanya), User(ID=15076341, ScreenName=mduo13), User(ID=27139146, ScreenName=Magical_Senpai), User(ID=2431991, ScreenName=Tidus), User(ID=34882786, ScreenName=omgyaystars), User(ID=16158866, ScreenName=TravelValNT), User(ID=29290348, ScreenName=EliteslayerX), User(ID=74671123, ScreenName=tsubasaaki), User(ID=15686644, ScreenName=Spiritsnare), User(ID=20536907, ScreenName=PixelatedIndex)]
'''

#Modules Documentation https://python-twitter.readthedocs.io/en/latest/twitter.html
#To post a twitter status message (after being authenticated)
#posttweet = api.PostUpdate("I tweet from my Twitter API using module python-twitter in Python.")
#print(posttweet.text) #print I tweet from my Twitter API using module python-twitter in Python.
'''
There are many other methods, including:
>>> api.PostUpdates(status)
>>> api.PostDirectMessage(screen_name, text)
>>> api.GetUser(user)
>>> api.GetReplies()
>>> api.GetUserTimeline(user)
>>> api.GetHomeTimeline()
>>> api.GetStatus(status_id)
>>> api.GetStatuses(status_ids)
>>> api.DestroyStatus(status_id)
>>> api.GetFriends(user)
>>> api.GetFollowers()
>>> api.GetFeatured()
>>> api.GetDirectMessages()
>>> api.GetSentDirectMessages()
>>> api.PostDirectMessage(user, text)
>>> api.DestroyDirectMessage(message_id)
>>> api.DestroyFriendship(user)
>>> api.CreateFriendship(user)
>>> api.LookupFriendship(user)
>>> api.VerifyCredentials()
'''
statusvariable = "@inin61 I'm using PostUpdates #python"
#postupdates = api.PostUpdates(status=statusvariable)
#Calculate the length of a tweet using the utility below
postupdateslength = twitter.twitter_utils.calc_expected_status_length(status=statusvariable)
#print(postupdates) #print [Status(ID=1195961761184092165, ScreenName=inin61, Created=Sun Nov 17 07:07:58 +0000 2019, Text=u"@inin61 I'm using PostUpdates #python")]
#print(postupdateslength) #print 37
#Get Favorites
userfavorites = api.GetFavorites(screen_name="@inin61", count=1, include_entities=False, return_json=False)
#print(userfavorites)
#for eachmethod in userfavorites:
	#print(dir(eachmethod))
'''
	['AsDict', 'AsJsonString', 'NewFromJsonDict', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_json', 'contributors', 'coordinates', 'created_at', 'created_at_in_seconds', 'current_user_retweet', 'favorite_count', 'favorited', 'full_text', 'geo', 'hashtags', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'lang', 'location', 'media', 'param_defaults', 'place', 'possibly_sensitive', 'quoted_status', 'quoted_status_id', 'quoted_status_id_str', 'retweet_count', 'retweeted', 'retweeted_status', 'scopes', 'source', 'text', 'truncated', 'tweet_mode', 'urls', 'user', 'user_mentions', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope']
'''
#for eachmethod in userfavorites:
	#print(eachmethod.user, eachmethod.created_at, eachmethod.text)
'''
	(User(ID=134707146, ScreenName=scaloy), u'Fri Nov 15 19:20:48 +0000 2019', u'Thank you #AnimEigo!  #GunsmithCats looks amazing!\nWatching this brought me back to when I was 17-18 yrs old, when\u2026 https://t.co/9gpUsFxTak')
'''
#Send private message to myself
#newmessage = api.PostDirectMessage(screen_name="inin61", text="Did you get the private message")
#print(newmessage) #error message.  I can't send message to those who are not following you.