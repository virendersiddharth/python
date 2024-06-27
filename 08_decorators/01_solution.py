# Problem: Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function takes time to execute : ", end - start)
        return result
    return wrapper

@timer
def funA():
    time.sleep(4)
    print("Hello")


funA()
funA()