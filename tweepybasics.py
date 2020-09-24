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

#WIP Print recent tweets in my timeline including retweets with dates, url links, and retweet link
#https://stackoverflow.com/questions/48436964/problems-collecting-280-characters-using-tweepy
# mytweetslist = []
# mytweets = api.user_timeline(screen_name = "inin61", count=1, tweet_mode="extended")
# print(mytweets) #print [Status(_api=<tweepy.api.API object at 0x7f77b2fa9278>, _json={'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, ...
# print(mytweets[0]) #print [Status(_api=<tweepy.api.API object at 0x7f77b2fa9278>, _json={'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, ...
# print(mytweets[0]._json) #print {'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, ...

# for status in tweepy.Cursor(api.user_timeline, id="inin61", tweet_mode="extended").items(3):
#   #print(status._json) #print {'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, ...
#   #print(status._json["full_text"])

# for status in api.user_timeline(id="inin61", tweet_mode="extended", count=3):
#   print(status._json["full_text"])

# for tweet in tweepy.Cursor(api.search,q="inin61",lang="en",since="2019-10-26",tweet_mode="extended").items():
#   print(tweet.full_text)

#WIP 2 Print recent tweets in my timeline including retweets with dates, url links, and retweet link
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=5):
    #print(status) #print Status(_api=<tweepy.api.API object at 0x7f190e2882e8>, _json={'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, 'id_str': '1283478007181537280', 'full_text': ...
    #print(type(status)) #print <class 'tweepy.models.Status'>
    try:
        print(status._json["retweeted_status"]["full_text"]) #print Residences are cleaner in the autumn and winter seasons because the windows are closed.  People spend more time indoors.
        print(status._json["retweeted_status"]["created_at"]) #print Residences are cleaner in the autumn and winter seasons because the windows are closed.  People spend more time indoors.
        print(status._json["retweeted_status"]["entities"]["media"][0]["expanded_url"]) #print https://twitter.com/espn/status/1283084418060451840/video/1
    except KeyError:
        print(status._json["full_text"]) #print Residences are cleaner in the autumn and winter seasons because the windows are closed.  People spend more time indoors.
        print(status._json["created_at"]) #print Residences are cleaner in the autumn and winter seasons because the windows are closed.  People spend more time indoors.
        for eachtweeturl in status._json["entities"]["urls"]:
            print(eachtweeturl["expanded_url"])
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=20):
    #print(status) #print Status(_api=<tweepy.api.API object at 0x7f190e2882e8>, _json={'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, 'id_str': '1283478007181537280', 'full_text': ...
    #print(type(status)) #print <class 'tweepy.models.Status'>
    print(status._json["id"])
    if status._json["retweeted"] == False:
        print(status._json["created_at"])
        print(type(status._json["created_at"]))
        print(status._json["created_at"][0:19])
        print(status._json["full_text"])
        for eachtweeturl in status._json["entities"]["urls"]:
            print(eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print(eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print(eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print(status._json["retweeted_status"]["created_at"])
        print(status._json["retweeted_status"]["user"]["screen_name"])
        print(status._json["retweeted_status"]["full_text"])
        print(status._json["retweeted_status"]["id"])
        for eachtweeturl in status._json["entities"]["urls"]:
            print(eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print(eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print(eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    else:
        print("There is an error.")
    print("\n")
#https://stackoverflow.com/questions/18711398/converting-twitters-date-format-to-datetime-in-python/18736802
from datetime import datetime
d = datetime.strptime(status._json["created_at"], '%a %b %d %H:%M:%S %z %Y')
print(d.strftime('%Y-%m-%d'))

#WIP 3 Added retweet my own tweets.  I think I'm getting information from different jsons fields.  Can I be consistent use same json fields?
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=21):
    #print(status)
    print("Retweet myself?:", status._json["is_quote_status"])
    print("Retweet?:", status._json["retweeted"])
    #print(status) #print Status(_api=<tweepy.api.API object at 0x7f190e2882e8>, _json={'created_at': 'Wed Jul 15 19:06:17 +0000 2020', 'id': 1283478007181537280, 'id_str': '1283478007181537280', 'full_text': ...
    #print(type(status)) #print <class 'tweepy.models.Status'>
    print("Tweet id:", status._json["id"])
    print("Tweet date:", status._json["created_at"])
    #print(type(status._json["created_at"])) #print <class 'str'>
    if status._json["is_quote_status"] == True:
        print("Tweet text:", status._json["full_text"])
        print("Retweet myself date:", status._json["quoted_status"]["created_at"])
        print("Retweet myself user:", status._json["quoted_status"]["user"]["screen_name"])
        print("Retweet myself tweet text:", status._json["quoted_status"]["full_text"])
        print("Retweet myself tweet id:", status._json["quoted_status"]["id"])
        for eachtweeturl in status._json["quoted_status"]["entities"]["urls"]:
            print("Retweet myself url:", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet myself retweet picture url:", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet myself video link:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == False:
        print("Tweet text:", status._json["full_text"])
        for eachtweeturl in status._json["entities"]["urls"]:
            print("expanded url:", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Media url:", eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Video url:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print("Retweet date:", status._json["retweeted_status"]["created_at"])
        print("Retweet user:", status._json["retweeted_status"]["user"]["screen_name"])
        print("Retweet tweet text:", status._json["retweeted_status"]["full_text"])
        print("Retweet tweet id:", status._json["retweeted_status"]["id"])
        for eachtweeturl in status._json["entities"]["urls"]:
            print("Retweet media url:", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Video url:", eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print(eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    # elif status._json["is_quote_status"] == False:
    #   for eachtweeturl in status._json["entities"]["urls"]:
    #       print("expanded media url:",eachtweeturl["expanded_url"])
    #   try:
    #       for eachtweeturl in status._json["extended_entities"]["media"]:
    #           print("media url:",eachtweeturl["media_url_https"])
    #   except KeyError:
    #       pass
    #   try:
    #       for eachtweeturl in status._json["extended_entities"]["media"]:
    #           print("video url:",eachtweeturl["video_info"]["variants"][0]["url"])
    #   except KeyError:
    #       pass
    else:
        print("There is an error.")
    print("\n")

#WIP 4 Correct fields.  All links and text downloaded correctly.
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=1):
    print("\n")
    print("My Tweet ID ", status._json["id"])
    print("Retweet? ", status._json["retweeted"])
    if status._json["is_quote_status"] == True:
        print("Retweeting Myself Date:", status._json["quoted_status"]["created_at"])
        print("Tweet text:", status._json["full_text"])
        print("Retweet Myself Tweet text:", status._json["quoted_status"]["full_text"])
        print("Retweet myself user:", status._json["quoted_status"]["user"]["screen_name"])
        print("Retweet myself tweet id:", status._json["quoted_status"]["id"])
        for eachtweeturl in status._json["quoted_status"]["entities"]["urls"]:
            print("Retweet myself url:", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet myself retweet picture url:", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet myself video link:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == False:
        print("Tweet Date " + status._json["created_at"])
        print("Tweet Text " + status._json["full_text"])
        for eachtweeturl in status._json["entities"]["urls"]:
            print("URL " + eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Pic url:", eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Video url:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print("Retweeting Date " + status._json["created_at"])
        print("Tweet Date " + status._json["retweeted_status"]["created_at"])
        print("Retweeting From " + status._json["retweeted_status"]["user"]["screen_name"])
        print("Retweeting Text Full " + status._json["retweeted_status"]["full_text"])
        print("Retweeting ID", status._json["retweeted_status"]["id"])
        for eachtweeturl in status._json["retweeted_status"]["entities"]["urls"]:
            print("URL " + eachtweeturl["url"])
        try:
            for eachtweeturl in status._json["retweeted_status"]["entities"]["media"]:
                print("Pic URL " + eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]["variants"]:
                print("Video URL " + eachtweeturl["url"])
        except KeyError:
            pass

#WIP 5 Code ready to go.  Prepare fields to download in .csv code.
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=100):
    print("\n")
    print("Tweet ID", status._json["id"])
    if status._json["is_quote_status"] == True:
        print("Retweet Quoted")
        print("Tweet Date " + status._json["created_at"])
        print("Retweet Myself My Quote", status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        print("Retweet Myself Tweet Date", status._json["quoted_status"]["created_at"])
        print("Retweet Myself ID", status._json["quoted_status"]["id"])
        print("Retweet Myself From", status._json["quoted_status"]["user"]["screen_name"])
        print("Retweet Myself Text", status._json["quoted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["quoted_status"]["entities"]["urls"]:
            print("Retweet Myself Url:", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet Myself Picture Url:", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet Myself Video Url:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == False:
        print("Tweet")
        print("Tweet Date " + status._json["created_at"])
        print("Tweet Text " + status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["entities"]["urls"]:
            print("Tweet Url " + eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Tweet Picture Url:", eachtweeturl["media_url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Tweet Video Url:", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print("Retweet")
        print("Tweet Date " + status._json["created_at"])
        print("Retweet ID", status._json["retweeted_status"]["id"])
        print("Retweet Date " + status._json["retweeted_status"]["created_at"])
        print("Retweet From " + status._json["retweeted_status"]["user"]["screen_name"])
        print("Retweet Text " + status._json["retweeted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["retweeted_status"]["entities"]["urls"]:
            print("Retweet Url " + eachtweeturl["url"])
        try:
            for eachtweeturl in status._json["retweeted_status"]["entities"]["media"]:
                print("Retweet Picture Url " + eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]["variants"]:
                print("Retweet Video Url " + eachtweeturl["url"])
        except KeyError:
            pass
    else:
        print("Problem")

#WIP 6 Retweet Quoted What if the quoted is pics, videos, or both pics and videos.  Retween quoted pic origin pic is good.
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=2):
    print("\n")
    print(status)
    print("\n")
    print("Tweet ID", status._json["id"])
    if status._json["is_quote_status"] == True:
        print("Retweet Quoted")
        print("Tweet Date " + status._json["created_at"])
        print("Retweet Myself My Quote", status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Retweet Myself My Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Retweet Myself My Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
        print("Retweet Myself Origin Tweet Date", status._json["quoted_status"]["created_at"])
        print("Retweet Myself Origin ID", status._json["quoted_status"]["id"])
        print("Retweet Myself Origin Twitter Handle", status._json["quoted_status"]["user"]["screen_name"])
        print("Retweet Myself Origin Text", status._json["quoted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["quoted_status"]["entities"]["urls"]:
            print("Retweet Myself Origin Url", eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet Myself Origin Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("Retweet Myself Origin Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == False:
        print("Tweet")
        print("Tweet Date " + status._json["created_at"])
        print("Tweet Text " + status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["entities"]["urls"]:
            print("Tweet Url " + eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Tweet Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("Tweet Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print("Retweet")
        print("Tweet Date " + status._json["created_at"])
        print("Retweet ID", status._json["retweeted_status"]["id"])
        print("Retweet Date " + status._json["retweeted_status"]["created_at"])
        print("Retweet From " + status._json["retweeted_status"]["user"]["screen_name"])
        print("Retweet Text " + status._json["retweeted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["retweeted_status"]["entities"]["urls"]:
            print("Retweet Url " + eachtweeturl["url"])
        try:
            for eachtweeturl in status._json["retweeted_status"]["entities"]["media"]:
                print("Retweet Picture Url " + eachtweeturl["media_url_https"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]["variants"]:
                print("Retweet Video Url " + eachtweeturl["url"])
        except KeyError:
            pass
    else:
        print("Problem")

#WIP 7 Numbered headers.  Ready for tab delimited .csv and join urls and pic urls.
for status in api.user_timeline(id="inin61", tweet_mode="extended", count=150):
    print("1 Tweet ID", status._json["id"])
    print("2 Tweet Date " + status._json["created_at"])
    if status._json["is_quote_status"] == True:
        print("1b Tweet Type Retweet Quoted")
        print("3 Tweet Text:  Retweet Myself My Quote", status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        for eachtweeturl in status._json["entities"]["urls"][:-1]:
            print("4 Tweet Url:  Retweet Myself My Url " + eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("5 Tweet Picture Url:  Retweet Myself My Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        print("6 Origin Tweet ID:  Retweet Myself Origin ID", status._json["quoted_status"]["id"])
        print("7 Origin Tweet Date:  Retweet Myself Origin Tweet Date", status._json["quoted_status"]["created_at"])
        print("8 Origin Tweet Handle:  Retweet Myself Origin Twitter Handle", status._json["quoted_status"]["user"]["screen_name"])
        print("9 Origin Tweet Text:  Retweet Myself Origin Text", status._json["quoted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        try:
            for eachtweeturl in status._json["quoted_status"]["entities"]["urls"]:
                print("10 Origin Tweet Url:  Retweet Myself Origin Url", eachtweeturl["expanded_url"])
        except:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("10 Origin Tweet Url:  Retweet Myself Origin Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["quoted_status"]["extended_entities"]["media"]:
                print("11 Origin Tweet Pic Url:  Retweet Myself Origin Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
    elif status._json["retweeted"] == False:
        print("1b Tweet Type Tweet")
        print("3 Tweet Text " + status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        try:
            for eachtweeturl in status._json["entities"]["urls"]:
                print("4 Tweet Url " + eachtweeturl["expanded_url"])
        except:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("4 Tweet Url:  Tweet Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        except KeyError:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("5 Tweet Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
    elif status._json["retweeted"] == True:
        print("1b Tweet Type Retweet")
        try:
            print("6 Origin Tweet ID:  Retweet ID", status._json["retweeted_status"]["id"])
        except KeyError:
            print("6 Origin Tweet ID:  Retweet Your Own Tweet ID", status._json["id"])
        try:
            print("7 Origin Tweet Date:  Retweet Date " + status._json["retweeted_status"]["created_at"])
        except KeyError:
            print("7 Origin Tweet Date:  Retweet Your Own Tweet Date " + status._json["created_at"])
        try:
            print("8 Origin Tweet Handle:  Retweet From " + status._json["retweeted_status"]["user"]["screen_name"])
        except KeyError:
            print("8 Origin Tweet Handle:  Retweet Your Own Tweet From " + status._json["user"]["screen_name"])
        try:
            print("9 Origin Tweet Text:  Retweet Text " + status._json["retweeted_status"]["full_text"].encode("unicode-escape").decode("utf-8"))
        except KeyError:
            print("9 Origin Tweet Text:  Retweet Your Own Tweet Text " + status._json["full_text"].encode("unicode-escape").decode("utf-8"))
        try:
            for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]["variants"]:
                print("10 Origin Tweet Url:  Retweet Video Url " + eachtweeturl["url"])
        except:
            pass
        try:
            for eachtweeturl in status._json["retweeted_status"]["entities"]["urls"]:
                print("10 Origin Tweet Url:  Retweet Url " + eachtweeturl["expanded_url"])
        except KeyError:
            for eachtweeturl in status._json["entities"]["urls"]:
                print("10 Origin Tweet Url:  Retweet Your Own Url? " + eachtweeturl["expanded_url"])
        try:
            for eachtweeturl in status._json["retweeted_status"]["extended_entities"]["media"]:
                print("11 Origin Tweet Pic Url:  Retweet Picture Url", eachtweeturl["media_url_https"])
        except:
            pass
        try:
            for eachtweeturl in status._json["extended_entities"]["media"]:
                print("11 Origin Tweet Pic Url:  Retweet Your Own Picture Url", eachtweeturl["media_url_https"])
        except KeyError:
            pass
        #One tweet used Retweet Your Own Video Url
        # try:
        #     for eachtweeturl in status._json["extended_entities"]["media"]:
        #         print("Retweet Your Own Video Url", eachtweeturl["video_info"]["variants"][0]["url"])
        # except KeyError:
        #     pass
    else:
        print("Problem")
    print("\n")

colors = ["red", "blue", "white", "green", "black"]
print(", ".join(colors)) #print red, blue, white, green, black
header11 = ""
for eachcolors in colors:
    header11 = (", ".join(colors))
print(header11) #print red, blue, white, green, blac
links = ["https://pbs.twimg.com/media/EifVcOIXcAAYj1J.jpg", "https://pbs.twimg.com/media/EifVcYRWAAM-tw8.jpg", "https://pbs.twimg.com/media/EifVclEWoAAG1Zs.jpg", "https://pbs.twimg.com/media/EifVcvQX0AAMAbC.jpg"]
print(", ".join(links)) #print https://pbs.twimg.com/media/EifVcOIXcAAYj1J.jpg, https://pbs.twimg.com/media/EifVcYRWAAM-tw8.jpg, https://pbs.twimg.com/media/EifVclEWoAAG1Zs.jpg, https://pbs.twimg.com/media/EifVcvQX0AAMAbC.jpg

colors = ["white"]
links = [n for n in colors]
if len(links) == 1:
    print("".join(links)) #print white
else:
    print(", ".join(links))
colors = ["red", "blue", "white", "green", "black"]
links = [n for n in colors]
if len(links) == 1:
    print("".join(links))
else:
    print(", ".join(links)) #print red, blue, white, green, black

# for status in api.user_timeline(id="inin61", tweet_mode="extended", count=150):
#     if status._json["id"] == 1308927370720505856:
#         # for eachtweeturl in status._json["extended_entities"]["media"]:
#         #     print(eachtweeturl["media_url_https"])
#         print(status)
