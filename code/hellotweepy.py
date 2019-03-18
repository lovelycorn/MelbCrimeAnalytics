import tweepy

consumer_key = '24pWrfUqPqUPpIalseTolQvVh'
consumer_secret = 'lni7BT14qa6bLoE4958blDvkoUQMHX66J88Klvjg4R9sQbwOmR'
access_token = '1107208573036064770-endEUd5aMz7niD6d19anTriTldsizp'
access_token_secret = 'MWwhBhKrJeakP51ecWYKmenh4hoaU56WLLRa62eudbJXk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#for tweet in tweepy.Cursor(api.search, q='League of Legends').items(10):
#	print('Tweet by:@' + tweet.user.screen_name)
place = api.geo_search(query = "melbourne")
print(place)