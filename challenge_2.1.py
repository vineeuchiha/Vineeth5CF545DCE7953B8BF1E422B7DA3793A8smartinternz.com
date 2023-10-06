class bank_account:
    def __init__(self,account_number,account_holder_name,initial_balance=0.0):
        self.__account_number=account_number
        self.__account_holder_name=account_holder_name
        self.__account_balance=initial_balance
    def deposit(self,amount):
        if amount>0:
            self.__account_balance +=amount
            print("deposited RS{}.new balance RS{}".format(amount,self.__account_balance))
        else:
            print("invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__account_balance:
            self.__account_balance-=amount
            print("withdraw RS{}.new balance:RS{}".format (amount,self.__account_balance))
        else:
            print("invalid withdrawal amount or insufficient balance")
    def display_balance(self):
        print("account balance for{}(account #{}):RS{}".format(self.__account_holder_name,
                                                               self.__account_number,
                                                               self.__account_balance))


account=bank_account(account_number="1234567890",
                         account_holder_name="vijay",
                         initial_balance=50000.00)
account.display_balance()
account.deposit(500.00)
account.withdraw(200.00)
account.display_balance()
