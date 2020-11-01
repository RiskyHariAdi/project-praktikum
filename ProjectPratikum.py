# Variabel adalah tempat menyimpan data

# menaruh / assignment nilai
a = 10
x = 5
panjang = 1000
print(0, 10**0)

# pemanggilan pertama
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang = ",panjang)

# penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 1000000 # ini boleh
nilaiZ = 17.5 # ini boleh

# pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai b = ", a)

# assignment indirect
b = a
print("Nilai b = ",b)

a=int(input("masukkan nilai a:"))
b=int(input("masukkan nilai b:"))
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil pejumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
