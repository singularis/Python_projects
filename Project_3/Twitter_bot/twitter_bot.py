from twilio.rest import Client

account_sid = ./account_sid
auth_token =  ./auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+19292050759',
    body='It`s work',
    to='+380661246867'
)

print(message.sid)
