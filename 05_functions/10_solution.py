# Create a recursive function to calculate the factorial of a number

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

print(factorial(79))