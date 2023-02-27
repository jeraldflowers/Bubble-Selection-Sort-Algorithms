# 1. Begin to make comparisons of adjacent elements
# 2. Repeat until you have a complete pass without any swap

def bubbleSort(array):
    n = len(array)
    changes = 1
    for i in range(n):
        print(array)
        changes = 0
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                changes = 1
                if changes < 1:
                    break

array = [190, 1200, 1, 2, 3, 55, 1000, 6, 800, -20]
bubbleSort(array)

print("The sorted array of ascending form is: ")
for i in range(len(array)):
    print("%d"%array[i])