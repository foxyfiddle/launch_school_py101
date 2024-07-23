# You'll need three pieces of information:

#   the loan amount
#   the Annual Percentage Rate (APR)
#   the loan duration

# From the above, you'll need to calculate the following two things:

#   monthly interest rate (APR / 12)
#   loan duration in months

def prompt(message):
    print(f'==> {message}')

def invalid_input(input):
    try: 
        float(input)
    except ValueError:
        return True
    else:
        return False
    
def monthly_rate(APR):
    return float((float(APR) / 100) / 12)

def years_to_months(months):
    return float(months) * 12



prompt('Please enter the loan amount')
loan_amount = input()

while invalid_input(loan_amount):
    prompt('Please enter a decimal value')
    loan_amount = input()

prompt("Thank you! Please enter the Annual Percentage rate.")
APR = input()

while invalid_input(APR):
    prompt('Please enter a decimal value')
    APR = input()

monthly_interest_rate = monthly_rate(APR)
prompt("Thank you! Please enter the duration of the loan in years.")
loan_duration = input()

while invalid_input(loan_duration):
    prompt('Please enter a numeric value')
    loan_duration = input()
monthly_duration = years_to_months(loan_duration)
prompt("Thanks!")

monthly_payment = float(loan_amount) * (float(monthly_interest_rate) / (1 - (1 + float(monthly_interest_rate)) ** (-float(monthly_duration))))

prompt(f"your monthly payment is ${'%.2f' % monthly_payment}")