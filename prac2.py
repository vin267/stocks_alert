import requests
import time

# global variables
api_key = '64be8b4c-32e1-48a7-84ab-dac90dab2536'
bot_token = '1889572236:AAHbRsYeVZge5axBj9by5xrXx-Aw9pvDklI'
chat_id = '1886817846'
threshold = 40000
time_interval = 30  # in seconds


def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

print(get_btc_price())


# fn to send_message through telegram
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    # send the msg
    requests.get(url)


# main fn
def main():
    price_list = []

    # infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)

        # if the price falls below threshold, send an immediate msg
        if price < threshold:
            send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price}')


        # fetch the price for every dash minutes
        time.sleep(time_interval)


# fancy way to activate the main() function
if __name__ == '__main__':
    main()



