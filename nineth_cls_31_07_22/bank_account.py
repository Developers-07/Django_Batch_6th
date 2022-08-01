
from customer_implement import CustomerImplement

class BankAccount(CustomerImplement):

    def __init__(self,name,phn,email,pad,balance,deposit,withdraw):
        super(BankAccount,self).__init__(name=name,phn=phn,email=email,pad=pad)
        self.__balance=balance
        self.__deposit=deposit
        self.__withdraw=withdraw

    def get_balance(self):
        return self.__balance

    def get_deposit(self):
        return self.__deposit

    def get_withdraw(self):
        return self.__withdraw

    def get_present_amount(self):
        amount = (self.__balance+self.__deposit)-self.__withdraw
        return amount

