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
      analyzeWords(tweet)

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

def analyzeWords(tweet):
    hashtagCount = 0
    mentionCount = 0

    tweetWords = tweet.split(' ')
    for word in tweetWords:
        if len(word) > 0:
            if isHashtag(word):
                hashtagCount += 1
            elif isMention(word):
                mentionCount += 1

    print("The tweet has %d total #hashtags" % hashtagCount)
    print("The tweet has %d total @mentions" % mentionCount)

def isHashtag(word):
    firstCharacter = word[0]
    if firstCharacter == "#":
        print("Tweet contains the hashtag: %s" % word)
        return True
    return False

def isMention(word):
    firstCharacter = word[0]
    if firstCharacter == "@":
        print("Tweet contains the mention: %s" % word)
        return True
    return False

tweetalize()