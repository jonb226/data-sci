import sys
import json

def hw(scores, tweets):
    new_score_counter = {};
    for tweet in tweets:
        words = tweet.split(' ');
        tweet_avg = 0.0;
        count = 0.0;
        for word in words:
            if word in scores:
                tweet_avg = scores[word]
                count += 1.0
        if(count == 0.0):
            tweet_avg = 0.0;
        else:
            tweet_avg = tweet_avg/count
        for word in words:
            if word not in scores:
                if word in new_score_counter:
                    count = new_score_counter[word]['count']
                else:
                    count = 0.0
                new_score_counter[word] = {
                    'score': tweet_avg,
                    'count': count + 1.0
                }
    new_scores = {};
    for word in new_score_counter:
        new_scores[word] = new_score_counter[word]['score']/new_score_counter[word]['count']

    return new_scores;


def lines(fp):
    a = 3;

def main():
    sentiment_file = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sentiment_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])
    tweets = [];
    for line in tweet_file:
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict:
            tweet_text = tweet_dict['text']
            tweets.append(tweet_text);

    new_scores = hw(scores, tweets)
    word_to_test = sys.argv[3];

    if(word_to_test in scores):
        print 'Word was in given dictionary: '
        print scores[word_to_test]
    elif(word_to_test in new_scores):
        print 'Calculated score: '
        print new_scores[word_to_test]
    else:
        print 'Word was not in any tweets'



    lines(sentiment_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
