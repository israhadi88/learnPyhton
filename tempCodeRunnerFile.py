def pengelompokan(n):
    numbers = range(1,n+1)
    even_list = [num for num in numbers if num % 2 == 0]
    odd_list = [num for num in numbers if num % 2 != 0]
    print(f'odd: {odd_list}')
    print(f'even: {even_list}')
pengelompokan(6)