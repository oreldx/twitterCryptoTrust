import tweepy
import configparser


def auth():
    # Load Creditentials
    config = configparser.ConfigParser()
    config.read('creds.ini')

    apiKey = config['twitter']['api_key']
    apiKeySecret = config['twitter']['api_key_secret']
    accessToken = config['twitter']['access_token']
    accessTokenSecret = config['twitter']['access_token_secret']

    auth = tweepy.OAuth1UserHandler(
       apiKey, apiKeySecret, accessToken, accessTokenSecret
    )

    return tweepy.API(auth)


def retrievID(users):
    for user in users:
        item = api.get_user(screen_name=user)
        print(item.id)


if __name__ == '__main__':

    accounts = [
        'cacaboxtv'
    ]

    api = auth()
    retrievID(accounts)

    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
