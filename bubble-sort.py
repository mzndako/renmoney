# Bubble sort works by constantly iterating through an unsorted array 
# and swapping values within that array until such times as no swaps 
# are made within a full pass through the array

def bubbleSort(arr): 
    n = len(arr) # Get the length of the array

    # Loop through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

array = [44, 23, 1, 45, 5, 100]
bubbleSort(array)
print (array)