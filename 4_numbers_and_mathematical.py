#INTEGER
#Interger is a whole number without decimal even in negative
int_1 = 1
int_2 = -2
print(f'{int_1} adalah:', type(int_1))
print(f'{int_2} adalah:', type(int_2))

#integer addition
add_1 = 2
add_2 = 3
sum_add = add_1+add_2
print(f'ini adalah contoh:', sum_add) #5

#integer subtraction
int_1 = 5
int_2 = 2
sum_sub = int_1 - int_2
sum_mul = int_1 * int_2
sum_div = int_1 / int_2


print(f'int_1 ')
print(f'ini adalah contoh "-"', sum_sub) #contoh subtraction
print(f'ini adalah contoh "*"', sum_mul) #contoh multiplication
print(f'ini adalah contoh "/"', sum_div) #contoh division

#float is a whole decimal number even in negative value
float_1 = 10.5
float_2 = -2.5
print(f'{float_1} adalah:', type(float_1))
print(f'{float_2} adalah:', type(float_2))

my_float_1 = 15.5
my_float_2 = 2.5
float_add = my_float_1 + my_float_2
float_sub = my_float_1 - my_float_2
float_mul = my_float_1 * my_float_2
float_div = my_float_1 / my_float_2

print(f'ini adalah contoh "+"', float_add) #contoh subtraction
print(f'ini adalah contoh "-"', float_sub) #contoh subtraction
print(f'ini adalah contoh "*"', float_mul) #contoh multiplication
print(f'ini adalah contoh "/"', float_div) #contoh division

#int + float = float everything in decimal is float
intfl = 5
flint = 2.5
sumintfl = intfl + flint
print(sumintfl, type(sumintfl))

#mod and floor operator
mod1 = 4
mod2 = 3
print(mod1%mod2) #nilai sisa dari pembagi 4/3 = sisa 1

floor_1 = 4
floor_2 = 3
print(floor_1/floor_2)
print(floor_1//floor_2) #operasi ini membulatkan ke int terdekat dari hasil 1,3 paling dekat ke 1

#exponentiation 
exponen_1 = 2 
exponen_2 = 3
print(exponen_1**exponen_2)

#round make a float become the nearest int
rnd_2 = 2.51
rnd_1 = 2.49

hasil_rnd_1 = round(rnd_1)
hasil_rnd_2 = round(rnd_2)

print(hasil_rnd_1,type(hasil_rnd_1)) #int
print(hasil_rnd_2,type(hasil_rnd_2)) #int

#absolute (abs) membuat int / float menjadi nilau positif
num = -15.1

absolute_value = abs(num)
print(absolute_value, type(absolute_value)) # 15

#power (pow) melakukan hal yang sama dengan exponentiation
pow = pow(2,3)
print(pow)

#another pow 
pow2 = pow(2,2,3)
print(pow2) #melakukan exponentiation lalu modulo

#augmented assignment variable '<op>'="value yang mau di tambah"
var = 100
var /= 4
print(var,type(var)) #menambahkan tanpa perlu memanggil lagi 

var1 = 100
var1 = var1/4
print(var1) #hasilnya sama

