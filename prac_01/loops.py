#a.
for a in range(0, 105, 10):
    print(a, end=' ')
print()
#b
for b in range(20, 0, -1):
    print(b, end=' ')
print()
#c
c = int(input("Number of stars"))
for _ in range(c):
    print('*', end=' ')
print()
#d
d = int(input("Enter the number of lines: "))
if d < 0:
    print("Invalid input.")
else:
    for d in range(1, d + 1):
        print('*' * d)
