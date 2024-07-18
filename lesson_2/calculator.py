# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

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
    prompt(messages('what_first_number', language))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number', language))
        number1 = input()

    prompt(messages('what_second_number', language))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number', language))
        number2 = input()

    prompt(messages('what_operation', language))
    operation = input()

    # ["1", "2", "3", "4"]
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('incorrect_operation', language))
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
        

    prompt(messages('result', language) + ' ' + str(result))


should_continue = True
language = 'es'

prompt(messages('welcome', language))

while should_continue:
    calculation()
    prompt(messages('continue_question', language))
    user_choice = input()

    while user_choice not in ['1', '2']:
        prompt(messages('invalid_continue', language))
        user_choice = input()
    
    if user_choice == '1':
            should_continue = True
    else:
            should_continue = False

