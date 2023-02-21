from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
vs_currencies = "usd"


# print(cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=vs_currencies))
#
# coins_list = cg.get_coins_list()
#
# for n, item in enumerate(coins_list):
#     info_crypto_item = f'{n+1}. id >> {item["id"]} | symbol >> {item["symbol"]} | name >> {item["name"]}'
#     print(info_crypto_item)

# coins_markets = cg.get_coins_markets(vs_currency=vs_currencies)
# for n, item in enumerate(coins_markets):
#     print(n, item)

nft_list = cg.get_nfts_list()

print(cg.get_search_trending())

print(cg.search("Pi"))



