class Wallet:
    def __init__(self, balance):
        self._balance = balance
        print(f"Dompet dibuat dengan saldo awal {self._balance}")

    def deposit(self, amount):
        print(f"Mencoba deposit: {amount}")
        if amount > 0:
            self._balance += amount
            print(f"Berhasil menambahkan deposit {self._balance}")
        else:
            print(f"Transaksi gagal! angka tidak boleh 0 ")

    def withdraw(self, amount):
        print(f"Mencoba menarik uang: {amount}")
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Berhasil menarik {amount}")
        else:
            print(f"Transaksi gagal saldo tidak cukup")
    
    def cek_saldo(self):
        print(f"Saldo saat ini {self._balance}")
        return self._balance

print("="*40)
print("MEMBUAT DOMPET BARU")
dompet = Wallet(1000)  # Saldo awal 1000
print()

print("="*40)
print("MENCoba DEPOSIT")
dompet.deposit(500)    # Deposit 500
print()

print("="*40)
print("MENCoba WITHDRAW")
dompet.withdraw(300)   # Withdraw 300
print()

print("="*40)
print("MENCoba WITHDRAW TERLALU BESAR")
dompet.withdraw(2000)  # Coba withdraw 2000 (gagal)
print()

print("="*40)
print("MENCoba DEPOSIT DENGAN NEGATIF")
dompet.deposit(-100)   # Deposit negatif (gagal)
print()

print("="*40)
print("CEK SALDO AKHIR")
dompet.cek_saldo()

#kode 2 ("__") private 
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
