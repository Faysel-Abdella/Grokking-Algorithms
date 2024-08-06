def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left_side = [i for i in arr[1:] if i <= pivot]
        right_side = [j for j in arr[1:] if j > pivot]
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort([0,2,7,1,3,0]))