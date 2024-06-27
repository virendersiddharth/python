# create a lambda function to compute the cube of a number

cube = lambda x: x ** 3

isEven = lambda x : x % 2 == 0

isPositive = lambda x : x >= 0

print(isPositive(-3))

print(isEven(6))

print(cube(4))