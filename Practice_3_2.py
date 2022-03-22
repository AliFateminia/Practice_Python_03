import random
n = int(input("Enter the length of the array: "))
c = True
lst = []
while c:
    num = random.randint(0, n * 10)
    if num not in lst:
        lst.append(num)
    if len(lst) == n:
        break
print("array :", lst)
print("array length: ", len(lst))
