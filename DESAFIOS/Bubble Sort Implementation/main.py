# The Bubble Sort algorithm in Python. Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
#compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. 

numbers = []

# function to swap the order of two elements in the list
def swap(i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp

# function to sort the list using bubble sort
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                swap(j, j+1)


def main():

    # valdidations for the user inputs
    try:
      n = int(input("Enter the number of elements you want to sort: "))
      if n < 0:
        print("Please enter a positive number")
        n = int(input("Enter the number of elements you want to sort: "))
    except ValueError:
        print("Please enter a number")
        n = int(input("Enter the number of elements you want to sort: "))

    # ask the user to enter the elements of the list
    # check if the input is a number
    for i in range(0, n):
        try:
            element = int(input("Enter element: "))
            numbers.append(element)
        except ValueError:
            print("Please enter a number")
            element = int(input("Enter element: "))
            numbers.append(element) 

    bubbleSort(numbers)       

    # print the sorted list
    print(f'Sorted array:{numbers}')
    

main()