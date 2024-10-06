# write your code here
def coins(amount):
    a = amount//5
    return a


def coins(amount):
    # 5 coins
    coin5 = amount//5
    amount -= coin5 * 5
    # 2 coins
    coin2 = amount//2
    amount -= coin2 * 2
    # 1 coins
    coin1 = amount
    # berekening
    coins_needed = coin1 + coin2 + coin5

    return coins_needed
print(coins(9))
