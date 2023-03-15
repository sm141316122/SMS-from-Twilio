from twilio.rest import Client


account_sid = "ACffcda66b1c47c83468df800b08ed955e"
auth_token = "0e40ebc74a937994b0ef2a3584da810e"


client = Client(account_sid, auth_token)

message = client.messages.create(
	from_="+15406607654",
	to="+886975505680",
	body="哈囉, 這是簡訊程式測試"
	)

print(message.sid)