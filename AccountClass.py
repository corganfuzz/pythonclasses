class Account:

    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    # Accessor methods
    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    # Mutator methods
    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    # Calculations methods

    def getMonthlyInterestRate(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyInterestAmount = self.__balance * self.getMonthlyInterestRate()
        return monthlyInterestAmount

    def withdraw(self):
        withdraw = self.__balance - 2500
        return withdraw

    def deposit(self):
        deposit = self.__balance + 3000
        return deposit


