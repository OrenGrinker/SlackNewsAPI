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

pip install -r requirements.txt


### Configuring Slack

1. Create a new Slack app at [Slack API](https://api.slack.com/apps).
2. Add permissions to the app: `chat:write`.
3. Install the app to your workspace and note the OAuth token (begins with `xoxb-`).
4. Find the ID of the Slack channel where you want to post the news.

### Configuring NewsAPI

1. Sign up at [NewsAPI](https://newsapi.org/register) and get your API key.

#### Setting Up the Application

1. Navigate to the `config.py` file.
2. Replace `YOUR_NEWSAPI_KEY`, `YOUR_SLACK_BOT_TOKEN`, and `YOUR_SLACK_CHANNEL_ID` with your actual NewsAPI key, Slack bot token, and Slack channel ID, respectively.

## Running the Application

To run the application, execute the following command in the terminal:

python main.py


The script will fetch the latest news from Israel and post it to the specified Slack channel.

## Screenshot

![SlackNewsBot Screenshot](https://github.com/OrenGrinker/SlackNewsAPI/blob/636ff9336802a598e95b44c8736c2a6a3487fbe0/Screenshot%202024-03-02%20at%2019.31.08.png)

