import random
from random import randint
import string
import time
class Bank:
    accounts = 0
    account_number = 1000
    account_balance = 0.00
    all_accounts = [1000]
    user_names = []
    user_numbers = []
    def __init__(self):
       print("Welcome to xyz bank")
       time.sleep(2)
       print("------------------")

    def details(self):
        user_input1 = int(input("select options \n""press 1 - create an account\n" "press 2 - Exit\n""Enter : "))
        if user_input1 == 1:
            self.name = str(input("\tenter your name : ")).upper()
            Bank.user_names.append(self.name)
            self.phonenumber = str(input("\tenter phone number : "))
            Bank.user_numbers.append(self.phonenumber)
            self.accounts = Bank.accounts
            Bank.account_number = Bank.account_number + 1
            Bank.accounts = Bank.accounts+1
            Bank.all_accounts.append(Bank.account_number)
            customer_1.set_atm_pin()
        else:
            print("Invalid details")
            exit()
    def set_atm_pin(self):
        print("generating your pin......")
        time.sleep(2)
        self.pin = randint(0000, 9999)
        print(f"Your pin :", self.pin)
    def userdetails(self):
        print("........................\n""Your account is getting ready\n")
        time.sleep(3)
        print("customer name : {}\nphonenumber : {}\naccount_number : {}\n ".format(self.name,self.phonenumber,Bank.account_number))

    def deposit(self):
        print("---------DEPOSIT---------")
        self.amount = float(input("Enter deposit amount : "))
        Bank.account_balance = Bank.account_balance + self.amount
        print("your current account balance : {}".format(float(Bank.account_balance)))
        print("\n")

    def show_all(self):
        print(Bank.user_names)
        print(Bank.user_numbers)

    def withdraw_money(self):
        print("---------WITHDRAW----------")
        user_input = int(input("enter your pin : "))
        if user_input == self.pin:
            print("your current balance : {}".format(Bank.account_balance))
            user_input2 = float(input("Enter your amount : "))
            if user_input2 <= Bank.account_balance:
                Bank.account_balance = Bank.account_balance - user_input2
                print("collect your cash")
                print("your remaining balance : {}".format(Bank.account_balance))
            else:
                print("Invalid amount")
        else:
            print("wrong pin")

    def send_money(self):
        print("\n")
        print("--------SEND AMOUNT--------")
        self.send = float(input("send amount : "))
        self.receiver = int(input("Enter receiver's account number : "))
        if self.send < Bank.account_balance and self.receiver in Bank.all_accounts:
            Bank.account_balance = Bank.account_balance - self.send
            print("Your current balance : {}".format(float(Bank.account_balance)))
        else:
            print("Enter vaild details ")

class InterNetBanking(Bank):
    user_ids = []
    user_keys = []
    length = 5
    randomstr = ''.join(random.choices(string.ascii_letters, k=length)).lower()
    def __init__(self):
        super().__init__()
        print("\n")
        print("Welcome to Net Banking _/\_")

    def set_login(self):
        userinput_2 = int(input("Enter 1 to create Internet Banking, 2 to exit : "))
        if userinput_2 == 1:

            self.middle_name = str(input("enter your middle name :"))
            self.login_username = InterNetBanking.randomstr + self.middle_name.lower()
            InterNetBanking.user_ids.append(self.login_username)
            customer_1.show_login()
            customer_1.set_pin()
            customer_1.show_login_pin()

        elif userinput_2 == 2:
            print("Thank you")
    def show_login(self):
        print("your login id is : {}".format(self.login_username))
    def set_pin(self):
        self.login_pin = randint(000000, 999999)
    def show_login_pin(self):
        print("your login pin is : {}".format(self.login_pin))
        InterNetBanking.user_keys.append(self.login_pin)

class Loan(InterNetBanking):
    def __init__(self):
        super().__init__()
        print("\n")
        print("Welcome to xyz _/\_")
        print("--------Loan details---------")

    def interest_rates(self):
        self.pl = 0.1
        self.sl = 0.13
        self.cl = 0.08
        self.hl = 0.11

    def user_login(self):

        self.user_input3 = str(input("Enter your name : ")).upper()
        self.user_input4 = int(input("Enter your account number : "))
        self.user_input5 = str(input("Enter your login id : "))
        self.user_input6 = int(input("Enter your login pin : "))


        if self.user_input3 in Bank.user_names and self.user_input4 in Bank.all_accounts and self.user_input5 in InterNetBanking.user_ids and self.user_input6 in InterNetBanking.user_keys:
            user_options = int(input("press 1 -- personal loan\n""press 2 -- student loan\n""press 3 -- car loan\n""press 4 -- house loans\n""press 5 -- other loans\n""enter : "))
            self.p = float(input("Enter required loan amount : "))
            self.n = float(input("Number of time periods : "))
            if user_options == 1:
                self.interest = self.p * self.pl * self.n
                print("rate of interest 10%")
                print("Total Interest amount for ${} and for {}year : ${}".format(self.p, self.n , self.interest))
            elif user_options == 2:
                self.interest = self.p * self.sl * self.n
                print("rate of interest 13%")
                print("Total Interest amount for ${} and for {}year : ${}".format(self.p, self.n , self.interest))

            elif user_options == 3:
                self.interest = self.p * self.cl * self.n
                print("rate of interest 8%")
                print("Total Interest amount for ${} and for {}year : ${}".format(self.p, self.n , self.interest))

            elif user_options == 4:
                self.interest = self.p * self.hl * self.n
                print("rate of interest 11%")
                print("Total Interest amount for ${} and for {}year : ${}".format(self.p, self.n , self.interest))
            elif user_options == 5:
                print("contact local bank agents")

        else:
            print("Invalid")

customer_1 = Bank()
customer_1.details()
customer_1.userdetails()
customer_1.deposit()
# customer_1.show_all()
customer_1.withdraw_money()
customer_1 = InterNetBanking()
customer_1.set_login()
customer_1 = Loan()
customer_1.interest_rates()
customer_1.user_login()

