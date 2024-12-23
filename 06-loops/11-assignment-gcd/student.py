def gcd(x, y):
    x, y = abs(x), abs(y)
    
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
    return
