def invest(amount, rate, goal):
    time = 0
    while amount < goal:
        amount += amount * rate/100
        time += 1
    return time
