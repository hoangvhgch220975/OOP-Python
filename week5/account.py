
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,id, name):
        self._id = id
        self._name = name
        self._balance = 0


    
#Get/set name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if value =="":
            print('Name cannot be empty')
        else:
            self._name = value
#Get balance
    @property
    def balance(self):
        return self._balance
    
#Processing withdraw
    @abstractmethod
    def withdraw(self, amount):
        pass

#Processing deposit:
    def deposit(self,amount):
        if amount <=0:
            print('Amount must be greater than 0')
            return
        self._balance += amount
        print(f'Deposit successfully! Current balance: {self.balance}')

    def __str__(self):
        return f'ID: {self._id} | Name: {self.name} | Balace: ${self.balance}'
    


