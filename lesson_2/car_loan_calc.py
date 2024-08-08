# You'll need three pieces of information:

#   the loan amount
#   the Annual Percentage Rate (apr)
#   the loan duration

# From the above, you'll need to calculate the following two things:

#   monthly interest rate (apr / 12)
#   loan duration in months

MONTHS_IN_YEAR = 12
PRECISION = 2

def prompt(message):
    print(f'==> {message}')

def get_loan_amount():
    prompt('Please enter the loan amount')
    loan_amount = input()
    while is_valid_input(loan_amount) is not True:
        print('Please enter a positive numeric value')
        loan_amount = input()
    return loan_amount

def get_apr():
    prompt("Thank you! Please enter the Annual Percentage rate.")
    apr = input()
    while is_valid_input(apr) is not True:
        print('Please enter a positive numeric value')
        apr = input()
    return apr

def get_loan_duration():
    prompt("Thank you! Please enter the duration of the loan in years.")
    loan_duration = input()
    while is_valid_input(loan_duration) is not True:
        print('Please enter a positive numeric value')
        loan_duration = input()
    monthly_duration = years_to_months(loan_duration)
    return monthly_duration

def invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        return True

    return False

def verify_positive_int(user_input):
    if int(user_input) <= 0:
        return True
    return None

def calculate_monthly_rate(percentage_rate):
    monthly_interest_rate = float((float(percentage_rate) / 100) / MONTHS_IN_YEAR)
    return monthly_interest_rate

def years_to_months(months):
    return float(months) * MONTHS_IN_YEAR

def calculate_monthly_payment(loan_amount, monthly_interest_rate, \
                               monthly_duration):
    monthly_payment_amount = float(loan_amount) * (float(monthly_interest_rate)
        / (1 - (1 + float(monthly_interest_rate))
        ** (-float(monthly_duration))))
    return monthly_payment_amount

def is_valid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        return False

    if float(user_input) <= 0:
        return False
    return True

def display_monthly_payment(monthly_payment_amount):
    prompt(f"your monthly payment is ${round(monthly_payment_amount, PRECISION)}")

def main():
    loan_amount = get_loan_amount()
    apr = get_apr()
    monthly_interest_rate = calculate_monthly_rate(apr)
    monthly_duration = get_loan_duration()
    prompt("Thanks!")
    monthly_payment_amount = calculate_monthly_payment(loan_amount, \
         monthly_interest_rate, monthly_duration)
    display_monthly_payment(monthly_payment_amount)

main()