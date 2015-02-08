# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys

def tweetalize():
    print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")
    while True:
      tweet = getTweetFromUser()
      analyzeLength(tweet)
      analyzeHashtags(tweet)
      analyzeMentions(tweet)

def getTweetFromUser():
    userInput = raw_input("What tweet would you like to analyze? To quit, just enter 'q'. ") #if using python 3, use input function
    if userInput == 'q' or userInput == 'Q':
        exit()

    return userInput

def analyzeLength(tweet):
    tweetLength = len(tweet)
    print("Tweet is %d characters long" % tweetLength)

    maxTweetLength = 140
    if tweetLength > maxTweetLength:
        print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

def analyzeHashtags(tweet):
    hashtagCount = 0
    for word in tweet.split(' '):
        firstCharacter = word[0]
        if firstCharacter == "#":
            print("Tweet contains the hashtag: %s" % word)
            hashtagCount += 1
    print("The tweet has %d total #hashtags" % hashtagCount)

def analyzeMentions(tweet):
    mentionCount = 0
    for word in tweet.split(' '):
        firstCharacter = word[0]
        if firstCharacter == "@":
            print("Tweet contains the mention: %s" % word)
            mentionCount += 1
    print("The tweet has %d total @mentions" % mentionCount)

tweetalize()