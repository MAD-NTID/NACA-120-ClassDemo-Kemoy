def sum_rec(n):

    #base cases
    if n < 1:
        return 0
    if n == 1:
        return 1
    
    #recursive case = n-1
    return n + sum_rec(n-1)
    

result = sum_rec(-2222)
print(result)
result = sum_rec(10)
print(result)