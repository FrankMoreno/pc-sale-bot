import sys
from twilio.rest import Client
import praw

account_sid = "ACc7ee79de1e6a6201e7190755377f6358"
auth_token  = "976d369c6ebb6d309c9fe0394cbe1f8b"

client = Client(account_sid, auth_token)

bot = praw.Reddit(user_agent='MovieBot', client_id='gu7RSpgtKngx2A', client_secret='uVjiogo_X3SZmvoOMXJCqNAdP8g', username='MrGrumpyins', password='Tacos123')
finished = []

past_posts = open('posts.txt', 'r')
for line in past_posts:
    finished.append(line.strip())
past_posts.close

subreddit = bot.subreddit('buildapcsales')
submissions = subreddit.stream.submissions()
try:
    for submission in submissions:
        if submission.id not in finished:
            if '1060' in submission.title.lower():
                message = client.messages.create(
                    to="+14693861646", 
                    from_="+14696208635",
                    body=submission.url)
                print message.sid
except KeyboardInterrupt:
    past_posts = open('posts.txt', 'w')
    for post in finished:
        past_posts.write(post+'\n')
        past_posts.close
    print "File updated"

sys.exit(0)
