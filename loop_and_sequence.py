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

