from news_api_client import fetch_news
from slack_client import post_to_slack
from config import SLACK_CHANNEL_ID

def main():
    """Main function to fetch news and post it to Slack."""
    try:
        news = fetch_news()
        if news:
            post_to_slack(news, SLACK_CHANNEL_ID)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
