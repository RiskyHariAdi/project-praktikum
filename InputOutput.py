# input output file

"""

w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru 
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data diakhir baris
r+ = write and read mode

"""

# membuat file dalam bentuk text 

file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan menggunakan data python")
file.write("\nHallo perkenalkan nama saya ikky")
file.write("\nSaya sekolah di UNIVERSITAS PELITA BANGSA")
file.write("\nSaya masih belajar")

file.close()

# membaca file text diterminal / open file text

file2 = open("data.txt",'r')

#print(file2.read(10)) / membaca baris 

print(file2.readline())

print(file2.readline())

file2.close()

# appending mode / meneruskan text file (apabila diubah yang dalam buka & kurung akan tertimpa)

file3 = open("data.txt", 'a')

file3.write("\nDan masih belom bisa atuh")

file3.close()

