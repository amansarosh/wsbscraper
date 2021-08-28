# to-do: read from config file as well as credentials

import praw
import time

# import client details
reddit = praw.Reddit(client_id='xxx',
                     client_secret='xxx',
                     username='xxx',
                     password='xxx',
                     user_agent='xxx')

# Questions
sub_answer = str(input('What Subreddit would you like to see? '))
listing_num = int(input(f'How many posts of {sub_answer} would you like to see? (Pick from 1-1000) '))

print('0% ####')
time.sleep(.5)
print('25% ##################')
time.sleep(.5)
print('50% ########################')
time.sleep(.5)
print('75% ##############################')
time.sleep(.5)
print('100% ####################################')

# variable definitions
subreddit = reddit.subreddit(sub_answer)
hot_wsb = subreddit.hot(limit=listing_num)

# loop over post and see post metrics
for submission in hot_wsb:
    print('Title: {} // Upvotes: {}'.format(submission.title, submission.ups,))