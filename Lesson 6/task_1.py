def join_dict(x, y):
    join_dict_1 = dict(zip(x, y))
    return join_dict_1
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print(join_dict(coin, code))