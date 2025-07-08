import tweepy
import requests
import os
from dotenv import load_dotenv
load_dotenv()

TWITTER_BEARER = os.getenv("TWITTER_BEARER")

client = tweepy.Client(bearer_token=TWITTER_BEARER)

def search_tweets(query, max_results=10):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    return [tweet.text for tweet in tweets.data]

def get_snapshot_proposals(space="uniswap"):
    url = f"https://hub.snapshot.org/graphql"
    query = {
        "query": """
        {
          proposals(first: 5, where: {space_in: ["%s"]}) {
            id
            title
            state
            scores
            created
          }
        }
        """ % space
    }
    response = requests.post(url, json=query)
    return response.json()


def get_tally_governance(address):
    url = f"https://api.tally.xyz/v1/proposals?contractAddress={address}"
    headers = {"API-Key": os.getenv("TALLY_API_KEY")}
    return requests.get(url, headers=headers).json()
