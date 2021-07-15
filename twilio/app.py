from twilio.rest import Client

account_sid = "ACc2077bfab0ed9b07bb54b91d238e76f0"
auth_token = "9091d2bfc3c1427fc60d2562e37dd845"

Client = Client(account_sid,auth_token)

call = Client.messages.create(
    to="+919534700465",
    from_="+18647724911",
    body = "hello"
 )