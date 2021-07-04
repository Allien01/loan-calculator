import math

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

"""
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
"""

principal = int(input("Enter the loan principal: "))
option = input("""What do you want to calculate? 
Type 'm' for number of monthly payments,
Type 'p' for the monthly payment\n""")            
if option == 'm':
    pays_per_month = int(input("Enter the monthly payment: "))
    payment = round(principal / pays_per_month)
    if payment > 1:
        print("It will take {} months to repay the loan".format(payment))
    else:
        print("It will take {} month to repay the loan".format(payment))
elif option == 'p':
    months = int(input("Enter the number of months: "))
    pay = math.ceil(principal / months)
    last_payment = principal - (months - 1) * pay
    print("Your monthly payment = {} and the last payment = {}.".format(pay, last_payment))
else: quit()