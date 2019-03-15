from twilio.rest import Client

account_sid = 'ACd5ab3c5d8b98a91117a5b5c8e73cb02a'
auth_token = '764316e55a3af39db689b52a2f86862f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Blake come out and write the lab!',
    to='whatsapp:+4369918281258'
)

print(message.sid)