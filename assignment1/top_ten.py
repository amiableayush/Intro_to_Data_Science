import sys
import json
import types
import operator
import collections

def main():
    
    
    with open(sys.argv[1],"r") as tweet_file:
        hash_count={}
	top=10
	for line in tweet_file:
	    tweets=json.loads(line)
	    if 'entities' in tweets and type(tweets['entities']) is not types.NoneType:
		if 'hashtags' in tweets['entities'] and type(tweets['entities']['hashtags']) is not types.NoneType:
		    
      		    h_list= tweets['entities']['hashtags']
		    for tags in h_list:
			text= tags['text'].encode("utf-8")
			if text in hash_count.keys():
			    hash_count[text]+=1
			else:
			    hash_count[text]=1

    d=collections.Counter(hash_count)
    for k, v in d.most_common(10):
	print k ,v

if __name__ == '__main__':
    main()

     
