###python program to find sum of integers in the string.

s1 = "1xyze764890"
total = 0

for i in s1:
    if i.isdigit():
        total += int(i)

print("Sum of all integers in the string:", total)
