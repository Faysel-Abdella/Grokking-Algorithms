def findTheSmallest(arr):
    # Assume the first item is the smallest
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index            

def selectionSort(unOrdered):
    ordered = []
    for i in range(len(unOrdered)):
        currentSmallIndex = findTheSmallest(unOrdered)
        ordered.append(unOrdered.pop(currentSmallIndex))
    return ordered

print(selectionSort([4,8,1,3,2,10,9,3]))    


