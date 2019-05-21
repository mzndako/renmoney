
# Insertion sorting algorithm works by iterating through an array and sorting elements in a linear fashion.
# It can sort an unsorted array in a worst case time of O(N^2) time.
# If the array is already sorted, it has time complexity of O(N) 

def insertionSort(myList):
    # loop through every element in the array
    for index in range(1, len(myList)):
        # Get the current value of the element at the current index 'position'
        current = myList[index] 
        position = index

        # Compare the the previous value(s) with the current and swap if greather than current value 
        while position > 0 and myList[position-1] > current:
            # Swap the previous value with the value at index 'position'
            myList[position] = myList[position-1]
            # Reduce the position so that we can compare the value at that index against the current value again
            position -= 1
        # Let the current value (current) be at the last know position
        myList[position] = current

    # Return the sorted array
    return myList

unsortedArray = [4, 22, 100, 2, 3, 4, 2]
sortedArray = insertionSort(unsortedArray)
print(sortedArray)