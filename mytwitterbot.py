#YouTube CS DoJo
#Documentation http://docs.tweepy.org/en/latest/api.html#timeline-methods

import tweepy
import twitter_credentials as tc
import time

authenticate = tweepy.OAuthHandler(tc.consumerkey, tc.consumersecret)
authenticate.set_access_token(tc.accesstoken, tc.accesstokensecret)
api = tweepy.API(authenticate)

print("This is my twitter bot.  RM:  Instructor created print statement to check for errors when running.")

mentionswarmup = api.mentions_timeline(count=2) #API.mentions_timeline([since_id][, max_id][, count]).  Returns the 20 most recent mentions, including retweets.
print(mentionswarmup[1])
print(type(mentionswarmup)) #print <class 'tweepy.models.ResultSet'>  RM:  instructor Googled tweepy.models.ResultSet.  Search how to extract information.  A Stack Overflow website search result appeared https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset
print(type(mentionswarmup[1])) #print <class 'tweepy.models.Status'>  RM:  instructor Googled tweepy.models.Status.  Search how to extract information.  He found nothing useful.  
print((mentionswarmup[1].__dict__)) #print Converts the object to a dictionary.
print((mentionswarmup[1].__dict__.keys())) #print dict_keys(['_api', '_json', 'created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'source', 'source_url', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'author', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'lang']).  Converts the object to a dictionary.  These are the attributes for the class.
print((mentionswarmup[1].text)) #print @inin61 tweepy bot please ignore #1
print((mentionswarmup[1].id)) #print 1200930183491907584
print(type(mentionswarmup[1].id)) #print <class 'int'>

# mentions = api.mentions_timeline()
# for eachmentions in mentions:
# 	print(str(eachmentions.id) + " " +eachmentions.text)
# 	print(eachmentions.user.screen_name)
# 	if ("#helloworld") in eachmentions.text.lower():
# 		print("I FOUND HELLOWORLD")
# 		api.update_status("@" +eachmentions.user.screen_name+ " I see your #HelloWorld.  Hello back to you.  tweepy bot please ignore.", eachmentions.id)
'''
1200930248201625600 @inin61 tweepy bot please ignore #2 #HelloWorld
inin61
I FOUND HELLOWORLD
1200930183491907584 @inin61 tweepy bot please ignore #1
inin61
1196134014748246016 @inin61 Nice work! Now it's time to start brainstorming funny ideas for Twitter bots
mduo13
...
'''

'''
#Timer
import time
time.sleep(15) is a 15 second Timer
while True:
	functionname()
	time.sleep(15) #runs the function functionname every 15 seconds  Instructor wrote the mentions = api.mentions_timeline() in a function to run every 15 seconds.
'''

def mentionsfunctionhelloworld(counter):
	mentionsfunction = api.mentions_timeline()
	for eachmentions in mentionsfunction:
		print(eachmentions.user.screen_name + str(eachmentions.id) + " " +eachmentions.text)
		if ("#helloworld") in eachmentions.text.lower():
			print("I FOUND HELLOWORLD")
			api.update_status("@" +eachmentions.user.screen_name+ " I see your #HelloWorld.  Hello back to you.  Counter " +str(counter)+ " tweepy bot please ignore.", eachmentions.id)
			break
counter = 1
while True:
	print(mentionsfunctionhelloworld(counter))
	'''
	inin611200942642894270464 @inin61 I see your #HelloWorld.  Hello back to you.  tweepy bot please ignore.
	I FOUND HELLOWORLD
	None
	inin611200946956811419648 @inin61 I see your #HelloWorld.  Hello back to you.  Counter 1 tweepy bot please ignore.
	I FOUND HELLOWORLD
	None
	inin611200946971906674688 @inin61 I see your #HelloWorld.  Hello back to you.  Counter 2 tweepy bot please ignore.
	I FOUND HELLOWORLD
	None
	inin611200946987081719808 @inin61 I see your #HelloWorld.  Hello back to you.  Counter 3 tweepy bot please ignore.
	I FOUND HELLOWORLD
	...
	'''
	time.sleep(3)
	counter +=1
	if counter == 10:
		break


# def testcounter(check):
# 	return check
# counter=0
# while True:
# 	print(testcounter(counter))
# 	time.sleep(1)
# 	counter +=1
# 	if counter == 10:
# 		break
