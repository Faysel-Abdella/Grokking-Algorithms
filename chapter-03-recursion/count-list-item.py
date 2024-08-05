def count_size(arr):
    i = 0
    if arr == []:
        return 0
    else:
        i=+1
        return 1 + count_size(arr[i:]) 

print(count_size([]))    
