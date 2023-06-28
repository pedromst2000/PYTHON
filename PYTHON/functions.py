# functions => functions in python 
# are defined using the keyword def and can take any number of arguments

# string format => template strings in JS

# example

def sum(a, b):
  return print(a + b)

num1 = int(input("Indique um número: "))
num2 = int(input("Indique um número: "))

sum(num1, num2)

def names(firstName, secondName):
    return print("Hello {} and {} Nice to meet you bouth!!" .format(firstName, secondName))

names("Lara", "Pedro")

def findTheGreatestNumber(num1, num2, num3, num4) :
    return print("o maior número é: {}" .format(max(num1, num2, num3, num4)))

findTheGreatestNumber(1, 2, 3, 4)

def multiply(num1, num2):
    result = num1 * num2
    return result

res = ("{1} X {0} = {2}" .format(4, 2, multiply(4, 2)))

print(res)

# keyword arguments => arguments that are passed to a function in a specific order

def fullName(firstName, lastName):
    return 'My name is {} {}'.format(firstName, lastName)


name = fullName(lastName="Pedro", firstName="Teixeira")

print(name)

# *args => pass multiple arguments to a function
def multiply(*nums):
    total = 1
    for num in nums:
        total *= num
    return total


multiplyNumbers = multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(multiplyNumbers)


