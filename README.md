# SlackNewsBot

SlackNewsBot is a Python script that fetches the top news headlines from Israel using NewsAPI and posts them to a specified Slack channel.

## Setting Up

### Prerequisites
- Python 3.x
- `requests` library
- `slack_sdk` library

### Installation

1. Clone this repository or download the files.
2. Install the required Python libraries:

pip install requests slack_sdk


### Configuring Slack

1. Create a new Slack app at [Slack API](https://api.slack.com/apps).
2. Add permissions to the app: `chat:write`.
3. Install the app to your workspace and note the OAuth token (begins with `xoxb-`).
4. Find the ID of the Slack channel where you want to post the news.

### Configuring NewsAPI

1. Sign up at [NewsAPI](https://newsapi.org/register) and get your API key.

### Setting Up the Script

1. Open `main.py` and replace `YOUR_NEWSAPI_KEY` with your NewsAPI key.
2. Replace `YOUR_SLACK_BOT_TOKEN` with the Slack bot token.
3. Replace `YOUR_SLACK_CHANNEL_ID` with your Slack channel ID.

## Running the Script

Execute the script in the terminal:

python main.py


The script will fetch the latest news from Israel and post it to the specified Slack channel.
