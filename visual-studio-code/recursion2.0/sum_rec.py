def sum_rec(n):
    #base case
    if n == 3:
        return n
    return sum_rec(n+1) + n


result = sum_rec(1)
print(result)

def sum_rec_2(n):
    if n == 1:
        return n
    return sum_rec_2(n-1)  + n

result = sum_rec_2(3)
print(result)