# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'MESSAGES' contains the loaded messages as a Python dictionary

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculation():

    # Ask the user for the first and second number
    prompt(MESSAGES['what_first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['what_second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['what_operation'])
    operation = input()

    # ["1", "2", "3", "4"]
    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['incorrect_operation'])
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
        

    prompt(f'The result is {result}')


should_continue = True
prompt(MESSAGES['welcome'])

while should_continue:
    calculation()
    prompt(MESSAGES['continue_question'])
    user_choice = input()

    if user_choice == '1':
        should_continue = True
    else:
        should_continue = False

