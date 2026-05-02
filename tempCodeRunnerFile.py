def number_pattern(n):
    if not isinstance (n,int):
            return 'Agument must be an integer value.'
    if n < 1:
            return ('Argument must be an integer greater than 0.')
    numbers = []
    for num in range(1, n + 1):
        numbers.append(str(num))
    
    format =' '.join(numbers)
    return format
print(number_pattern(4))
print(number_pattern(12))
print(number_pattern('a'))
print(number_pattern(0))