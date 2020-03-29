import requests 
# python need to pip install requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def telegram_bot_sendtext():
    
    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    bot_chatID = '158059877'
    payment_amount = '32'
    # to retrieve payment_amount from input and automatically add
    bot_message = "You have successfully paid SGD" + payment_amount + " for your preorder via Paypal."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

# test = telegram_bot_sendtext()
# print(test)

# https://api.telegram.org/bot1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s/getUpdates
# mychatid: 410414385
# jychatid: 158059877