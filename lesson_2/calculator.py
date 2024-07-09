# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')

# Ask the user for the first and second number
number1 = input("What's the first number?: ")
number2 = input("What's the second number?: ")

operation = input('What operation would you like to perform?\n'
    '1) Add 2) Subtract 3) Multiply 4) Divide: ')
    
if operation == '1': # 1 represents addition
    result = int(number1) + int(number2)
elif operation == '2': # 2 represents subtraction
    result = int(number1) - int(number2)
elif operation == '3': # 3 represents multiplication
    result = int(number1) * int(number2)
elif operation == '4': # 4 represents division
    result = int(number1) / int(number2)
else:
    print('Incorrect operation choice...')
    
print(f'The result is {result}')