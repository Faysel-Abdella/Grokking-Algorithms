def count_size(arr):
    i = 1
    if arr == []:
        return 0
    else:
        return 1 + count_size(arr[i:]) 

print(count_size([1,2,3,4]))    
