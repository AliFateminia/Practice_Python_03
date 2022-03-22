ln = int(input("Enter the length of the snake: "))
b = ''
j = 0
for i in range(ln):
    if (i % 2) == 0:
        b = b + "*"
        j += 1
    if (i % 2) != 0:
        b = b + "#"
        j = j - 1
print(b)
