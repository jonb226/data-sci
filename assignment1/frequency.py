import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    tweets = [];
    for line in tweet_file:
		tweet_dict = json.loads(line)
		if 'text' in tweet_dict:
			tweet_text = tweet_dict['text']
			tweets.append(tweet_text)

    total_count = 0.0
    word_count = {}

    for tweet in tweets:
		words = tweet.split(' ');
		for word in words:
			if(word in word_count):
				word_count[word] += 1
			else:
				word_count[word] = 1.0
			total_count += 1.0

    print word_count[sys.argv[2]]/total_count

if __name__ == '__main__':
    main()
