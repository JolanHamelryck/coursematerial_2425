def rpg2(n_sides, goal):
    total_combinations = 0
    good_combinations = 0 
    for die1 in range(1, n_sides + 1):
        for die2 in range(1, n_sides + 1):
            total_combinations += 1
            if die1 + die2 >= goal:
                good_combinations += 1 
    probability = good_combinations / total_combinations
    return probability
        
def rpg3(n_sides, goal):
    total_combinations = 0 
    good_combinations = 0
    for die1 in range(1, n_sides + 1):
        for die2 in range(1, n_sides + 1):
            for die3 in range(1, n_sides + 1):
                total_combinations += 1
                if die1 + die2 + die3 >= goal:
                    good_combinations += 1
    probability = good_combinations / total_combinations
    return probability
