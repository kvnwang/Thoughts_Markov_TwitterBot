import praw
import json
import requests
import tweepy 
import time


number_tweets=5
SUBREDDITNAME='r\ShowerThoughts'
CLIENT_ID='XXX'
CLIENT_SECRET='XXX'
PASSWORD='XXX'
USER_AGENT='XXX'
USERNAME='XXX'

CONSUMER_KEY='XXX'
CONSUMER_SECRET='XXX'
ACCESS_TOKEN='XXX'
ACCESS_TOKEN_SECRET='XXX'

def reddit_conenction(subreddit):
	r = praw.Reddit(
		client_id=CLIENT_ID, 
		client_secret=CLIENT_SECRET,  
		password=PASSWORD, 
		user_agent=USER_AGENT, 
		username=USERNAME)
	subR=r.get.subreddit(subreddit)
	return subR

def get_Reddit_posts(subreddit):
	post_titles = []
	post_links = []
	post_ids = []
	for submission in subreddit.get_hot(limit=5):
		if already_tweeted(submission.id): 
			p_id=submission.id
			post_link=submission.url
			post_title=clean_title(submission.title)
			print (post_title)

			post_titles.append(post_title)
			post_links.append(post_link)
			post_ids.append(post_id)
	return post_titles, post_links, post_ids

def clean_title(title):
	characters=len(title)
	if len(title)<=140: 
		return title
	elif len(title>=140):
		return title[:140]
	else:
		return ""

def already_tweeted(p_id):
    with open(posted_tweeets, 'r') as file:
        for line in file:
            if pid in line:
            	return True
    return False

def twitter_connection():
	print ("Authenticizing Twitter Connection")

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	twitter = tweepy.API(auth)
	
	print('Authenticated.')
	return twitter

def log_tweet(post_id):
    with open(posted_tweeets, 'a') as log:
        log.write(str(post_id) + '\n')

# def issue_tweets(api):
# 	for post, post_id in zip(post_titles, post_ids):
#         post_text = strip_title(post)
#         print('[bot] Posting this link on Twitter')
#         print(post_text)
#         api.update_status(post_text)
#         log_tweet(post_id)
#         time.sleep(DELAY_BETWEEN_TWEETS)

def main():
	print("This is a Reddit Twitter Bot")
	subreddit = reddit_conenction(SUBREDDIT_TO_MONITOR)
	post_titles, post_links, post_ids=get_Reddit_posts(subreddit)
	# chains=generate_chains()
	# messages=generate_messages(post_titles, post_links, post_ids)
	# twit=twitter_connection()
	#issue_tweets(twit)



if __name__ == '__main__':
    main()
