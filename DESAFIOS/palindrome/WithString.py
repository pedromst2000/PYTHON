import re


def palindrome(str):

    # Remove all non-alphanumeric characters
    str = re.sub(r'[^A-Za-z0-9]', "", str)

    # Convert all characters to lowercase
    str = str.lower()

    reverseString = str[::-1]

    if str == reverseString:
        return True
    return False


print(palindrome("osso"))
