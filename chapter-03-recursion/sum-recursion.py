def sum_to_1(num):
    if num == 1:
        return 1
    else:
        return num + sum_to_1(num - 1)
    
print(sum_to_1(5))     