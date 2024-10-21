#!/usr/bin/env py

# def tip_calculator():
#     #recive total price
#     total_price = float(input('total price'))
#     #tip percentage default 20
#     tip_input = input('tip percentage')


#     if tip_input == '':
#         tip_percentage = 20
#     else:
#         float(tip_input)
#         tip_percentage = tip_input

    
#     total_amount = round(total_price * (1 + tip_percentage/100))

#     print(f'you have to pay {total_amount}')



    # tip_price = total_price % tip_percentage 
    # payment = tip_price + total_price
    # return f'{payment}'


def tip_calculator():
    try:
        # Get the total price from the user
        total_price = float(input("Enter total price: "))

        # Get the tip percentage, allowing for a default of 20% if input is empty
        tip_input = input("Enter tip percentage (default=20): ")
        tip_percentage = 20 if tip_input == '' else float(tip_input)

        # Calculate the total amount to be paid
        total_amount = round(total_price * (1 + tip_percentage / 100))

        # Display the result
        print(f"You have to pay {total_amount}")
    
    except ValueError:
        print("Please enter valid numbers for price and tip percentage.")


