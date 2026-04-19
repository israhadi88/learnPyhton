#1. Function 
# reusable code ketika dipanggil
# input() dan print() adalah contih built-in function

name = input('What is your name?')
print(f'Hello, {name}')

#untuk menuliskan function sendiri, gunakan def: "def <nama fungsi>():"
def hello():
    print('Hellow')

hello()

def calculate(a,b):
    return(a+b)

mysum = calculate(1,2)
print (mysum)

#2. SCOPE
#scope menentukan point mana kamu bisa mengakses variable dengan aturan LEGB:
#L(local)
#variable di deklarasikan di dalam function
def myLocal():
    lvar = 10
    print(lvar)
myLocal()

#E(enclosing)
#function yang nested ke function lain, variable yang didalam function bisa memanggil variable yang
#(cont) berada di function sebelumnya
def outerFunction():
    msg = 'Hello World'

    def innerFunction():
        print(msg)
    innerFunction()
outerFunction() #menjalankan outerfunction yang dimana ada inner function yang menggunakan var outer

#another Enclosing scope
def outer_func():
    msg = 'Hello there!'
    res = '' #deklarasi res none, value di inner

    def inner_func():
        nonlocal res #modifikasi res adalah nonlocal
        res= 'How are you?'
        print(msg) #inner menggunakan variable outer

    inner_func()
    print(res) #res bisa di print

outer_func()

#G(global)
#variable yang dapat di akses semua function 
var = 10

def showVar():
    print(var)

showVar()
print(var)

#another global scope, making enclosing become global
var1 = 12 #variable global 
def showVar2():
    global var2 #deklarasi Enclosing jadi global
    var2 = 15
    print(f'ini adalah var 2: {var2}')
print(f'ini adalah var 1: {var1}')
showVar2()

#Enclosing bisa memodifikasi global variable
var_mod = 10
print(f'var_mod sebelum modifikasi: {var_mod}')
def mod_var():
    global var_mod
    var_mod = 30
mod_var()
print(f'var_mod sesudah modifikasi: {var_mod}')

#B(built-in)
#contoh-contoh built in 
print(str(22))
print(type(2))
print(isinstance(2,int))
    