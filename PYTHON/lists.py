# list => used to store multiple items in a single variable

import os
food = ["pizza", "hamburger", "hotdog", "fries", "soda", "chips"]

# print("i would like to eat {} with {}".format(food[1], food[4]))

print(food[-1])  # to acess the last position

# changing the values of a list

food[1] = "chicken"
food[4] = "water"

print("i would like to eat {} with {}".format(food[1], food[4]))

# some methods of a list

# food.append("ice cream")  # to add an item to the list
# food.remove("chips")  # to remove an item from the list
# food.pop()  # to remove the last item from the list
# food.insert(1, "chips")  # to insert an item in a specific position
# food.sort()  # to sort the list in alphabetical order
# food.reverse()  # to reverse the list
# food.clear()  # to clear the list
# food.copy()  # to copy the list
# food.count("chips")  # to count the number of times an item appears in the list
# food.index("chips")  # to find the index of an item in the list
# food.extend("chips")  # to add multiple items to the list

# ---------------------------------------------------------------------------------------------
# 2D lists

# to achieve this multidimensional list, we need to create a list inside another list
# food = [["pizza", "hamburger", "hotdog", "fries", "soda", "chips"], ["ice cream", "cake", "brownie", "cookies", "candy", "chocolate"]]

# create a list for each food type
# lunch = ["pizza", "hamburger", "hotdog", "fries", "chips"]
# drinks = ["soda", "water", "juice", "milk", "coffee"]
# dessert = ["ice cream", "cake", "brownie", "cookies", "candy"]

# # now we join all lists in once list called food
# food = [lunch, drinks, dessert]

# print(food)

# # acessing the items of a 2D list
# print("For lunch i would like to eat {}. For drinks i can take {}, and finally"
# "for dessert i would like to eat {}".format(food[0][1], food[1][1], food[2][1]))

# ---------------------------------------------------------------------------------------------
# Tuples

# tuples are like lists, but they are immutable, which means that they cannot be changed
# tuples are created using parenthesis instead of square brackets

# food = ("pizza", "hamburger", "hotdog", "fries", "soda", "chips")

# print(food.count("chips"))  # to count the number of times an item appears in the list
# print(food.index("chips"))  # to find the index of an item in the list

# # search for an item in a tuple

# search = input("what would you like to search for? ")

# if search in food:
#     print("yes, {} is in the tuple".format(search))
# else: # search not in food
#     print("no, {} is not in the tuple".format(search))

# ---------------------------------------------------------------------------------------------
# Sets

# sets are like lists, but they are unordered and unindexed! no duplicates are allowed

# carsBrand = {"ford", "chevy", "dodge", "honda", "toyota"}

# motosBrand = {"honda", "yamaha", "suzuki", "kawasaki"}

# # carsBrand.add("bmw")  # to add an item to the set
# # carsBrand.remove("ford")  # to remove an item from the set
# # carsBrand.clear()  # to clear the set
# # carsBrand.update(motosBrand)  # to add multiple items to the set

# # brands = carsBrand.union(motosBrand)  # to join two sets

# # difference between two sets

# print(carsBrand.difference(motosBrand)) # to return what they don´t have in common
# print(carsBrand.intersection(motosBrand)) # to return what they have in common

# ---------------------------------------------------------------------------------------------
# Dictionaries

# dictionaries are used to store data values in key:value pairs

# simmiliar to Objects in JS

countries = {"Portugal": "Lisbon", "Spain": "Madrid",
             "France": "Paris", "Germany": "Berlin"}


print(countries["Portugal"])  # to acess the value of a key => Lisbon
# with the get method we can acess the value of a key without getting an error
print(countries.get("Portugal"))  # to acess the value of a key => Lisbon
#print keys of a dictionary
print(countries.keys())
#print values of a dictionary
print(countries.values())
#print items of a dictionary
print(countries.items())
# to change the value of a key
countries["Portugal"] = "Lisboa"
# to add a new key:value pair
countries["Italy"] = "Rome"
# to remove a key:value pair
countries.pop("Italy")
# to remove the last item of a dictionary
countries.popitem()
# to clear the dictionary
countries.clear()
# to copy the dictionary
countries.copy()
# to get the length of a dictionary
print(len(countries))
# to update a dictionary
countries.update({"Portugal": "Lisboa", "Italy": "Rome"})
# to delete a dictionary
del countries

# to search for a key in a dictionary
searchDict = input("What capital country would you like to search for? ")
if searchDict in countries:
    print("The capital of {} is {}".format(
        searchDict, countries.get(searchDict)))
elif searchDict not in countries:
    print("Sorry, {} is not in our database".format(searchDict))


# ---------------------------------------------------------------------------------------------

op = ""

while True:
    op = input("Would you like to search for a capital? (Y/N) ")

    if op == "Y" or op == "y":
        searchDict = input(
            "What capital country would you like to search for? ")
        # os.system("cls")
        if searchDict in countries:
            print("The capital of {} is {}".format(
                searchDict, countries.get(searchDict)))
        elif searchDict not in countries:
            print("Sorry, {} is not in our database".format(searchDict))

    elif op == "N" or op == "n":
        # os.system("cls")
        break
