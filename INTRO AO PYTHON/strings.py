# strings methods

fullName = "PedroTeixeira"

# basic methods
# print(fullName)
print(len(fullName))
print(fullName.find("r"))
print(fullName.capitalize())
print(fullName.upper())
print(fullName.lower())
# but "123" will return true since is digit number in string
print(fullName.isdigit())
print(fullName.isalpha())
print(fullName.count("e"))
print(fullName.replace("e", "a"))
print(fullName*2)
print(fullName.index("i"))

# ---------------------------------------------------------------------------
# SLICE METHODS
# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

fullName = "Pedro Teixeira"

print(fullName[:5])  # will slice from index 0 to 5 (not including 5)
print(fullName[5:])  # will slice from index 5 to the end
# # reverse string
print(fullName[::-1])

# slice function
# slice(begin, -end) => begin => positive | end => reverse couting with negative

# reverse string with for loop


def reverseString(string):
    # reverse string with for loop
    reversedString = ""
    for i in range(len(string)-1, -1, -1):
        reversedString += string[i]
    return reversedString


str = input("Indique uma string: ")

print(reverseString(str))

# # reverse string with slice method


def reverseString(string):
    return string[::-1]


print(reverseString("alo"))


def upperCaseOdd(string):
    # upper case odd characters
    for i in range(len(string)):
        if i % 2 == 0:
            # will slice only the odd characters and upper case them and finally returning the new string
            string = string[:i] + string[i].upper() + string[i+1:]
    return string


print(upperCaseOdd("Pedro"))


text = "O rato roeu a roupa do rei de roma"

# #count vowels
vowels = "aeiou"
count = 1
for i in text:
    if i in vowels:
        count += 1
print(count)

# #count consonants
consonants = "bcdfghjklmnpqrstvwxyz"
count = 0
for i in text:
    if i in consonants:
        count += 1
print(count)

# get this output => "O rato roeu de roma" => remove the word "a roupa do rei"
# remove the word "a roupa do rei"
newText = text[:text.find("a roupa do rei")] + text[text.find("de roma"):]
print(newText)

name = "Pedro Miguel da Silva Teixeira"
newName = name[:name.find("Miguel da Silva")] + name[name.find("Teixeira"):]
print(newName)
