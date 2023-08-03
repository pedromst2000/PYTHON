# nested loops => loops inside loops

# challenge => drawn a rectangle with nested loops
rows = int(input("Hom many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")


for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print() # print outer loop

# second challenge => obtain the follow output =>#0 x A
#                                                  0 x A
#                                                  0 x A
for i in range(3):
    for j in range(3):
        if j == 0:
            print("0", end=" ")
        elif j == 1:
            print("x", end=" ")
        else:
            print("A", end=" ")
    print()
