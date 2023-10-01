"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input is not an integer: for example,when it is a decimal or a letter, a ValueError will be output.
2. When will a ZeroDivisionError occur?
When the denominator (dividend) input by the user is equal to 0, a ZeroDivisionError will be output.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

