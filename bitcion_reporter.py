import requests
import time

# global variables
api_key = '7753f933-be78-484b-8b63-c339f7576d9b'
bot_key = '5015569006:AAFABMg-lD93h-m7c0xq7DVAPDky69zcII4'
chat_id = '1054043832'
limit = 50000
time_interval = 30


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    respons = requests.get(url, headers=headers, params=parameters).json()
    btc_price = respons['data'][0]['quote']['USD']['price']
    return btc_price


print(get_price())


def send_msg(msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    index = 0
    while index <= 5:
        price = get_price()
        print(price)
        if price < limit:
            send_msg(f"yaaa khali l bitcoin raho hbat ta7t 50k raho ydir : {price}")
            time.sleep(time_interval)
        index += 1


main()
