# create a function that accepts any number of keyword arguments and prints them in the format key: value pairs.

def print_kwargs(**kwargs):
    print(kwargs) # Dictionary
    print(kwargs.items()) # List of Tuples
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Duniya", age = 25, city = "Bangalore")