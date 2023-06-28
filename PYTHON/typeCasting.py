# type casting = convert the data type of a value to another data type

# IN JS we can check the data type with the typeof operator

# int() = converts a string or a float to an integer
# float() = converts a string or an integer to a float
# str() = converts a string, integer or float to a string

x = 1  # int
y = 1.1  # float
z = "1"  # string

# convert from int to float:
a = float(x)
print(a)
print(type(a))

# convert from float to int:
b = int(y)
print(b)
print(type(b))

# convert string to int:
c = int(z)
print(c)
print(type(c))

# int and float into string
d = str(x)
print(d)
print(type(d))

# ---------------------------------------------------------------------------
# pratice example
# sum bouth strings

firstString = "5"
secondString = "5"

print(firstString + secondString)  # output: 55
# ! well we want to achive the real sum with the expected output: 10

# first we convert bouth strings into integers
firstNewString = int(firstString)
secondNewString = int(secondString)

# now we can sum the integers
print(firstNewString + secondNewString)  # output: 10
