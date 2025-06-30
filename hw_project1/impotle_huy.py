# my_int = 1
# import json

# print(globals().keys())

# #
# import random

# my_list = [1, 2, 3]

# print(random.choice(my_list))
# print(globals().keys())

# #
# from Ruletka import flip_coin, simulate_martingale_for_n_players

# print(simulate_martingale_for_n_players)
# print(flip_coin)

# #
# import requests
# url = 'https://api.binance.com/api/v3/ticker/price'

# response = requests.get(url, params={'simbol': 'BTCUSDT'})

# price = response.json()

# content = response.content
# print(price)
# print(content)
# print(type(content))

# #
# import requests
# import time

# url = 'https://api.binance.com/api/v3/ticker/price'

# bitcoin_prices = []
# for i in range(30):
#     response = requests.get(url, params={'simbol': 'BTCUSDT'})
#     price = float(response.json()["price"])
#     # bitcoin_prices.append(price) 
#     time.sleep(5)

# print(bitcoin_prices)
# print(len(bitcoin_prices))
# print(max(bitcoin_prices))
# print(min(bitcoin_prices))

# # #
# import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/posts/1')

# print(
#     response.json()
# )

#
import httpx

body = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/posts", data=body)

print(response.json())

# curl --location --request POST 'https://jsonplaceholder.typicode.com/posts' \
# --header 'Content-type: application/json; charset=UTF-8' \
# --data '{
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }'