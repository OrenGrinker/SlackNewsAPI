import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Your NewsAPI key
newsapi_key = "YOUR_NEWSAPI_KEY"


# Function to fetch top news from Israel
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=il&apiKey=" + newsapi_key
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print("Failed to fetch news")
        return []


# Function to post a message to Slack
def post_to_slack(news, slack_token, channel):
    client = WebClient(token=slack_token)
    try:
        for article in news:
            response = client.chat_postMessage(
                channel=channel,
                text=f"Headline: {article['title']}\nLink: {article['url']}"
            )
    except SlackApiError as e:
        print(f"Got an error: {e.response['error']}")


# Main function to fetch news and post to Slack
def main():
    slack_token = "YOUR_SLACK_BOT_TOKEN"
    slack_channel = "YOUR_SLACK_CHANNEL_ID"

    news = fetch_news()
    if news:
        post_to_slack(news, slack_token, slack_channel)


if __name__ == "__main__":
    main()
