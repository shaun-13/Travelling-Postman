from flask import Flask
app = Flask(__name__)

import requests

@app.route("/")
def telegram_bot_sendtext():
    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    bot_chatID = '410414385'
    # to retrieve payment_amount from input and automatically add
    bot_message = "You have successfully register for your preorder."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()