jumlah_orang = int(input('Masukkan Jumlah orang:'))
daftar_umur = []

for i in range(jumlah_orang):
    age = int(input(f'Masukkan umur orang ke{i+1}:'))
    daftar_umur.append(age)
    #if dalam loop
    if age >= 18:
        print('Status: Anda cukup umur')
    elif age >13:
        print ('Status: Anda Remaja')
    else:
        print('Anda Anak-anak')
    print (f'Data umur anda {age}, telah disimpan')
    print('---------------------------------')

print(f'\n Total data valid yang dimasukkan {len(daftar_umur)}')
print(f'Daftar umur: {daftar_umur}')