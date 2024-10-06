# write your code here
from math import ceil
def internet_costs(duration_in_seconds, cost_per_block):

    time = ceil(duration_in_seconds/360)
    final_cost = time * cost_per_block
    return final_cost

print(internet_costs(720, 0.5))
