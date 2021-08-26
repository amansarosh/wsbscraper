import praw

# import client details
reddit = praw.Reddit(client_id='xxx',
                     client_secret='xxx',
                     username='xxx',
                     password='xxx',
                     user_agent='xxx')

# scraping destination

# to-do: read from config file as well as credentials
subreddit = reddit.subreddit('python')

# posts to retrieve
hot_wsb = subreddit.hot(limit=5)

# loop over post and see post metrics
for submission in hot_wsb:
    if not submission.stickied:
        print('Title: {} // Upvotes: {}'.format(submission.title, submission.ups,))
