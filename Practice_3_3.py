ln = int(input("Enter the length of the array: "))
ar1 = ar2 = []
for i in range(ln):
    ar1.append(int(input("Enter numers: ")))

    if ln == len(ar1):
        ar2 = ar1.copy()
        ar1.sort()
        if ar1 == ar2:
            print("list is sorted >>> ", ar2)
        else:
            print("list is not sorted", ar2)
        break
