n = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)