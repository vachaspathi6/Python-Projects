## You need 4 credentials from your X (Twitter) account to run this code.

import tweepy

def tweet(message):
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    print("Tweet posted successfully!")

def main():
    message = input("Enter tweet message: ")
    tweet(message)

if __name__ == "__main__":
    main()
