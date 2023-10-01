# Task 4: Read and sum all numbers from "numbers. txt"
total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

print(f"The total sum of all numbers in the file is {total}")
