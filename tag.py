#variabel dan type data
nama = "merry"
print(nama,type(nama))
umur = 18
print(umur,type(umur))
tinggi = 1.63
print(tinggi,type(tinggi))
ngoding = True
print(ngoding,type(ngoding))

print("="*60)

#operator aritmatika
# +,-,*,/,%,**,//

angka1 = 9
angka2 = 3
print(angka1 + angka2)
print(angka1 - angka2)
print(angka1 * angka2)
print(angka1 / angka2)
print(angka1 % angka2)
print(angka1 ** angka2)
print(angka1 // angka2)

print("="*60)

#menghitung gaji karyawan
nama = "merry"
gaji_pokok = 1000000
lama_lembur = 11
gaji_lemburPerjam = 5000
gaji_lembur = gaji_lemburPerjam * lama_lembur
gaji_kotor = gaji_pokok + gaji_lembur
pajak = 9/100
potongan = gaji_pokok*pajak
gaji_bersih = gaji_kotor - potongan

print("nama            :",nama)
print("Gaji pokok      = Rp ",gaji_pokok)
print("Gaji_lembur/jam = Rp",gaji_lemburPerjam)
print("Gaji lembur     = Rp",gaji_lembur)
print("Gaji kotor      = Rp",gaji_kotor)
print("pajak           = ",pajak)
print("potongan        = Rp",potongan)
print("Gaji bersih     = Rp", gaji_bersih)
