import random

MAX_INCREASE = 0.175  # Updated to 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00  # Updated to $1.00
MAX_PRICE = 100.00  # Updated to $100.00
INITIAL_PRICE = 10.00

number_of_days = 0  # Added number_of_days variable
OUTPUT_FILE = "stock_prices.txt"  # Added output file name

price = INITIAL_PRICE

out_file = open(OUTPUT_FILE, 'w')  # Open the output file for writing

print(f"Starting price: ${price:.2f}", file=out_file)  # Output the starting price to the file

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # Generate a random integer of 1 or 2
    # If it's 1, the price increases, otherwise, it decreases
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1  # Increment the number of days
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)

out_file.close()  # Close the output file at the very end.
