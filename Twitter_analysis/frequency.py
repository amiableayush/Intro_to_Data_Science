from __future__ import division

import sys
import json


def main():
    tweet_words=[]
    
    with open(sys.argv[1],"r") as tweet_file:
        for line in tweet_file:
            tweet_dict=json.loads(line)
	    if "text" in tweet_dict:
	        tweet_word=tweet_dict["text"].split()
	        for i in range(len(tweet_word)):
		    tweet_word[i]=tweet_word[i].encode("utf-8")
		    tweet_words.append(tweet_word[i])	
	       	    
    unique_list=[]
    for item in tweet_words:
	if item in unique_list:
	    continue
	else:
	    unique_list.append(item)
        
        

    total=0
    freq=[]
    for item in unique_list:
        start_at = -1
        locs = []
	count=0
        while True:
            try:
                loc = tweet_words.index(item,start_at+1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
		count=count+1
	total=total+count	
	freq.append(count)
    
    for i in range(len(unique_list)):
	print unique_list[i] ,freq[i]/total
         
if __name__ == '__main__':
    main()
		
	    
