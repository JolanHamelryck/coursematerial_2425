# write your code here
import math

def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        base_price = 10
    elif duration <= 120:
        base_price = 11
    elif duration <= 150:
        base_price = 12
    else:
        base_price = 15

    if imax:
        base_price *= 1.2 
        base_price = math.ceil(base_price) 
    if student:
        base_price -= 3
    
    base_price = max(base_price, 0)

    total_cost = base_price * ticket_count
    return total_cost