# Create a function taht takes two numbers as parameters and return their sum

# Function 
def sum_two_numbers(number1, number2):
    return number1 + number2;

# It will handle N number of arguments
def sum_two_numbers(*args):
    return sum(args)

result = sum_two_numbers(23, 21)
print(result)