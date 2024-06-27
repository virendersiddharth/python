# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function

import time

def cache(func):
    cache_value = {}
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        return result
    return wrapper
    
@cache
def long_function_running(a, b):
    time.sleep(4)
    return (a+b)

print(long_function_running(2,3))
print(long_function_running(2,3))
print(long_function_running(2,7))
print(long_function_running(2,3))