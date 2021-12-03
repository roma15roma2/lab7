def sum_list(x):
    total = 0
    for number in x:
        total = total + number
    return total


l = [1,10,20,30]
s = sum_list(l)
print(s)
