my_str_3 = """Multiline
string"""

print(my_str_3)

#using backslash to print a single or double qoute
print('it\'s rainy day')
print("\"Hello\"")

#using in to check word or character in string: output boolean
checking_containt = "Hello sunday"
print('Hello' in checking_containt)
print('Rainy' in checking_containt)

#using len to get lenght of strings
my_str = 'Hello world'
print(len(my_str))  # 11 

#indexing string, counting start from 0 
print(my_str[2]) #l

#indexing string, start from the two from last
minus = 'satu'
print(minus[-2])

#string is immutable in python but can reassign them
x = 2
print(x) 
#reassign
x = 3
print(x)
print(x)

#Examples of other immutable data types in Python are:
#integer, float, boolean, tuple, and range. 

#2. string concatenation & interpolation
#concatetination 
#combine multiple string is together, this process called concatenation

#example
a = 'Israhadi'
b = 'Hutama'
#concate with +
print(a+' '+b)

#if try concate string with int or somthing else
#get a TypeError
a = 'Israhadi'
b = 29
print(a +' ' +b)

#concate different data with function
a = 'Israhadi'
b = 29
print(a +' ' +str(b)) #making int into str

#example 2
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += ' ' + str(age)  # Append the age as string

print(name_and_age)  # John Doe26

#interpolation
#by using the f or called f-sting we can making variable into string

#example
name = 'Israhadi'
age = 29

name_age = f'my name is: {name} and i am {age} years old'
print(name_age)

#LESSON 3 Slicing 
#access string with specific part of it 
#string[start:stop]

#example
slc = 'israhadi'
print(slc[1:3])

#or start to selected index
slc2 = 'israhadi'
print(slc2[:4])

#start from selected index to end
slc3 = 'israhadi'
print(slc3[4:])

#we can add some step
slc4 = 'israhadi'
print(slc4[0:9:2])

#or step backward
slc4 = 'israhadi'
print(slc4[::-1])

#LESSON 4 COMMON STRING METHOD
cmmn = 'Hello World'
print(cmmn.lower()) #to lowercase
print(cmmn.upper()) #to uppercase

cmmn2 = 'Hello World'
print(cmmn2.strip()) #make into single word space
print(cmmn2.replace('Hello','hi')) #replace string to 
print(cmmn2.split()) #split into list

cmmn3 = cmmn2.split()
print(' '.join(cmmn3)) #list (immutable into string)