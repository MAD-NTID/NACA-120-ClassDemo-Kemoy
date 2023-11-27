def sum_loop(n):
    result = 0
    for num in range(1,n+1):
        result+=num
    
    return result

res = sum_loop(10)
print(f"The loop sum is {res}")