class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()}! says woof woof! I'm {self.age} years old")


dog_1 = Dog("Jack", 3)

dog_1.bark()

# attibute ada 2 yaitu instance dan class


class Car:
    jumlah_roda = 4  # ini attribute class

    def __init__(self, merk, tipe):
        self.merk = merk  # ini adalah attribute instance
        self.tipe = tipe

    def describe(self):
        return f"This car is a {self.merk} {self.tipe}"


mobil_a = Car("Toyota", "Avanza")
print(mobil_a.merk, mobil_a.tipe)  # manggil attribute instance
print(Car.jumlah_roda)  # manggil attribute kelas langsung pake nama kelas
print(mobil_a.describe())


class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def __len__(self):
        return self.page

    def __str__(self):
        return f"'{self.title}' has {self.page} pages"

    def __eq__(self, value):
        return self.page == value.page


book1 = Book("Renjana", 420)
book2 = Book("Bumi dan Langit", 420)

print(len(book1))
print(len(book2))
print(str(book1))
print(book1 == book2)


# coretan buat magic method
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} added")

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed")
        else:
            print(f"{item} is not in cart")

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


cart = Cart()
cart.add("Laptop")
cart.add("Wireless mouse")
cart.add("Ergo keyboard")
cart.add("Monitor")

# for item in cart:
#   print(item, end=' '"\n")

# cart.remove('Monitor')
# cart.remove("banana")
# for item in cart:
#   print(item, end=' '"\n")

atr_name = input("Enter yout attribute you want to see:")
print(getattr(cart, atr_name, "Attribute Not Found"))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desc(self):
        return f"My name is {self.name} {self.age} years old"


person_1 = Person("Israhadi", 29)


print(person_1.desc())
print(
    getattr(person_1, "Sex", "Male")
)  # masukkan attribute name dan value jika tidak ada


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John Doe", 30)

att_name = input("Enter the attribute you want to see: ")
print(getattr(person, att_name, "Attribute not found"))
print(person.city)  # give error


# coba pake try-except
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Annie", 33)

attr_name = input("Enter the attribute:")

try:
    value = getattr(person, attr_name)
    print(value)
except AttributeError:
    print("Attribute not found")


# using getattr if doesnt exist
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John Cena", 55)
print(f"attribute name: {person.name}")
print(f"attribute age: {person.age}")
print(f"attribute tambahan 'city', default value: {getattr(person,'city','Milan')}")


# using dir()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 31)

for a in dir(person):
    if not a.startswith("__") and not callable(getattr(person, a)):
        value = getattr(person, a)
        print(f"{a}: {value}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bicara(self):  # <--- Ini fungsi buatanmu sendiri
        return "Halo!"


person = Person("John", 31)


# KODE KAMU (Tanpa not callable)
for a in dir(person):
    if not a.startswith("__") and not callable(getattr(person, a)):
        value = getattr(person, a)
        print(f"{a}: {value}")


# setattr
class Configuration:
    pass


setting_data = {
    "server_url": "https://api.example.com",
    "timeout_sec": 30,
    "max_retries": 5,
}

config_obj = Configuration()

for key, value in setting_data.items():
    setattr(config_obj, key, value)

print(config_obj.server_url)  # https://api.example.com
print(config_obj.timeout_sec)
print(config_obj.max_retries)


# hasattr() cek ada atau enggak attribute tsb, return false/true
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product_a = Product("T-shirt", 25)

required_attributes = ["name", "price", "inventory_id"]

for attr in required_attributes:
    if not hasattr(product_a, attr):
        setattr(product_a, "inventory_id", 1)
        print(
            f"Attribute '{attr}' tidak ditemukan, menambahkan attribute '{attr}' dengan nilai {getattr(product_a,attr)}"
        )
    # elif not hasattr(product_a, attr):
    #    setattr(product_a, 'inventory_id',1)
    else:
        print(f"{attr}: {getattr(product_a, attr)}")

#delattr() buat remove attribute:

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token
        self.temp_counter = 0

session = UserSession(101,'a123d123d123')

attribute_to_clean = ['auth_token', 'temp_counter']

for attr in attribute_to_clean:
    if hasattr(session,attr):
        delattr(session,attr)
        print(f"Attribute '{attr}' removed")
print(f'\nfinal attribute remaining:')

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session,attr)):
        print(f" - {attr}: {getattr(session,attr)}")


class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token
        self.temp_counter = 0

session = UserSession(102,'a124451ksa')

temp = ['auth_token','temp_counter']

for attr in temp:
    if hasattr(session,attr):
        delattr(session,attr)
        print(f"'{attr}' removed")
print("\n Attribute remaining:")

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session,attr)):
        print(f"- {attr}: {getattr(session,attr)}")