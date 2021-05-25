import requests
import time
from yahoo_fin import stock_info as si

# global variables
# api_key = 'OCN9UXR7UQPVI3TZ'
bot_token = '1889572236:AAHbRsYeVZge5axBj9by5xrXx-Aw9pvDklI'
chat_id = '1886817846'
threshold_buy = {
    'ACB': 10,
    'DSS': 6,
    'BCLI': 2
}

Stock_ls = ['ACB','TSLA','BCLI','DSS']

thresh_list = []
for i in threshold_buy:
    thresh_list.append(threshold_buy[i])
print("thresh list: ", thresh_list)

thresh_name_ls = []
for i in threshold_buy:
    thresh_name_ls.append(i)
print("thresh name: ",thresh_name_ls)

threshold_sell = {
    'TSLA': 550,
    'ACB': 14,
    'DSS': 6,
    'BCLI': 6,
    'IDRA': 1
}

thresh_sell_ls = []
for i in threshold_sell:
    thresh_sell_ls.append(threshold_sell[i])
print("thresh sell ls: ",thresh_sell_ls)

thresh_sell_name_ls = []
for i in threshold_sell:
    thresh_sell_name_ls.append(i)
print("threshname sell: ",thresh_sell_name_ls)

time_interval = 100  # in seconds


current_price_buy_list = []
def get_current_price_buy():
    for i in threshold_buy:
        print("names: ",i)
        current_price = si.get_live_price(i)
        current_price_buy_list.append(current_price)
    return "current price: ", current_price_buy_list
print(get_current_price_buy())

current_price_sell_list = []
def get_current_price_sell():
    for i in threshold_sell:
        print("names: ",i)
        current_price = si.get_live_price(i)
        current_price_sell_list.append(current_price)
    return "current price: ", current_price_sell_list
print(get_current_price_sell())

# fn to send_message through telegram
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    # send the msg
    requests.get(url)

# main fn
def main():
    while True:
        current_buy = dict(zip(thresh_name_ls, current_price_buy_list))
        for key in current_buy:
            if current_buy[key] < threshold_buy[key]:
                send_message(chat_id=chat_id, msg=f'STOCKS Price Buy Drop Alert {key}: {current_buy[key]}')

        current_sell = dict(zip(thresh_sell_name_ls, current_price_sell_list))
        for i in current_sell:
            if current_sell[i] > threshold_sell[i]:
                send_message(chat_id=chat_id, msg=f'STOCKS Price Sell Drop Alert {i}: {current_sell[i]}')

        # fetch the price for every dash minutes
        time.sleep(time_interval)
main()
