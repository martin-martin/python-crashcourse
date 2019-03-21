# https://slack.dev/python-slackclient/index.html
from slackclient import SlackClient
from config import config
from pprint import pprint


slack_args = {
    "python-resources": "CGUDWETHR",
}

sc = SlackClient(config['token'])
history = sc.api_call("channels.history",
                      channel=slack_args['python-resources'])
messages = history['messages']

#print(messages)

for m in messages:
    link = m['text'].strip('<>')
    if 'http' in link:
        print(link)
