# white a function that takes variable number of agruments and retuns their sum

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))