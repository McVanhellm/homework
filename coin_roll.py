from coin import Coin
coin = Coin()
results = []
for i in range(100):
    result = coin.roll()
    if result == 1:
        results.append('орел')
    else:
        results.append('решка')
print(results)