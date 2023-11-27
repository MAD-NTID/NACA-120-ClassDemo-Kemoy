def sum_rec(n):
    #base case
    if n == 10:
        return 10
    
    #recursive case is n+1
    return n + sum_rec(n+1)

result = sum_rec(1)

print(f"The sum is {result}")