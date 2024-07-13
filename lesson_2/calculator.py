# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt('Welcome to Calculator!')

# Ask the user for the first and second number
prompt("What's the first number?: ")
number1 = input()

while invalid_number(number1):
    (prompt("hmm...that's not a valid number."))
    number1 = input()

prompt("What's the second number?: ")
number2 = input()

while invalid_number(number2):
    (prompt("hmm...that's not a valid number."))
    number2 = input()

prompt('What operation would you like to perform?\n'
    '1) Add 2) Subtract 3) Multiply 4) Divide: ')
operation = input()

# ["1", "2", "3", "4"]
while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()
    
match operation:    
    case '1': # 1 represents addition
        result = int(number1) + int(number2)
    case '2': # 2 represents subtraction
        result = int(number1) - int(number2)
    case '3': # 3 represents multiplication
        result = int(number1) * int(number2)
    case '4': # 4 represents division
        result = int(number1) / int(number2)
    case _:
        print('Incorrect operation choice...')
    
prompt(f'The result is {result}')