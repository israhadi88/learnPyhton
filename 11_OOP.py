class Wallet:
        def __init__(self,balance):
            self._balance = balance
            print(f"Dompet dibuat dengan saldo awal {self._balance}")

        
        def deposit(self,amount):
            print(f"Mencoba deposit: {amount}")
            if amount > 0:
                self._balance += amount
                print(f"Berhasil menambahkan deposit {self._balance}")
        
        def withdraw(self,amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
