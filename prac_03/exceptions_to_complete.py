"""
CP1404 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
result = None  # Initialize result

while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        is_finished = True #If "is_finished" is True to exit the loop
    except ValueError:# TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)