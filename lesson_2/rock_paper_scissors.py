# get player choice -- done
# get computer choice -- done
# calculate winner -- done
# display winner of round -- done
# update total of rounds won -- done
# loop through first 5 steps -- done
# when someone wins 3 rounds -- done
# display winner of round and game
# ask if player wants to play again

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'==> {message}')

def welcome_message():
    prompt('Welcome to "Rock, Paper, Scissors, Lizard, Spock!"')

def is_valid_choice(choice):
    if choice.startswith('r') or choice.startswith('p') or \
        choice.startswith('s') or choice.startswith('l'):
        return True
    return False

def calculate_player_choice(choice):
    player_choice = ''

    rock_choice = is_rock_choice(choice)
    if rock_choice is True:
        player_choice = 'rock'
        return player_choice

    paper_choice = is_paper_choice(choice)
    if paper_choice is True:
        player_choice = 'paper'
        return player_choice

    scissors_choice = is_scissors_choice(choice)
    if scissors_choice is True:
        player_choice = 'scissors'
        return player_choice

    lizard_choice = is_lizard_choice(choice)
    if lizard_choice is True:
        player_choice = 'lizard'
        return player_choice

    spock_choice = is_spock_choice(choice)
    if spock_choice is True:
        player_choice = 'spock'
        return player_choice
    player_choice = ''
    return player_choice

def is_rock_choice(choice):
    if choice == 'rock':
        return True
    if choice == 'r':
        return True
    if choice.startswith('r') and choice != 'rock':
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
    return False

def is_paper_choice(choice):
    if choice == 'paper':
        return True
    if choice == 'p':
        return True
    if choice.startswith('p') and choice != 'paper':
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
    return False

def is_scissors_choice(choice):
    if choice == 'scissors':
        return True
    if choice == 's':
        prompt('Which did you mean? a) scissors b) spock')
        answer = input().lower()
        while True:
            if answer in ('a', 'b'):
                break

            prompt('please enter "a" or "b".')
            answer = input().lower()
        if answer == 'a':
            prompt('Awesome! Nice choice!')
            return True
        prompt('Awesome! Nice choice!')
        return False
    if choice.startswith('s') and choice != 'scissors':
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
    return False

def is_lizard_choice(choice):
    if choice == 'lizard':
        return True
    if choice == 'l':
        return True
    if choice.startswith('l') and choice != 'lizard':
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
    return False

def is_spock_choice(choice):
    if choice == 'spock':
        return True
    if choice == 's':
        return True
    if choice.startswith('s') and choice != 'spock':
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
    return False

def get_player_choice():
    while True:
        prompt(f'choose one of the following: ({", ".join(VALID_CHOICES)}.)')
        prompt(
    "Make your choice by typing the full word or first letter. Choose wisely!")

        player_input = input().lower()
        while True:
            is_valid = is_valid_choice(player_input)
            if is_valid is True:
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

def rock_is_winning_choice(winning_input, \
                           losing_input):
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    # 3 = lizard
    # 4 = spock

    if winning_input == VALID_CHOICES[0] and \
        losing_input == VALID_CHOICES[3] or \
        winning_input == VALID_CHOICES[0] and \
        losing_input == VALID_CHOICES[2]:
        return True
    return False

def paper_is_winning_choice(winning_input, \
                           losing_input):
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    # 3 = lizard
    # 4 = spock

    if winning_input == VALID_CHOICES[1] and \
        losing_input == VALID_CHOICES[0] or \
        winning_input == VALID_CHOICES[1] and \
        losing_input == VALID_CHOICES[4]:
        return True
    return False

def scissors_is_winning_choice(winning_input, \
                           losing_input):
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    # 3 = lizard
    # 4 = spock

    if winning_input == VALID_CHOICES[2] and \
        losing_input == VALID_CHOICES[1] or \
        winning_input == VALID_CHOICES[2] and \
        losing_input == VALID_CHOICES[3]:
        return True
    return False

def lizard_is_winning_choice(winning_input, \
                           losing_input):
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    # 3 = lizard
    # 4 = spock

    if winning_input == VALID_CHOICES[3] and \
        losing_input == VALID_CHOICES[4] or \
        winning_input == VALID_CHOICES[3] and \
        losing_input == VALID_CHOICES[1]:
        return True
    return False

def spock_is_winning_choice(winning_input, \
                           losing_input):
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    # 3 = lizard
    # 4 = spock

    if winning_input == VALID_CHOICES[4] and \
        losing_input == VALID_CHOICES[2] or \
        winning_input == VALID_CHOICES[4] and \
        losing_input == VALID_CHOICES[0]:
        return True
    return False

def is_winner(winning_input, losing_input):
    if rock_is_winning_choice(winning_input, losing_input) is True:
        return True

    if paper_is_winning_choice(winning_input, losing_input) is True:
        return True

    if scissors_is_winning_choice(winning_input, losing_input) is True:
        return True

    if lizard_is_winning_choice(winning_input, losing_input) is True:
        return True

    if spock_is_winning_choice(winning_input, losing_input) is True:
        return True

    return False

def display_round_winner(winner_result, player_choice, computer_choice, round_number):
    # 0 = player_winner
    # 1 = computer_winner

    if winner_result == 0:
        prompt(f"You chose {player_choice}, and the "
                 f"computer chose {computer_choice}; You won round {round_number}!")
    elif winner_result == 1:
        prompt(f"You chose {player_choice}, and the "
                 f"computer chose {computer_choice}; the computer won round {round_number}!")
    else:
        prompt(f"You chose {player_choice}, and the "
                 f"computer chose {computer_choice}; round {round_number} was a tie!")

def calculate_winner(player_choice, computer_choice):
    # 0 = player_winner
    # 1 = computer_winner

    player_winner = is_winner(player_choice, computer_choice)
    computer_winner = is_winner(computer_choice, player_choice)
    if player_winner is True:
        return 0
    if computer_winner is True:
        return 1
    return None

def update_rounds_won(winner_counter):
    winner = winner_counter
    winner += 1
    return winner

def is_play_again():
    prompt('would you like to play again? (y/n)')
    play_again = input()
    while True:
        if play_again.startswith('y') or play_again.startswith('n'):
            break
        else: 
            prompt('Please choose y or n')
            play_again = input()
    if play_again == 'y':
        return True
    if play_again == 'n':
        return False

def increase_round_number(current_round):
    current_round += 1
    return current_round

def main():
    player_rounds_won = 0
    computer_rounds_won = 0
    rounds_counter = 1

    welcome_message()
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        round_winner = calculate_winner(player_choice, computer_choice)
        display_round_winner(round_winner, \
            player_choice, computer_choice, rounds_counter)
        rounds_counter = increase_round_number(rounds_counter)
        if round_winner == 0:
            player_rounds_won = update_rounds_won(player_rounds_won)
        if round_winner == 1:
            computer_rounds_won = update_rounds_won(computer_rounds_won)
        print(player_rounds_won)
        print(computer_rounds_won)
        if player_rounds_won == 3 or computer_rounds_won == 3:
            play_again = is_play_again()
            if play_again is True:
                continue
            else:
                prompt('Thanks for playing!')
                break
            


main()