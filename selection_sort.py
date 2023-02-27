# 1. Find the smallest element in my array
# 2. Create two subarrays to keep track of our algorithm
# 3. Print the sort result

import sys
array = [5, 21, 6, 1000, 54, -3, -6, 78, 102, 100, 0, 3, 2]

def selectionSort(array):
    # loop through our entire array
    for i in range(len(array)):
        print(array)
        # find the minimum value remaining inside our unordered array
        idxDes = i 
        for j in range(i+1, len(array)):
            if array[idxDes] > array[j]:
                idxDes = j

        # Since we found the minimum element we are going to change it
        # to the first value of our unordered array.
        array[i], array[idxDes] = array[idxDes], array[i]

selectionSort(array)
print("Sorted array: ")
for i in range(len(array)):
    print("%d"%array[i])
