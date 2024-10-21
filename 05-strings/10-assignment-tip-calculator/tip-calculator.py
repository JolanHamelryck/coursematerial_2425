#!/usr/bin/env py

def tip_calculator():
    try:
        total_price = float(input("Enter total price: "))

        tip_input = input("Enter tip percentage (default=20): ")
        tip_percentage = 20 if tip_input == '' else float(tip_input)

        total_amount = round(total_price * (1 + tip_percentage / 100))


        print(f"You have to pay {total_amount}")
    
    except ValueError:
        print("Please enter valid numbers for price and tip percentage.")

def main():
    tip_calculator()

if __name__ == "__main__":
    main()
