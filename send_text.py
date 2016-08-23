from twilio.rest import TwilioRestClient

account_sid = "###" # Your Account SID from www.twilio.com/console
auth_token  = "###"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	body="Hey~!",
    to="+1###",    # Replace with your phone number
    from_="+1###") # Replace with your Twilio number

print(message.sid)