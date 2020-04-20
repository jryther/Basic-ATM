#ATM Final Project
#Josh Ryther
#2/17/20

import sys

go = True
#Account Balance
account_balance = float(500.25)

#Print balance function
def printBalance (account_balance):
    print("Your current balance:")
    print("$%.2f\n" % account_balance)
#Deposit function
def deposit (account_balance):
    #Input parameter 1
    deposit_amount = float(input(
        "How much would you like to deposit today?\n"
        ))
    account_balance = account_balance + deposit_amount
    print(
        "Deposit was $%.2f, current balance is $%.2f\n" 
        % (deposit_amount, account_balance)
        )
    #Function returning output 1
    return account_balance
#Withdrawal function
def withdrawal (account_balance):
    #Input parameter 2
    withdrawal_amount = float(input(
        "How much would you like to withdraw today?\n"
    ))
    if withdrawal_amount > account_balance:
        print("$%.2f is greater than your account balance of $%.2f\n" 
        % (withdrawal_amount, account_balance)
        )
    else:
        account_balance = account_balance - withdrawal_amount
        print(
            "Withdrawal amount was $%.2f, current balance is $%.2f\n" 
            % (withdrawal_amount, account_balance)
        )
        #Function returning output 2
        return account_balance
#Program terminated function
def end_Program(go):
    print("Thank you for banking with us.")
    go = False
    #Function returning output 3
    return go

#Program start
while go == True:
    userChoice = input(
        "What would you like to do?\n"
        "(D)eposit, (W)ithdrawal, Account (B)alance, or (Q)uit\n"
    )
    userChoice = userChoice.title()
    if (userChoice == 'B'):
        printBalance (account_balance)
    if (userChoice == 'D'):
        account_balance = deposit(account_balance)
    if (userChoice == 'W'):
        account_balance = withdrawal(account_balance)
    if (userChoice == 'Q'):
        go=end_Program(go)