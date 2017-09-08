import praw
import tweepy 
import time
import markovify



number_tweets=5
SUBREDDITNAME='r\ShowerThoughts'
CLIENT_ID='XXX'
CLIENT_SECRET='XXX'
PASSWORD='XXXX'
USER_AGENT='XXX'
USERNAME='XXX'

CONSUMER_KEY='XXX'
CONSUMER_SECRET='XXX'
ACCESS_TOKEN='XXX'
ACCESS_TOKEN_SECRET='XXX'

def reddit_conenction(subreddit):
	reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,  password=PASSWORD, user_agent=USER_AGENT, username=USERNAME)
	sub = reddit.subreddit(subreddit)
	return sub


def get_Reddit_posts(subreddit):
	post_titles = []
	post_ids = []
	for submission in subreddit.hot(limit=20):
		#if already_tweeted(submission.id):
			new_title=cleanup_text(submission.title)
			post_titles.append(new_title)
			post_ids.append(submission.id)
	return post_titles, post_ids

def cleanup_text(tweet):
	characters=len(tweet)
	if len(tweet)<=140: 
		return tweet
	elif len(tweet)>=140:
		return tweet[:140]
	else:
		return ""

def already_tweeted(p_id):
	with open('posted_tweets.txt', 'r') as file:
		for line in file.read().splitlines():
			if post_id == line:
				return True
	return False

def twitter_connection():
	print ("Authenticizing Twitter Connection")

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	twitter = tweepy.API(auth)
	
	print('Authenticated.')
	return twitter

# def log_tweet(post_id):
# 	count=0
#     with open(posted_tweeets, 'a') as log:
#         log.write(str(post_id[count]) + '\n')
#         count=count+1

def create_msg(tweets):
	new_tweets=[]
	for tweet in tweets:
		model = markovify.Text(tweets, state_size=1)
		new_tweet=model.make_short_sentence(140)
		new_tweets.append(new_tweet)
	return new_tweets


def post_tweet(api, tweets):
	for tweet in tweets:
		api.update_status(post_text)
		time.sleep(5*60)

def main():
	print("This is a Reddit Twitter Bot")
	subreddit = reddit_conenction('Showerthoughts')
	post_titles, post_ids=get_Reddit_posts(subreddit)
	#logTweets(post_ids)
	#chains=generate_chains()
	tweets=create_msg(post_titles)
	# messages=generate_messages(post_titles, post_links, post_ids)
	twit=twitter_connection()
	post_tweet(twit)



if __name__ == '__main__':
    main()
