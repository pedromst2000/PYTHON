# Reverse String Challenge and then checking if is palindrome

# Output 
# osso
# osso is palindrome

# input
print()
stringInput = str(input("Insert a string: "))


def reverseString(string):
    return string[::-1]

def isPalindrome(string):
    if string == reverseString(string):
        return True
    else:
        return False
    

print(reverseString(stringInput))
# ternary operator
# condition_if_true if condition else condition_if_false
print(f"{stringInput} is palindrome" if isPalindrome(stringInput) else f"{stringInput} is not palindrome")