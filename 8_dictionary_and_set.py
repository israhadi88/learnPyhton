# dictionary adalah sepasang value antara key:value
# contoh
dictionary = {
    "nama": "Israhadi",
    "alamat": "Mampang",
    "aset bergerak": ["Motor", "Mobil"],
}
print(dictionary)

# contoh bikin dict dengan {}
pizza = {
    "name": "Margherita Pizza",
    "price": 8.9,
    "calories_per_slice": 250,
    "toppings": ["mozzarella", "basil"],
}
print(pizza)

# contoh bikin dict dengan built-in function dict()
pizza = dict(
    [
        ("name", "Margherita Pizza"),
        ("price", 8.9),
        ("calories_per_slice", 250),
        ("toppings", ["mozzarella", "basil"]),
    ]
)
for key, value in pizza.items():
    print(f"{key}:{value}")

x = pizza.get("toppings", [])  # mengakses toppings dalam dict pizza
print(x)  # ["mozzarella", "basil"]

sate = dict(
    [
        ("name", "Sate Ayam"),
        ("price", "25000"),
        ("calories", "740"),
        ("toppings", ["Peanut Sauce", "Soy"]),
    ]
)
print(sate)
sate.pop("price", 25000)  # hapus price dan valuenya
print(sate)
sate["price"] = 25000  # update value key price
print(sate)
sate.clear()  # hapus semua dict
print(sate)

sate = dict(
    [
        ("name", "Sate Ayam"),
        ("price", "25000"),
        ("calories", "740"),
        ("toppings", ["Peanut Sauce", "Soy"]),
    ]
)
print(sate)
sate.update(
    {"name": "Sate Kambing", "total_time": 20}
)  # ganti value atau nambahin key+value yang belum ada
sate.popitem()  # hapus key:value terakhir (toppings: value)

#common techniques to loop over dict
product = {
    'Laptop':900,
    'Handphone':600,
    'Tablet':750,
    'Headphone':350
}
for index, item in enumerate(product.keys(), start=1):
    print(f'{index}. {item}') #ini menampilkan key menggunakan keys() dan loop
for index, item in enumerate(product.values(), start=1):
    print(f'{index}. {item}') #ini menampilkan value menggunakan values() dan loop
for index, item in enumerate(product.items(), start=1):
    print(f'{index}. {item}') #ini menampilkan key+calue menggunakan items() dan loop


print(product)
print(product.values())
print(product.keys())
print(product.items())

my_set = {1,2,3,4,5}
copy_my_set = {1,2,3,4,5}
your_set = {2,3,4,5,6}
print(my_set&your_set)
print(my_set|your_set)

print(copy_my_set.issubset(my_set))
print(copy_my_set.issuperset(my_set))