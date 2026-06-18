class Dompet:
    def __init__(self):
        self.__balance = 0
    
    def __validate(self,amount):
        if amount < 0:
            raise ValueError ("Amount must be higher than 0")
    
    def deposit(self,amount):
        self.__validate(amount)
        self.__balance += amount
    
    def withdraw(self,amount):
        self.__validate = (amount)
        if amount > self.__balance:
            raise ValueError ('Dana kurang')
        self.__balance -= amount
    
    def cek_saldo(self):
        return self.__balance

acct_one = Dompet()
acct_one.deposit(50)
print(acct_one.cek_saldo())
acct_one.withdraw(10)
print(acct_one.cek_saldo())
acct_one.withdraw(-21)
print(acct_one.cek_saldo())
