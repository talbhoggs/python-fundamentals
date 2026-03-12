import os, time

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
            raise ValueError(" You have insufficient Funds!")
        self.balance -= amount    
    # show history

class AutomatedTeller:
    def __init__(self, account:Account, user_action: int | None=None):
        self.account = account 
        self.users_action = user_action 
    
    def menu(self)->None:
        self.screen_template("Menu: \n[1] Available Balance \n[2] Widraw \n[3] Deposit \n[4] Exit\n")

    def available_balance(self)->None:
        self.screen_template(f"Available Balance: P{self.account.balance}\n\n\n\n\n        [1] Go back to Main Menu")
    
    def widraw(self)->None:
        self.screen_template("Enter Widraw Amount:\n\n\n\n\n")
        amount = self.user_action
        self.account.with_draw(amount=amount)
        print("Thank you") 
    
    def deposit(self):
        self.screen_template("Enter Deposit Amount:\n\n\n\n\n")
        amount = self.user_action
        self.account.add_amount(amount=amount)
        print("Thank you") 

    # utils
    def prompt(self):
        self.user_action = int(input("> "))
 
    def screen_template(self, text:str = ""):
        self.welcome_header()
        print(text)
        print("\n\n")
        self.divider()
        self.prompt() 

    def welcome_header(self):
        self.clear_screen()
        print(f"\n------ Welcome {self.account.name} ! -------\n")

    def divider(self):
        print("--------------------------------")
     
    def clear_screen(self):
        os.system("clear")

    def run(self):
        self.clear_screen()
        input_account = input("\nEnter your Account: ")
        input_pin = input("Enter pin: ")
        if self.account.name != input_account or self.account.pin != input_pin:
            raise ValueError("No account or Invalid pin!")

        while True:
            self.menu()
            if self.user_action == 1:
                while True:
                    self.available_balance()
                    if self.user_action == 1:
                        break
            elif self.user_action == 2:
                try:
                    self.widraw()
                except ValueError:
                    print("Insufficient Funds!")
                    time.sleep(1)
                    continue
                time.sleep(1) 
            elif self.user_action == 3:
                self.deposit()
                time.sleep(1) 
            elif atm.user_action == 4:
                print("Thank You")
                break


if __name__ == "__main__":
    charles_accunt = Account("Charles", balance=125, pin="1234")
    atm = AutomatedTeller(account=charles_accunt)
    atm.run()

# TODO:
# 1. Multi account
# 2. 