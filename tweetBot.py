"""
This is a program for tweeting without needing to open the Twitter web application.

The tweet is to be written into a text file named "Tweet.txt".

The program presupposes:
    - Twitter API access keys fetched from Twitter's developer portal;
    they should be in a text file named 'twitterkeys.txt'
    - Tweepy

Additional benefit for using this bot: you can customize the device name from which you
are tweeting. It is the name of your application on the Twitter developer site.
"""

import tweepy

all_keys = open("twitterkeys.txt", 'r').read().splitlines()
# The order of the keys in the file ought to be as follows:
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

# Authentication:
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# Inserting the tweet contents into another text file:
f = open('Tweet.txt', 'r')
Tweet = f.read()
if len(Tweet) < 141:
    print(Tweet)
    print("Your tweet has " + str(len(Tweet)) + " characters.")
    confirm = input("Tweet this? (yes/no): ")
    if confirm == "yes":
        api.update_status(Tweet)
        print("")
        print("Tweet sent successfully!")
    else:
        print("Tweet was not sent.")
else:
    print("The tweet you tried to send is too long; it has " + str(len(Tweet)) + " characters. \n")
    print("This is", len(Tweet) - 140, "characters too many.")
    print("Please try again!")
    print("")
f.close()
