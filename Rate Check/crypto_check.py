import requests, json, time
import conf
from boltiot import Bolt

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

def get_bitcoin_rate():
	URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
	response = requests.request("GET", URL)
	response = json.loads(response.text)
	current_price = response["USD"]
	return current_price

bitcoin_rate = get_bitcoin_rate()
checkOne = False

def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False

while True:
	if checkOne == False:
		print("\n\nNew session started:\n")
		message = "The new session is started. Bitcoin rate is: " + str(bitcoin_rate)
		telegram_status = send_telegram_message(message)
		print("This is the Telegram Status: ", str(telegram_status) + "\n")
		checkOne = True
	else:
		new_bitcoin_rate = get_bitcoin_rate()
		if (new_bitcoin_rate >= bitcoin_rate):
			message = "Yay! BTC rate is not decreased. Bitcoin rate is: " + str(new_bitcoin_rate)
			telegram_status = send_telegram_message(message)
			print("This is the Telegram Status: ", str(telegram_status) + "\n")
			bitcoin_rate = new_bitcoin_rate
		else:
			message = "Attention! BTC rate is decreased. Bitcoin rate is: " + str(new_bitcoin_rate)
			telegram_status = send_telegram_message(message)
			print("This is the Telegram Status: ", telegram_status)
			response = mybolt.digitalWrite('0', 'HIGH')
			print(response + "\n")
			time.sleep(5)
			response = mybolt.digitalWrite('0', 'LOW')
			print(response + "\n")
			bitcoin_rate = new_bitcoin_rate
	time.sleep(30)