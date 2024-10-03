from math import ceil
# write your code here
def buses_needed(people_count, bus_capacity):
    # bus capacity: 10
    # people: 20
    return (ceil(people_count / bus_capacity))


#print (buses_needed(x,y)) 
buses_needed(20, 10)
print(buses_needed(24, 10))
