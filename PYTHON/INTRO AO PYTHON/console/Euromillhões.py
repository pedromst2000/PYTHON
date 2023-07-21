import random

numbers = []
stars = []

def generateNumber():
    return random.randint(1, 50)

def generateStars():
    return random.randint(1, 5)

for i in range(5):
    while len(numbers) < 5:
        newNumber = generateNumber()
        if newNumber in numbers:
            pass
        else:
            numbers.append(newNumber)

for i in range(2):
    while len(stars) < 2:
        newStar = generateStars()
        if newStar in stars or newStar in numbers:
            pass
        else:
            stars.append(newStar)

joinedKeys = numbers + stars
fullKey = "".join(str(joinedKeys))
    
print(f"A sua chave de euromilhoes é: {fullKey}")
