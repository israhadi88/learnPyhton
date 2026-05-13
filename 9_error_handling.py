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

#python menyediakan try, except, else, dan finally buat handle error

try: #try block kode yang di antisipasi bakalan ngasih error
    x = 10 / 0
except ZeroDivisionError: #kode blok yang bakal running kalo ada error, disini pembagian dengan nol
    print("You cant divide by zero!")

