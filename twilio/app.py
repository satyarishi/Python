from twilio.rest import Client

account_sid = "69"
auth_token = "69"

Client = Client(account_sid,auth_token)

call = Client.messages.create(
    to="+919534700465",
    from_="+18647724911",
    body = "hello"
 )
