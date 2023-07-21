def count_and_biggest(numbers):
    count = {}
    # LOOKS IF THE NUMBER EXISTS IN THE DICTIONARY. IF IT DOESEN'T IT ADDS IT AS A KEY AND ASIGNS 1 AS ITS VALUE(NUMBER APPEARS ONCE) IF IT EXISTS IT GOES TO ITS KEY AND ADS 1 TO THE VALUE (IT HAS A DUPLICATE)
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            # SORTS THE LIST IN REVERSE SO THAT THE FIRST TWO ELEMENTS ARE THE BIGGEST ONES
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    two_biggest = sorted_count[:2]
    return count, two_biggest

numbers = [1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 1, 9, 9, 9]
count, two_biggest = count_and_biggest(numbers)
print("Count:", count)
print("Two biggest:", two_biggest)
