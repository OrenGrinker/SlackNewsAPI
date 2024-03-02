from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_BOT_TOKEN

def post_to_slack(news, channel):
    """Post news articles to a specified Slack channel."""
    client = WebClient(token=SLACK_BOT_TOKEN)
    for article in news:
        try:
            client.chat_postMessage(
                channel=channel,
                text=f"Headline: {article['title']}\nLink: {article['url']}"
            )
        except SlackApiError as error:
            raise Exception(f"Slack API error: {error.response['error']}")
