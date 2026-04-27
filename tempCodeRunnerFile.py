languages = ['Spanish','English','Indonesia','Chinese']
x = dict(enumerate(languages))
for index, language in enumerate(languages):
    print(f'index {index} and language {language}')
print(x,type(x))