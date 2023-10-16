from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number
from_number = 'your_twilio_number'

# Recipient's phone number
to_number = 'recipient_number'

# Message content
message = client.messages.create(
    body='Hello, this is a test message from Python!',
    from_=from_number,
    to=to_number
)

print(f"Message sent with SID: {message.sid}")