# https://slack.dev/python-slackclient/index.html
from slackclient import SlackClient
from config import config


slack_args = {
    "botland": "CH18NPJ2G",
}

sc = SlackClient(config['token'])

sc.api_call(
  "chat.postMessage",
  channel=slack_args['botland'],
  text="wazzup?!"
)
