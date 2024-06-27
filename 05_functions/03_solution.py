# Polymorphism in Function

# write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a*b;

print(multiply(2, 3))           # 6
print(multiply('a', 3))         # aaa
print(multiply(2, 'a'))         # aa