'''
Author:Jacob Thomas
Date:28/10/2024
Description: a program that simulates a simple bank ATM system
'''
balance_amount=100001
while True:
    print("\n1. \tCheck Balance")
    print("2.\tDeposit Money")
    print("3. \tWithdraw Money")
    print("4. \tExit" )
    choice= int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance is ${balance_amount}")
    elif choice==2:
        deposit_amount = float(input("Enter the amount "))
        balance_amount = balance_amount +deposit_amount
        print(f"The deposited amount is $ {deposit_amount} and " f" the current balance amount is ${balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("Enter the amount to withdraw"))
        if(withdraw_amount>balance_amount):
            print("Insufficient balance")
        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The amount withdrawn is ${withdraw_amount} and " f"The balance amount is ${balance_amount}")

    elif choice == 4:
        break
    else:
        print("Invalid Entry")