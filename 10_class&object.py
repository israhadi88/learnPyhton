class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()}! says woof woof! I'm {self.age} years old")


dog_1 = Dog("Jack", 3)

dog_1.bark()

#attibute ada 2 yaitu instance dan class

class Car:
    jumlah_roda = 4 #ini attribute class

    def __init__(self,merk,tipe):
        self.merk = merk #ini adalah attribute instance
        self.tipe = tipe

    def describe(self):
        return f"This car is a {self.merk} {self.tipe}"

mobil_a = Car('Toyota','Avanza')
print(mobil_a.merk, mobil_a.tipe) #manggil attribute instance
print(Car.jumlah_roda) #manggil attribute kelas langsung pake nama kelas 
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
    
book1 = Book("Renjana",420)
book2 = Book("Bumi dan Langit",420)

print(len(book1))
print(len(book2))
print(str(book1))
print(book1==book2)

#coretan buat magic method 
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} added")

    def remove (self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed")
        else:
            print(f'{item} is not in cart')
    
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
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' '"\n") 

cart.remove('Monitor')
cart.remove("banana")
for item in cart:
   print(item, end=' '"\n") 