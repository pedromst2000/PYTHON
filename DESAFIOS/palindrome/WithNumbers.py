
def palindrome(number):

    # convert number to string
    number = str(number)

    # reverse the string
    reverseNumber = number[::-1]

    # check if the number is palindrome
    if number == reverseNumber:
        return True
    return False



print(palindrome(2002)) # True
print(palindrome(2012)) # False
