# write your code here
def hours(duration):
    h = duration//3600
    return h

def minutes(duration):
    h = hours(duration)
    m = duration - 3600 * h
    return m // 60

def seconds(duration):
    h = hours(duration)
    duration = duration - 3600 * h
    m = minutes(duration)
    duration = duration - m * 60
    return duration
print(seconds(30))
