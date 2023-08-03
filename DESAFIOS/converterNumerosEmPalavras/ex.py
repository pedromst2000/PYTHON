# convert numbers to words
# eg: 123 -> one hundred and twenty three

import sys

def convert(num):
    # convert number to words
    # num: int
    # return: str
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'minus ' + convert(-num)
    else:
        return convert_pos(num)
    
def convert_pos(num):
    # convert positive number to words
    # num: int
    # return: str
    if num <= 19:
        return ones[num]
    elif num <= 99:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
    elif num <= 199:
        return 'one hundred' + (' and ' + convert_pos(num % 100) if num % 100 != 0 else '')
    elif num <= 999:
        return ones[num // 100] + ' hundred' + (' and ' + convert_pos(num % 100) if num % 100 != 0 else '')
    elif num <= 1999:
        return 'one thousand' + (' ' + convert_pos(num % 1000) if num % 1000 != 0 else '')
    elif num <= 999999:
        return convert_pos(num // 1000) + ' thousand' + (' ' + convert_pos(num % 1000) if num % 1000 != 0 else '')
    elif num <= 1999999:
        return 'one million' + (' ' + convert_pos(num % 1000000) if num % 1000000 != 0 else '')
    elif num <= 999999999:
        return convert_pos(num // 1000000) + ' million' + (' ' + convert_pos(num % 1000000) if num % 1000000 != 0 else '')
    elif num <= 1999999999:
        return 'one billion' + (' ' + convert_pos(num % 1000000000) if num % 1000000000 != 0 else '')
    else:
        return convert_pos(num // 1000000000) + ' billion' + (' ' + convert_pos(num % 1000000000) if num % 1000000000 != 0 else '')
    
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen']
tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']

print()
number = int(input('Insert a number: '))
print(f'{number} -> {convert(number)}')