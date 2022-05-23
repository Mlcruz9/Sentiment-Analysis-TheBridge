import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "TheBridge_Tech until:2022-05-22 since:2022-01-01"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.replyCount])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Likes', 'Retweets', 'Replies'])
df.to_csv('tweets.csv')