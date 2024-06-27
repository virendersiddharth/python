# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args);
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"function name is : {func.__name__} Value of args : {args_value if args_value else 0} and value of kwargs : {kwargs_value if kwargs_value else 0}")
        return result
    return wrapper

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}")


greet("vihaan", greeting="Hey")
greet("Siddharth", "Hi")