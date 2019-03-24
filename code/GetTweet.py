import tweepy
import json


consumer_key = '24pWrfUqPqUPpIalseTolQvVh'
consumer_secret = 'lni7BT14qa6bLoE4958blDvkoUQMHX66J88Klvjg4R9sQbwOmR'
access_token = '1107208573036064770-endEUd5aMz7niD6d19anTriTldsizp'
access_token_secret = 'MWwhBhKrJeakP51ecWYKmenh4hoaU56WLLRa62eudbJXk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#for tweet in tweepy.Cursor(api.search, q='League of Legends').items(10):
#   print('Tweet by:@' + tweet.user.screen_name)
regions = ["melbourne","ballarat","warrnambool"]
places = api.geo_search(query = 'ballarat')[0]
number = 0
# This is the first way to call API
#search_results = api.search(q="place:01864a8a64df9dc4",count=300)
#for tweet in search_results:
#    print(tweet._json['text'])
#    print(tweet.lang)

#This is the second way to call API
max_tweets = 1000
search_results = tweepy.Cursor(api.search, q="place:01864a8a64df9dc4").items(5)
for tweet in search_results:
    number += 1
    print(tweet._json['created_at'])
    print(tweet._json['text'])
    print(number)
#This is the third way to call API
#for tweet in tweepy.Cursor(api.search,q='test',since='2015-06-26 10:01:25',until='2015-06-26 10:15:10').items():
print('over')





