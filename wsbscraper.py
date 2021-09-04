import praw
import time

# import client details
reddit = praw.Reddit(client_id='xxx',
                     client_secret='xxx',
                     username='xxx',
                     password='xxx',
                     user_agent='xxx')

# <-----------------Questions--------------------------------------------> #
sub_answer = input('What Subreddit would you like to see: ')  # Left as input as subs are ints as well

# Title Amt
while True:
    try:
        listing_num = int(input(f'How many posts of {sub_answer} would you like to see? (Pick from 1-1000): '))
        if listing_num > 0:
            break
        print("Invalid number entered")
    except Exception as e:
        print(e)

# <-----------------Questions--------------------------------------------> #

# print('0% ####')
# time.sleep(.5)
# print('25% ##################')
# time.sleep(.5)
# print('50% ########################')
# time.sleep(.5)
# print('75% ##############################')
# time.sleep(.5)
# print('100% ####################################')

# <-----------------Questions--------------------------------------------> #

# variable definitions
subreddit = reddit.subreddit(sub_answer)
hot_wsb = subreddit.hot(limit=listing_num)

# loop over post and see post metrics
for submission in hot_wsb:
    print('Title: {} // Upvotes: {}'.format(submission.title, submission.ups, ))

# comment function
comment_limit = int(input('How many comments would you like to see would you like to see: '))

submission.comments.replace_more(comment_limit)  # define out comments

for comment in submission.comments.list():  # looping over comments
    print(comment.body)
    if len(comment.replies) > 0:
        for reply in comment.replies:
            print('||||||', reply.body)

#

while True:
    try:
        print('===')
        mention_questions = str(input('Would you like to count mentions?: '))
        if mention_questions == 'yes':
            mentions_ans = (input('What mentions?: '))
            print(f'You said {mentions_ans}')
            break
    except Exception as e:
        print(e)


# Code was basically dumped in, will organize and fix bugs later this week, hopefully.
