# write your code here
def heatwave(temperatures):
    count_25 = 0  # Counter for consecutive days >= 25°C
    count_30 = 0  # Counter for consecutive days >= 30°C
    
    for temp in temperatures:
        if temp >= 25:
            count_25 += 1
            if temp >= 30:
                count_30 += 1
        else:
            count_25 = 0  # Reset if temperature is below 25°C
            count_30 = 0
        
        # Check if we've found a valid heatwave
        if count_25 >= 5 and count_30 >= 3:
            return True
    
    return False
