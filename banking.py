# BANKING PROGRAM



def show_balance():
    pass
def deposit():
    pass
def withdrawal():
    pass

balance = int(input("enter your balance: "))

while True:
    print("----------BANKING PROGRAM----------")
    print("1. Show balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    print()

    choice = input("Enter (1,2,3,4): ")

    if choice.isdigit():
        if choice == "1":
            print(f"Your balance is {balance}")
        elif choice == "2":
            deposit = input("How much would you like to deposit: ")
            print()
            balance += int(deposit)
            print(f"Your deposit was {deposit} hence your balance is now {balance}")
        elif choice == "3" and int(choice)> 0:
            withdraw = input("How much would you like to withdraw: ")
            balance = balance - int(withdraw)
            print(f"The amount you withdrew is {withdraw} hence your balance is {balance}")
        elif choice == "4":
            print("THANK YOU FOR YOUR PATIENCE!")
            break
        else:
            print("INVALID RESPONSE")