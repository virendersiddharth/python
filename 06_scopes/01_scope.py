username = "virender"

def func():
    # username = "siddharth"
    print(username)


print(username) 
func()


x = 98

# def func2(y):
#     z = x+y
#     return z

# print(func2(10))

# def func3():
#     # Avoid global changes into the function
#     global x
#     x = 88

# func3()
# print(x);



# Closures
def func4():
    x = 78
    def func5():
        print(x)
    return func5
result = func4()
result()


def code(num):
    def code2(x):
        return x ** num
    return code2
result2 = code(2)
result3 = code(3)

print(result2(3))
print(result3(3))

