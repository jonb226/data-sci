import sys
import json
import pdb
import pprint

def pp(mydict):
    pretty_printer = pprint.PrettyPrinter(indent=4)
    pretty_printer.pprint(mydict)

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary

    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

    scores2 = []
    for line in tweet_file:
        score = 0
        tweet_dict = json.loads(line)
        if 'text' in tweet_dict:
            tweet_text = tweet_dict['text']
            # pdb.set_trace()
            for word in tweet_text.split(' '):
                if word in scores:
                    score = score + scores[word]
        scores2.append(score)

    print scores2[20:30]


if __name__ == '__main__':
    main()
