import math
import argparse


# this function is intended to find i which is nominal interest
def find_i(loan_interest):
    return loan_interest / (12 * 100)


def month_calculator(i, A, P):
    # from te given formula x is A / A - i * P so it's written as below
    x = A / (A - i * P)
    # base is shown as 1 + i so it's written as below
    base = 1 + i
    return math.ceil(math.log(x, base))


def annuity_calculator(i, n, P):
    return P * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1)


def loan_principal_calculator(i, A, n):
    # as the formula is too complex I decided to divide it into variables
    # the denominator part of the formula will be calculated in this variable
    denominator = (i * pow((1 + i), n)) / (pow((1 + i), n) - 1)
    return A / denominator


def month_convert(number_of_months):
    number_of_years = math.floor(number_of_months / 12)
    remaining_months = math.ceil((number_of_months - (number_of_years * 12)))
    if number_of_months < 12:
        if number_of_months == 1:
            return f'{number_of_months} month'
        else:
            return f'{number_of_months} months'
    elif number_of_months == 12:
        return "1 year"
    elif remaining_months == 0:
        return f'{number_of_years} years'
    else:
        return f'{number_of_years} years and {remaining_months} months'


def find_period(interest, payment, principal):
    number_of_months = month_calculator(find_i(interest), payment, principal)
    # print(number_of_months)
    overpayment = math.ceil(payment * number_of_months - principal)
    return f'It will take {month_convert(number_of_months)} to repay this loan!\nOverpayment = {overpayment}'


def find_annuity_payment(principal, periods, interest):
    i = find_i(interest)
    annuity_payment = math.ceil(annuity_calculator(i, periods, principal))
    overpayment = math.ceil(annuity_payment * periods - principal)
    return f'Your annuity payment = {math.ceil(annuity_payment)}!\nOverpayment = {overpayment}'


def find_loan_principal(payment, periods, interest):
    i = find_i(interest)
    loan_principal = loan_principal_calculator(i, payment, periods)
    overpayment = math.ceil(payment * periods - loan_principal)
    return f'Your loan principal = {math.floor(loan_principal)}!\nOverpayment = {overpayment}'


def is_anything_negative(my_list):
    for n in my_list:
        try:
            if n is not str and n is not None:
                if int(n) < 0:
                    return True
        except ValueError:
            print('')
    return False


def calculate_diff_payment(principal, periods, interest):
    payments = []
    for i in range(1, int(periods) + 1):
        payment = principal / periods + (find_i(interest) * (principal - ((principal * (i - 1)) / periods)))
        payments.append(math.ceil(payment))
    # formula to find overpayment
    # print(sum(payments) - principal)
    return payments


parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')

args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]

if args.type is None:
    print('Incorrect parameters')
elif args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')
elif args.interest is None:
    print('Incorrect parameters')
elif is_anything_negative(arguments):
    print('Incorrect parameters')
elif arguments.count(None) > 1:
    print('Incorrect parameters')
elif args.type == 'diff' and args.payment is None:
    result = calculate_diff_payment(float(args.principal), float(args.periods), float(args.interest))
    # print(result)
    for i in range(len(result)):
        print(f'Month {i + 1}: payment is {result[i]}')
    overpayment = sum(result) - int(args.principal)
    print(f'\nOverpayment = {overpayment}')
elif args.type == "annuity" and args.payment is None:
    print(find_annuity_payment(float(args.principal), float(args.periods), float(args.interest)))
elif args.type == "annuity" and args.principal is None:
    print(find_loan_principal(float(args.payment), float(args.periods), float(args.interest)))
elif args.type == "annuity" and args.periods is None:
    print(find_period(float(args.interest), float(args.payment), float(args.principal)))
