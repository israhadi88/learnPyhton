hewan = ["ayam", "bebek", "kucing"]
buah = ["apel", "kelengkeng", "pir"]
sayur = ["bayam", "kangkung", "wortel"]


def finder(kode):
    if kode == "h":
        return f"Hewan: {hewan}"
    if kode == "b":
        return f"Buah: {buah}"
    if kode == "s":
        return f"Sayur: {sayur}"
    else:
        return None


while True:
    karakter = input("Masukkan kode:")
    hasil = finder(karakter)

    if hasil is not None:
        print(hasil)
        break
    else:
        print("Tidak ditemukan, gunakan h/b/s:")


def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} gives {result}")
    return result


add(2, 7127912)

# interactive debugging with pdb module
import pdb


def divider(a, b):
    pdb.set_trace()
    return a / b


print(divider(4, 2))

# exception handling
# Exception handling is the process of catching and managing errors that occur
# during the execution of a program, so your code doesn't crash unexpectedly.

# python menyediakan try, except, else, dan finally buat handle error

try:  # try block kode yang di antisipasi bakalan ngasih error
    x = 10 / 0
except (
    ZeroDivisionError
):  # kode blok yang bakal running kalo ada error, disini pembagian dengan nol
    print("You cant divide by zero!")


print("Division 10 / 0")
try:
    x = 10/0
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("Division successful:",x)
finally:
    print("This always run")


#menangkap beberapa exeption
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")


try:
    x = 1 / 0
except ZeroDivisionError as e: #kasih alias pada exception 
    print(f'Error occurred: {str(e).title()}')

#kasih multiple exception dalam 1 deklarasi dengan menggunakan tuple

try:
    number = int(input('Enter a number: '))
    result = 10 / number
except(ValueError,ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
else:
    print(f'{result}')

#raise
#manually trigger execption 

def check_age(age):
    if age < 0:
        raise ValueError ('Age cannot be negative value')
    return age

try:
    result = check_age(-1)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
else:
    print(f'Your age is {result}')

#re raise
def process_data(data):
    try:
        result = int(data)
        return result * 2 
    except ValueError:
        print('Logging: invalid data receive')
        raise #Ini melempar error yang sama ke luar

# Di luar fungsi
try:
    process_data('asd') 
except ValueError: 
    print('Handled in higher level')

#contoh
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e
config = parse_config('config.txt')

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')