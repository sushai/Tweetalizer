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
      tweet = raw_input("What tweet would you like to analyze? To quit, just enter 'q'. ") #if using python 3, use input function

      if tweet == 'q' or tweet == 'Q':
          exit()

      tweetLength = len(tweet)
      maxLength = 140

      print("Tweet is " + str(tweetLength) + " characters long")
      if tweetLength > maxLength:
        #if len(tweet) > 140:
          print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

      hashtags = 0
      for x in tweet.split(' '):
          if x[0] == "#":
              print("Tweet contains the hashtag: " + x)
              hashtags += 1
      print("The tweet has " + str(hashtags) + " total #hashtags")

      tweets = 0
      for x in tweet.split(' '):
          if x[0] == "@":
              print("Tweet contains the mention: " + x)
              tweets += 1
      print("The tweet has " + str(tweets) + " total @mentions")


tweetalize()
