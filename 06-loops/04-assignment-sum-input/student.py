# write your code here
def sum_input():
    total = 0 
    number = int(input("Enter integer: "))
    
    while number != 0: 
        total += number
        number = int(input("Enter intiger: "))
    print(f"The sum equals {total}.")