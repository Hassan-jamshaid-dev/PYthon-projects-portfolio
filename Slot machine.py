# SLOT MACHINE PROGRAM


import random

def row_spinning():
    spins = ["🍇","🍈","🍉","🍊","🍌"]
    results =[]
    for spin in range(3):
        results.append(random.choice(spins))
    return results

def print_rows(rows):
    print("- - - - - - - - - - -")
    print("|".join(rows))
    print("- - - - - - - - - - -")

def pay_out(rows,bet):
    if rows[0] == rows[1]== rows[2]:
        if rows[0] == "🍇":
             return int(bet)*6
        elif rows[0] == "🍈":
            return int(bet) * 3
        elif rows[0] == "🍉":
            return int(bet) * 10
        elif rows[0] == "🍊":
            return int(bet) * 5
        elif rows[0] == "🍌":
            return int(bet) * 12

    return 0


def main_():
    balance = input("Enter your balance: ")
    print("-----------PYTHON SLOT MACHINE-----------")
    print("🍇,🍈,🍉,🍊,🍌")
    print()
    print(f"Your balance is {balance}")
    while int(balance) > 0:
        bet = input("How much would you like to bet: ")
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        if int(bet) > int(balance):
            print("You cannot bet more than your balance")
            continue
        if int(bet)<=0:
            print("Bet must be a positive number")
            continue

        balance = int(balance) - int(bet)
        rows  = row_spinning()
        print("spinning... \n")
        print_rows(rows)
        payout = pay_out(rows,bet)
        if payout > 0:
            print(f"You won {payout}")
        else:
            print(f"Your balance is {balance}")
            print("You lost")

        balance += payout
        play_again = input("Do you want to play again (Y/N): ").upper()
        if play_again != "Y":
            break
if __name__ == "__main__":
    main_()