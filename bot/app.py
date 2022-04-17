""""
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = "EAAJ9Jx5tHvoBAMssC7y3BTDja0rDEZBlWxZAH03Vi1fk2pFKW2XZBKwemSRadeisi8vZBJWcMIK2EFZBquMpHAXblCpWh9tyvkCgZBuMUTZAulmQMRYt6BtLI4ZCi9zj8LV99elccRh454mebjOkWBZCgxUmAbw9MIwfOZANOzcHcPKqiT9Ld7aPUZC"
VERIFY_TOKEN = "MYTESTINGTOKEN"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    elif request.method == 'POST':
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5000, debug=True)

"""""