list1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
list2 = [1, 3, 5, 7, 14, 18, 21, 7, 9 , 8]

duplicateAmount = 0
duplicateNumber = []

for i in list1:
    for j in list2:
        if i == j:
            duplicateAmount += 1
            duplicateNumber.append(i)

duplicateString = ", ".join(map(str, duplicateNumber))

print(f"existem {duplicateAmount} elementos da lista 1 que se repetem na lista 2: {duplicateString}")
