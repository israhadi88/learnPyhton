cities = ['Jakarta','Londo','Tokyo']
print(cities[0])

name = 'Israhadi Tri Hutama'
print(list(name)) 

cities = ['Jakarta','London','Tokyo']
print(cities)
print(len(cities))#total in list
cities[0] = 'Bangkok' #update list based on index, ganti value 0 yang lama
print(cities)
del cities[0] #delete index 0 value in list 
print(cities)

cities = ['Jakarta','London','Tokyo']
check = 'Jakarta' in cities #checking jakarta in cities list, output boolean
print(check)

#cara access by index di dalam nested list 
developer = ['Israhadi',29,['Python','Javascript','Go']]
print(developer[2][0])

developer = ['Israhadi',30,'Javascript']
name, age, language = developer #unpacking value of list, deklarasi ke variable
print(name)

developer = ['Brodo', 34, 'Rust Developer']
name, *test = developer #unpacking value of list, pake asterik jika ingin semuanya

print(name)
print(test)

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:3]) #akses index list using slicing | []'Cookies','Ice Cream']

#Common method used for list

#1. .append() used to add an item to the end of list
app_list = [1,2,3,4,5]
app_list.append(6) #ini menambahkan di akhir list dengan append
print(app_list)

#bisa nenambahkan list juga di dalam list
app_list2 = [1,3,5,7]
evenNumber = ([2,4,6,8])
app_list2.append(evenNumber)
print(app_list2)#[1, 3, 5, 7, [2, 4, 6, 8]]

#bisa juga nambahin list tanpa harus gabung dalam list
ext_list = [1,2,3,5]
extend = [2,4,6]
ext_list.extend(extend)
print(ext_list) #[1, 3, 5, 2, 4, 6] tapi tetap gaberurutan dan ada double counting

#pakai insert() kalo mau nambahin sesuai index
inst_list = [1, 2, 3, 5]
inst_list.insert(3,4)
print(inst_list) #3 indextnya 4valuenya (masukkan 4 pada list ini di index ke-3)

#pakai remove() untuk menghapus value yang diinginkan, tapi cuma value yang paling depan dan
#gak semua value yang sama
rmv_list = [1,2,3,4,5,5,6,6,6,]
rmv_list.remove(5)
print(rmv_list)

#pakai pop() untuk menghapus semua value berdasarkan index
pop_list = [1,2,3,4,5,6,7,7,7,7,8]
pop_list.pop(3) #menghapus index 3 = 4
print(pop_list)

pop_list2 = [1,2,3,4,5,6,7,7,7,7,8]
pop_list2.pop() #menghapus index terakhir
print(pop_list2)

#gunakan clear() jika ingin mengosongkan list
clr_list = [1,2,3,4,5,6]
clr_list.clear()
print(clr_list) # ilang []

#gunakan sort() untuk mengurutkan value dalam list
sort_list = [1,3,2,5,4,6,7,9,8]
print(sort_list) #list seadanya sesuai yang di declare
sort_list.sort()
print(sort_list) #sudah di sorting ascending
sort_list.sort(reverse=True)
print(sort_list) #ini sorting descending

#gunakan sorted() untuk sorting di list baru, bisa pakai reverse juga
soso = [2,3,1,4,7,6,9,8]
sorted_list = sorted(soso)
print(sorted_list)
sorted_list = sorted(soso, reverse=True)
print(sorted_list)

#reverse() juga bisa dipakai sendiri buat membalikkan value
rere = [1,2,3]
rere.reverse()
print(rere) #[3, 2, 1]

