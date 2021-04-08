
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf2153f25d73d02c977d84fe4383c38bd"
# Your Auth Token from twilio.com/console
auth_token  = "eb62bd4951bbdfc7b254c081d3e4c986"
client = Client(account_sid, auth_token)


message = client.messages.create(
    to="+5561998210607",
    from_="+12408307158",
    body="hello from twilio")
print(message.sid)


