# write your code here
def empty_seats(used_seats):
    used_seats = sorted(used_seats)

    empty_count = 0

    for i in range(len(used_seats) - 1):
           empty_count += (used_seats[i + 1] - used_seats[i] - 1)
    
    return empty_count

