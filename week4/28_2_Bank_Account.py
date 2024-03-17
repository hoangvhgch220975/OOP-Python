


class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance =  balance

#Get ID
    @property
    def id(self):
        return self.__id
    
#Get/set name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if value =="":
            print('Name cannot be empty')
        else:
            self.__name = value
#Get balance
    @property
    def balance(self):
        return self.__balance
#Processing withdraw
    def withdraw(self):
        amount = int(input('Enter amount: '))
        if amount <=0 :
            print('Amount must be greater than 0')
            return
        if amount > self.balance:
            print('Insufficient funds')
            return
        self.__balance -= amount
        print(f'Withdraw successfully! Current balance: {self.balance}')

#Processing deposit:
    def deposit(self):
        amount = int(input('Enter amount: '))
        if amount <=0:
            print('Amount must be greater than 0')
            return
        self.__balance += amount
        print(f'Deposit successfully! Current balance: {self.balance}')

    def show(self):
        print(f'ID; {self.id} | Name: {self.name} | Balance: {self.balance}')
    


acc1 = BankAccount(1,"John Doe",10000)
acc1.show()

acc1.deposit()
acc1.show() 

acc1.withdraw()
acc1.show()
