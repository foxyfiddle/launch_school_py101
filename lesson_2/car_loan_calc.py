# You'll need three pieces of information:

#   the loan amount
#   the Annual Percentage Rate (apr)
#   the loan duration

# From the above, you'll need to calculate the following two things:

#   monthly interest rate (apr / 12)
#   loan duration in months

def prompt(message):
    print(f'==> {message}')

def get_loan_amount():
    global loan_amount
    loan_amount = input()
    while is_valid_input(loan_amount) is not True:
        print('Please enter a positive numeric value')
        loan_amount = input()
    return loan_amount

def get_apr():
    global apr
    apr = input()
    while is_valid_input(apr) is not True:
        print('Please enter a positive numeric value')
        apr = input()
    return apr

def get_loan_duration():
    global monthly_duration
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
    global monthly_interest_rate
    monthly_interest_rate = float((float(percentage_rate) / 100) / 12)
    return monthly_interest_rate

def years_to_months(months):
    return float(months) * 12

def calculate_monthly_payment(loan_amount, monthly_interest_rate, \
                               monthly_duration):
    global monthly_payment_amount
    monthly_payment_amount = float(loan_amount) * (float(monthly_interest_rate)
        / (1 - (1 + float(monthly_interest_rate))
        ** (-float(monthly_duration))))
    prompt(f"your monthly payment is ${round(monthly_payment_amount, 2)}")
    return monthly_payment_amount

def is_valid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        return False

    if float(user_input) <= 0:
        return False
    return None

def main():

    prompt('Please enter the loan amount')
    get_loan_amount() # returns "loan_amount"
    prompt("Thank you! Please enter the Annual Percentage rate.")
    get_apr() # returns "apr" variable
    calculate_monthly_rate(apr) # returns "monthly_interest_rate"
    prompt("Thank you! Please enter the duration of the loan in years.")
    get_loan_duration() # returns 'loan_duration"
    prompt("Thanks!")
    calculate_monthly_payment(loan_amount, \
         monthly_interest_rate, monthly_duration)

main()