#TEBAK ANGKA
#IQBAL SIGMA
import random
angka = random.randint(1, 10)

nama = input("Hai, Siapa Namamu? ")
total_tebakan = 0
print('Hi '+ nama + ' aku sedang memikirkan angka dari 1 sampai 10, coba tebak:')

while total_tebakan < 5:
    tebakan = int(input())
    total_tebakan += 1
    if tebakan < angka:
        print('Tebakanmu terlalu rendah')
    if tebakan > angka:
        print('Tebakanmu terlalu tinggi')
    if tebakan == angka:
        break
if tebakan == angka:
    print('Kamu berhasil menebak dalam ' + str(total_tebakan) + ' percobaan!')
else:
    print('Kamu tidak berhasil menebak, angka yang benar adalah ' + str(angka))
