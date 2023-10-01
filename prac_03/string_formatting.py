name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# Format the output using f-strings
output = f"{year} {name} for about ${cost:,.2f}!"

print(output)

# Using a for loop with string formatting to produce the right-aligned numbers.
for i in range(0, 201, 50):
    print(f"{i:3}")
