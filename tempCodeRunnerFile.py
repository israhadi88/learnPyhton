class Wallet:
    def __init__(self, balance):
        self._balance = balance
        print(f"Dompet dibuat dengan saldo awal: Rp{self._balance}")
    
    def deposit(self, amount):
        print(f"Mencoba deposit: Rp{amount}")
        if amount > 0:
            self._balance += amount
            print(f"✅ Deposit berhasil! Saldo sekarang: Rp{self._balance}")
        else:
            print(f"❌ Deposit gagal! Jumlah harus lebih dari 0")
    
    def withdraw(self, amount):
        print(f"Mencoba withdraw: Rp{amount}")
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"✅ Withdraw berhasil! Saldo sekarang: Rp{self._balance}")
        else:
            print(f"❌ Withdraw gagal! Saldo tidak cukup atau jumlah tidak valid")
    
    def cek_saldo(self):
        print(f"Saldo saat ini: Rp{self._balance}")
        return self._balance

# ========== MENCOBA PROGRAM ==========
print("="*40)
print("MEMBUAT DOMPET BARU")
dompet = Wallet(0)  # Saldo awal 1000
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