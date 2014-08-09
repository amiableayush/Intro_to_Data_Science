import sys
import json

def main():
    sent_dict={}
    with open(sys.argv[1],"r") as sent_file:
	for line in sent_file:
	    term, score= line.split("\t")
	    sent_dict[term]= score

    tweet_list=[]
    with open(sys.argv[2],"r") as tweet_file:
	for line in tweet_file:
	    tweet_list.append(json.loads(line))
    for index in range(len(tweet_list)):
	if "text" in tweet_list[index].keys():
	    tweet_word=tweet_list[index]["text"].split()
	    sent_score=0
	    for word in tweet_word:
	    	word=word.encode("utf-8")
	    	word=word.rstrip('?:!.,;"@')
	   	word=word.replace("\n","")
	    	if word in sent_dict.keys():
		    sent_score=sent_score + int(sent_dict[word])
	    	else:
		    sent_score=sent_score
	    print sent_score
	else:
	    continue
            

if __name__ == '__main__':
    main()
   

	    


