def pin_extractor(poems): #function, argumen poems
    secret_codes = [] #bikin list kosong buat secret code dijadiin 1 list
    for poem in poems: #loop poems 
        secret_code = '' #secret code string kosong
        lines = poem.split('\n') #lines split kata dari loop poem
        for line_index, line in enumerate(lines): #loop indexing
            words = line.split() #ambil kata dari loop line
            if len(words) > line_index: #kalo panjang kurang dijadiin 0
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor(poem))
print(pin_extractor([poem,poem2,poem3]))