number_items = int(input("Number of items:"))
while number_items<0:
    print("Invalid input.")
    number_items = int(input("Number of items:"))
total_price=0
for i in range(number_items):
    item_price = int(input("Price of item:"))
    total_price += item_price

if total_price >100:
    total_price *=0.9

print(f"{number_items}items price are ${total_price}")

