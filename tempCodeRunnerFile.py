numbers = [1,2,3,4,5]
def square(num):
    return num**2

squared_number = list(map(square,numbers))
print(squared_number)