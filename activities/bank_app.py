import os, time
class Bank:
    def __init__(self):
        self.accounts = list[Account]

def clear_screen():
    os.system("clear")

class Account:
    def __init__(self, name:str, balance:int = 0, pin:str | None = None):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.history = [str] 
    # show balance 
    def show_balance(self)->None:
        print(f"Balance: {self.balance}")
    # add balance
    def add_amount(self, amount:int):
        self.balance += amount
    # with draw
    def with_draw(self, amount:int):
        if(self.balance <= amount):
            print("testing")
            raise ValueError(" You have insufficient Funds!")
        self.balance -= amount    
    # show history

charles_accunt = Account("Charles", balance=125, pin="1234")

clear_screen()
# main
input_account = input("Enter your Account: ")
input_pin = input("Enter pin: ")
if charles_accunt.name != input_account or charles_accunt.pin != input_pin:
    raise ValueError("No account or Invalid pin!")

while True:
    clear_screen()
    print(f"\n------ Welcome {charles_accunt.name} ! -------\n")
    print("Menu: \n[1] Available Balance \n[2] Widraw \n[3] Deposit \n[4] Exit\n")
    print("--------------------------------")
    user_action = int(input("> "))
    print("\n")

    if user_action == 1:
        while True:
            clear_screen()
            print(f"\n------ Welcome {charles_accunt.name} ! -------\n")
            print(f"Available Balance: P{charles_accunt.balance}\n\n\n\n")
            print("        [1] Go back to Main Menu")
            print("--------------------------------")
            user_action = int(input("> "))
            if user_action == 1:
                break
    elif user_action == 2:
        clear_screen()
        print(f"\n------ Welcome {charles_accunt.name} ! -------\n\n")
        print("Enter Widraw Amount:")
        print("\n\n")
        amount = int(input("> "))
        try:
            charles_accunt.with_draw(amount)
            print("Withdraw succesfull")
            time.sleep(1)
        except ValueError:
            print("Insuffient Funds")
            continue
    elif user_action == 3:
        clear_screen()
        print(f"\n------ Welcome {charles_accunt.name} ! -------\n\n")
        print("Enter Deposit Amount:")
        print("\n\n")
        amount = int(input("> "))
        charles_accunt.add_amount(amount)
        print("Deposit succesfull")
        time.sleep(1)
    elif user_action == 4:
        print("Thank you")
        break
# user inter 
# input pin

