
op = ""

while True:
    name = input("Enter your name: ")
    try:
        if name.isalpha() == False or name.isnumeric() == True:
            raise NameError
        else:
            print("Hello", name)
            op = input("Do you want to insert other name? (y/n): ")
            if op == "y" or op == "Y":
                continue
            else:
                break 
    except NameError:
        print("That's not a name!")
        continue

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

    if result == 0:
        raise ZeroDivisionError
    else:
        print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")