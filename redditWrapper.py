import praw


def reddit_conenction(subreddit):
	r = praw.Reddit(client_id='7KPMmtqSFtNVpA',
                     client_secret='w7oDFz3dM1KViWPMOpQzfMsGbUo',
                     password='thebeatles123',
                     user_agent='testscript by /u/fakebot3',
                     username='kwangster135')
	subR=r.get.subreddit(subreddit)
	return subR


def runbot():
	subreddit=r.get_subreddit("a")
	comments=subreddit.get_comment
