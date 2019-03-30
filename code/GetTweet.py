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

idlist = []
f_id = open("./idlist.json",'r')
tmpjson = json.load(f_id)
idlist = tmpjson['idlist']
idset = set(idlist)
f_id.close()

f_data = open("./data.json", 'a')
search_results = tweepy.Cursor(api.search, q="place:01864a8a64df9dc4").items(10)
#for line in f.readlines():
    #idlist.append(list(map(int,line.split(','))))
for tweet in search_results:
    if tweet._json['id'] in idlist :
    	continue
    else:
        number += 1
    #print(tweet._json['id'])
    #print(tweet._json['created_at'])
    #print(tweet._json['in_reply_to_screen_name'])
    #print(tweet._json['text'])
    #print(tweet._json['place']['name'])
    #print(number)
        idset.add(tweet._json['id'])
        dic = {'id':tweet._json['id'], 'At': tweet._json['created_at'],'name': tweet._json['in_reply_to_screen_name'], 'text': tweet._json['text'],'place': tweet._json['place']['name'], 'num': number}
        js = json.dumps(dic, sort_keys=False, indent=4, separators=(',', ':'))
        json.dump(js,f_data)
    #f.write(js)
        print(js)
#This is the third way to call API
#for tweet in tweepy.Cursor(api.search,q='test',since='2015-06-26 10:01:25',until='2015-06-26 10:15:10').items():
f_data.close()



f_id = open("./idlist.json",'w')
idlist2=list(idset)
dic2 ={'idlist':idlist2}
js2 = json.dumps(dic2)
f_id.writelines(js2)
f_id.close()


print('over')






