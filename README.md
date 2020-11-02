# Tugas ini untuk melengkapi pertemuan ke 6 <br>
# Dan menjelaskan project <br>

![Logo](poto/logo.png)

**Nama :Risky HariAdi** <br>
**Nim  :312010124** <br>
**Kelas:TI.A1.20** <br>
**Tugas:Bahasa Pemrogramman** <br>

DAFTAR ISI
| No | Description | Link |
| ----- | ----- | ----- |
| 1 | Tugas Pertemuan 5 | [click here](#pertemuan-5---tugas)
| 2 | Tugas Pertemuan 6 - Lab 1 | [click here](#pertemuan-6---lab-1)
| 3 | Tugas Pertemuan 6 - Lab 1 dan 2 | [click here](#pertemuan-6---lab-1-2)
 
## Pertemuan 5 - Tugas

Pada pertemuan 5 Bahasa Pemrograman saya diberi tugas oleh Dosen untuk membuat Aplikasi Biodata Python (seperti Gambar dibawah ini) <br>
![pertemuan](poto/pertemuan5.png) <br>
Saat ini saya akan menjelaskan hasil dari tugas tersebut. <br>
Berikut *source code* nya atau Klik Link berikut ([pertemuan5 python](pertemuan5.py)): <br>
```python <br>

print("==============================") <br>
print("= NAMA    : Risky HariAdi     ") <br>
print("= NIM     : 312010124         ") <br>
print("= KELAS   : TI.20 A.1         ") <br>
print("==============================") <br>

`print("Please enter your full name : Risky HariAdi")` <br> 
`fullname=input()` <br>
`print("Please enter nickname : Risky")` <br> 
`nickname=input()` <br>
`print("Please enter your NPM : 312010124")` <br> 
`npm=input()` <br>
`print("Please enter place of birth : BEKASI")` <br> 
`pob=input()` <br>
`print("Please enter date of birth : 13")` <br> 
`date=input()` <br>
`print("Please enter your month of birth : July")` <br> 
`month=input()` <br>
`print("Please enter year of birth : 2000")` <br> 
`year=input()` <br>
`print("Please enter your phone number : 085282024179")` <br>
`phone=input()` <br>
`print("Please enter your address : Perumahan Graha Bagasasi")` <br> 
`address=input()` <br>

`dob=input("2020-year")` <br>

`print("\n\n Assalamu'alaikum. ")` <br>
`print("f\n Let me introduce my self, my name is {Risky HariAdi}, but you can call me {Risky}, my NPM {312010124}, I was born in {BEKASI} and iam {2020} years old, I am very glad if you want to invite my house in {Perumahan Graha Bagasasi}, So don't forget to call me before with the number {085282024179}, \n\n Thanks you very much ")` <br>

```
Berikut Penjelasannya :<br>
```python <br>
print("please enter your full name : ") <br>
``` <br>
Source code diatas berfungsi untuk mencetak hasil / output berupa **Please enter your full name :** ". <br>
 Untuk menampilkan output string, saya menggunakan *tanda petik dua* didalam fungsi print(), sedangkan jika saya ingin menampilkan output atau hasil berupa angka atau interger saya tidak perlu menggunakan *tanda petik dua*. Contohnya : <br>

```python

print("Nama saya adalah...") <br>
print(1234567) <br>
```
(Seperti gambar dibawah ini) <br> 
![outputprint](poto/outputprint.png )
* Untuk source code berikutnya adalah inputan atau membuat variable. seperti syntax dibawah ini : <br>

 ```python 

`fullname=input()` <br>
``` <br>
**Keterangan** : <br> 
`>Variable adalah sebuah wadah penyimpanan data pada program yang akan akan digunakan selama program itu berjalan. yang berfungsi sebagai variable dalam source code diatas adalah **fullname** . <br>
`>Fungsi **input()** adalah untuk memasukan nilai dari layar console di command prompt, lalu kemudian mengembalikan nilai saat kita menekan tombol enter *(newline)* <br> 
 `*(newline)*` <br>

[poto](poto/input.png)<br>

pada gambar di atas, hasil dari inputan tersebut berwarna *hijau* <br>

* Untuk memasukan perintah lain seperti *Nikname, NPM, Place Of Birth, Date Of Birth, Year Of Birth, Phone Number, and Addres* mengikuti perintah sama seperti memasukan *fullname* <br>

* Untuk menghitung rumus saya menggunakan variable *DOB* yaitu 2020 (Tahun sekarang) dikurangin dengan Year of Birt, pada source code berikut : <br>
``` python 
dob=input("2020-year") <br>
``` <br>
Pada syntax/source diatas, saya menggunakan variable (dob) dimana untuk menghitung umur (variable **age** pada output), yaitu dengan rumus pada variable *dob=input("2020-year")* <br>

* langkah kali ini saya akan menampilkan output yang diminta oleh dosen.output pertama yang diminta Dosen adalah menampilkan salam, yaitu dengan mengetikkan syntax/source code berikut : <br>

``` python

`print("\n\n Assalamu'alaikum. ")` <br>
``` <br>
 Keterangan : <br>
1. Fungsi **\n** pada source code di atas adalah untuk memberi baris baru / enter / *(newline)* <br>
2. Fungsi print() seperti dijelaskan pada point **Output** diatas
Hasil dari source code diatas adalah seperti gambar dibawah ini : <br>

![outputsalam](poto/outputsalam.png) <br>

``` python

print(f"Let me introduce my self, my name is {fullname}, but you can call me {nickname}, my NPM {npm}, I was born in {pob} and iam {dob} years old, I am very glad if you want to invite my house in {address}, So don't forget to call me before with the number {phone}, \n\n Thanks you ")
``` 
Keterangan : 
1. Fungsi huruf **f** pada perintah *print(f"....")* adalah fungsi print atau bisa memudahkan programer dalam mencetak statement dalam satu baris dibandingkan dengan metode yang lama yaitu memisahkan string dan variable dengan simbol koma( , ) atau plus ( + )<br>
2. sedangkan fungsi {} pada output tersebut adalah untuk menampilkan hasil dari variable<br>
Hasil dari output tersebut seperti berikut :<br>
![semuaoutput](poto/semuaoutput.png)

<br>
---
<br>

## Pertemuan 6 - Lab 1

Pada halaman ini (Tugas Pertemuan 6 - Lab 1) saya diberikan tugas oleh Dosen yaitu mempelajari operator aritmatika menggunakan bahasa Pemrograman pyhton. Berikut source code yang di berikan oleh dosen : <br>

``` python

#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator

`w, x, y, z = 10, 15, 20, 25`
`print(w, x, y, z)`
`print(w, x, y, z, sep=',')`
`print(w, x, y, z, sep='')`
`print(w, x, y, z, sep=':')`
`print(w, x, y, z, sep='.....')`

```

Oke, kali ini saya akan menjelaskan tentang materi yang di berikan oleh Dosen.<br>

* Penggunaan END
Penggunaan end digunakan untuk menambahkan karakter yang dicetak di akhir baris. secara default penggunaan end adalah untuk ganti baris. <br>

``` python

`print('A', end='')`
`print('B', end='')`
`print('C', end='')`

```

`> Penggunaan print () digunakan untuk mencetak output, seperti syntax dibawah ini :`

``` python

`print()`

```

`>Syntax dibawah ini digunakan untuk menampilkan output berupa string`

``` python

`print('X')`
`print('Y')`
`print('z')`

```

Hasil dari source code tersebut seperti gambar dibawah ini :<br>

![outputend](poto/outputend.png)

* Penggunaan separator

`>Pendeklarasian beberapa variable beserta nilainya`

``` python

w,x,y,z=10,15,20,25

```

`>Menampilkan hasil dari variable tiap-tiap variable`

``` python

`print(w,x,y,z)`

```

`>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah : (koma)`

``` python

`print(w,x,y,z,sep=",")`

```

`>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah`

``` python

`print(w,x,y,z,sep="")`

```

`>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah : (titik dua)`

``` python

`print(w,x,y,z,sep=":")`

```

`>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah`

-----

``` python

`print(w,x,y,z,sep="-----")`

```

* hasil dari syntax / source code diatas adalah seperti berikut ini : <br>

![hasilsyntax](poto/hasilsyntax.png)




<br>
<hr>
<br>

## Pertemuan 6 - Lab 1-2

* String Format<br>
String formatting atau pemformatan string memungkinan kita menyuntikkan item kedalam string dari pada kita mencoba menggabungkan string menggunakan koma atau string concatenation.<br>

* Penggunaan source code yang di berikan oleh dosen seperti berikut : <br>

![stringg](poto/stringg.png) <br>

``` python

#string format 1
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format 1
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))

```

<br>
Saat ini saya akan membahas satu persatu dari syntax yang telah diberikan oleh Dosen.<br>

1. **String Format 1** <br>
Pada syntax / source code strring format satu akan menampilkan output berupa 2 outputan.<br>
Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan untuk sebelah kanan akan menampilkan Operasi Aritmatika Pangkat.<br> 
Dengan ketentuan sebagai berikut, Operasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [bintang dua] )<br>
 Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10, dengan output  sebagai berikut : <br>

 ![Operasi Aritmatika Pangkat](poto/hasilstringg.png)
 
 2 ** String Format 2** <br>
 Pada syntax atau source code string format dua akan menampilkan output berupa 2 output'an juga (seperti String Format 1, yaitu kanan dan kiri )<br>
 Dengan ketentuan sebagai berikut : <br>
 >secara Default, **.format()** menggunakan rata kiri, angka ke kanan. kita dapat menggunakan opsi opsional <,^, atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan **.format()** sebagai berikut :<br> 

 ``` python

`print('{0:8} | {1:9}'.format('Nama orang','Jumlah'))`
`print('{0:8} | {1:9}'.format('Alek',3.))`
`print('{0:8} | {1:9}'.format('Jony',10))`

```

Hasil dari source code contoh diatas akan seperti berikut :<br>
![hhasilstring](poto/hhasilstring.png)
>Secara Default,**.format()** menggunakan rata text ke kiri, angka ke kanan, kita dapat menggunakan opsi opsional<,^,atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan **.format()** sebagai berikut : <br>

``` python

`print('{:<30}{:30}{:>30}'.format('kiri','tengah','kanan'))`
`print('{:<30}{:30}{:>30}'.format(7,20,34))`

```

Hasil dari source code contoh diatas akan muncul seperti ini :<br>
![sourcecode](poto/sourcecode.png)
<br><br>

String Format

![sstringg](poto/sstringg.png)


Untuk hasil dari String Format 2 adalah :<br>

![Output String Format 2](gambar/string2.PNG)

<br><hr><br>

# Pengertian print <br>

`print` <br>

* print("Tugas ini untuk melengkapi pertemuan 6") <br>

![print](poto/print.png) <br>

* Menampilkan hasil print<br>

![project](poto/project.png) <br>

Contoh syntax variabel : <br>

![hasilvariable](poto/hasilvariable.png)

**TERIMA KASIH** <br>

![kelar](poto/kelar.png)