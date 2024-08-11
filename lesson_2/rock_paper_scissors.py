import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_CHOICES_SHORT = {'r': 'rock', 'p': 'paper', 's': 'scissors',
                       'l': 'lizard', 'sp': 'spock'}
WIN_CONDITIONS = [['r', 's'], ['p', 'r']]
def prompt(message):
    print(f'==> {message}')

def welcome_message():
    prompt('Welcome to "Rock, Paper, Scissors, Lizard, Spock!"')

def is_valid_choice(choice):
    if choice.startswith('r') or choice.startswith('p') or \
        choice.startswith('s') or choice.startswith('l'):
        return True
    else:
        return False

def calculate_player_choice(choice):
    player_choice = ''

    rock_choice = is_rock_choice(choice)
    if rock_choice == True:
        player_choice = 'rock'
        return player_choice
    
    paper_choice = is_paper_choice(choice)
    if paper_choice == True:
        player_choice = 'paper'
        return player_choice
    
    scissors_choice = is_scissors_choice(choice)
    if scissors_choice == True:
        player_choice = 'scissors'
        return player_choice
    
    lizard_choice = is_lizard_choice(choice)
    if lizard_choice == True:
        player_choice = 'lizard'
        return player_choice
    
    spock_choice = is_spock_choice(choice)
    if spock_choice == True:
        player_choice = 'spock'
        return player_choice
    player_choice = ''
    return player_choice

def is_rock_choice(choice):
    if choice == 'rock':
        return True
    elif choice == 'r':
        return True
    elif choice.startswith('r') and choice != 'rock':
        prompt('Did you mean "rock?" (y/n)')
        answer = input().lower()
        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            
            prompt('please enter "y" or "n".')
            answer = input().lower()
        
        if answer == 'y':
            prompt('Awesome! Nice choice!')
            return True
        return False
    else:
        return False

def is_paper_choice(choice):
    if choice == 'paper':
        return True
    elif choice == 'p':
        return True
    elif choice.startswith('p') and choice != 'paper':
        prompt('Did you mean "paper?" (y/n)')
        answer = input().lower()
        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            
            prompt('please enter "y" or "n".')
            answer = input().lower()
        
        if answer == 'y':
            prompt('Awesome! Nice choice!')
            return True
        return False
    else:
        return False

def is_scissors_choice(choice):
    if choice == 'scissors':
        return True
    elif choice == 'sc':
        return True
    elif choice == 's':
        prompt('Which did you mean? a) scissors b) spock')
        answer = input().lower()
        while True:
            if answer == 'a' or answer == 'b':
                break
            
            prompt('please enter "a" or "b".')
            answer = input().lower()
        if answer == 'a':
            prompt('Awesome! Nice choice!')
            return True
        prompt('Awesome! Nice choice!')
        return False
    elif choice.startswith('s') and choice != 'scissors':
        prompt('Did you mean "scissors?" (y/n)')
        answer = input().lower()
        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            
            prompt('please enter "y" or "n".')
            answer = input().lower()
        
        if answer == 'y':
            prompt('Awesome! Nice choice!')
            return True
        return False
    else:
        return False

def is_lizard_choice(choice):
    if choice == 'lizard':
        return True
    elif choice == 'l':
        return True
    elif choice.startswith('l') and choice != 'lizard':
        prompt('Did you mean "lizard?" (y/n)')
        answer = input().lower()
        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            
            prompt('please enter "y" or "n".')
            answer = input().lower()
        
        if answer == 'y':
            prompt('Awesome! Nice choice!')
            return True
        return False
    else:
        return False

def is_spock_choice(choice):
    if choice == 'spock':
        return True
    elif choice == 's':
        return True
    elif choice.startswith('s') and choice != 'spock':
        prompt('Did you mean "spock?" (y/n)')
        answer = input().lower()
        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            
            prompt('please enter "y" or "n".')
            answer = input().lower()
        
        if answer == 'y':
            prompt('Awesome! Nice choice!')
            return True
        return False
    else:
        return False

def get_player_choice():
    while True:
        prompt(f'choose one of the following: ({", ".join(VALID_CHOICES)}.)')
        prompt("Make your choice by typing the full word or first letter. Choose wisely!")

        player_input = input().lower()
        while True:
            is_valid = is_valid_choice(player_input)
            if is_valid == True:
                break
            prompt(f"please choose {", ".join(VALID_CHOICES)}")
            player_input = input().lower()
        
        player_choice = calculate_player_choice(player_input)
        if player_choice:
            break
        prompt("No worries! Let's try again.")

    return player_choice

def get_computer_choice():
    comp_choice = random.choice(VALID_CHOICES)
    return comp_choice

def display_round_winner(player_input, computer_input):
    if ((player_input == "rock" and computer_input == "scissors") or
        (player_input == "paper" and computer_input == "rock") or
        (player_input == "scissors" and computer_input == "paper")):
        prompt(f"You chose {player_input}, and the computer chose {computer_input}; You win!")
    elif ((player_input == "rock" and computer_input == "paper") or
          (player_input == "paper" and computer_input == "scissors") or
          (player_input == "scissors" and computer_input == "rock")):
        prompt(f"You chose {player_input}, and the computer chose {computer_input}; Computer wins!")
    else:
        prompt(f"You chose {player_input}, and the computer chose {computer_input}; It's a tie!")

def main():
    welcome_message()
    player_choice = get_player_choice()
    rock_choice = is_rock_choice(player_choice) # for testing
    print(rock_choice)
    computer_choice = get_computer_choice()
    display_round_winner(player_choice, computer_choice)


main()