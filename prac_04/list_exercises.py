# Initialize an empty list to store numbers
# Prompt the user for 5 numbers and add them to the list
numbers = []
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

# Output information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average:.1f}")

user_names= input("enter your name:")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn','Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
if user_names in usernames:
    print("Access granted")
else:
    print("Access denied")