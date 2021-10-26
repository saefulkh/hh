

print('\n====belajar python====\n')
print("hello")
print("world")
print("hello world")

a = 10
# comment
print(a)

#CARA COMPILE BUKA TERMINAL DAN TULIS -m py_compile nama.py

a = 10
x = 5
panjang = 1000
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)

# a = 10, a adalah variabel dengan nilai 10

print('\n======TIPE DATA======\n')

# tipe data: angka satuan yang ga ada komanya (integer)
data_integer = 1000
print(type(data_integer))
print("data:", data_integer,)
print("- bertipe:", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe :", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe :", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe :", type(data_bool))

print('\n======TIPE DATA KHUSUS=======\n')

## TIPE DATA KHUSUS

# bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe :", type(data_complex))

# TIPE DATA DARI BAHASA C

#from ctypes import  c_double 

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))

print('\n====BELAJAR CASTING====\n')
#  BELAJAR CASTING
# merubah dari satu tipe ke tipe lain
# tipe data =  int, float, str, bool

# int
print('========int=======')
data_int = 9
print("data = ",data_int,",type=", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int= nol
print("data =",data_float, ",type =", type(data_float))
print("data =",data_str, ",type =", type(data_str))
print("data =",data_bool, ",type =", type(data_bool))

# float
print("=========float========")
data_float = 9.5
print("data = ",data_float,",type=", type(data_float))

data_int = int(data_float) # akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float= nol
print("data =",data_int, ",type =", type(data_int))
print("data =",data_str, ",type =", type(data_str))
print("data =",data_bool, ",type =", type(data_bool))


# bool
print("=========bool========")
data_bool = False
print("data = ",data_bool,",type=", type(data_bool))

data_int = int(data_bool) # False bernilai 0 true bernilai 1
data_str = str(data_bool) # akan dibacca sebagai karakter
data_float = float(data_bool)
print("data =",data_int, ",type =", type(data_int))
print("data =",data_str, ",type =", type(data_str))
print("data =",data_float, ",type =", type(data_float))


# str
print("=========str========")
data_str = "10"
print("data = ",data_str,",type=", type(data_str))

data_int = int(data_str) # str harus angka
data_bool= bool(data_str) # false jika kosong
data_float = float(data_str) # str harus angka
print("data =",data_int, ",type =", type(data_int))
print("data =",data_bool, ",type =", type(data_bool))
print("data =",data_float, ",type =", type(data_float))

print("\n====BELAJAR INPUT DATA USER====\n")
#biar keren saya ubah jadi paswod jawab aja sembarang

## BELAJAR INPUT DATA USER

# data yang di masukan pasti string
#data = input("masukan data: ")
data = input("masukan nama anda: ")

print("data = ",data,",type = ", type(data))

# jika kita ingin mengambil int, maka data harus angka

#angka = float(input("masukan angka: "))
angka = float(input("masukan paswod angka saja: "))
print("data = ",angka,"type =",type(angka))
angka = int(input("ulangi paswod anda : "))
print("data = ",angka,"type =",type(angka))

# bagaimana dengan boolean akan false jika nilai yang d masukan 0

bier = bool(int(input("jawab pertanyaan 12 + 3 = ")))
print("data =",bier,",type =", type(bier))

print('\n=====OPERASI ARITMATIKA=====\n')

##  OPERASI ARITMATIKA
# +,-,*,/,**,%,//
a = 10
b = 3

# operasi tambah + 
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

print('\n====PRIORITAS OPERASI====\n')

# PRIORITAS OPERASI 

#PENDAHULUAN DALAM ARITMATIKA 
# ()
# EXSPONEN **
# PERKALIAN TERMASUK PEMBAGIAN dan teman2 * / ** % //
# PERTAMBAHAN TERMASUK PENGURANGAN
x = 3
y = 2
z = 4 

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '%' ,z, '//', x, '=', hasil)

hasil = x + y * z
print (x,'+', y, '*' ,z,'=', hasil )
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print ('(',x,'+', y,') *' ,z,'=', hasil )


print('\n====LATIHAN ARITMATIKA=====')
# LATIHAN ARITMATIKA 

#PROGRAM KONVERSI CELCIUS KE SATUAN LAIN

print("\nprogram konversi temperatur\n")

celcius = float(input('masukan suhu dalam celcius:'))
print("suhu adalah" , celcius, "celcius")


# reamur
reamur = (4/5)*celcius 
print("suhu dalam reamur adalah",reamur,"reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit,"fahrenheit")


# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"kelvin")



print('====LATIHAN====')
# LATIHAN =============



# fahrenheit ke kelvin
fahrenheit = float(input('masukan suhu dalam fahrenheit:'))
celcius = 5/9*(fahrenheit-32)
kelvin = celcius + 273
print("suhu fahrenheit dalam celcius adalah",celcius,"celcius")
print("suhu fahrenheit dalam kelvin adalah",kelvin,"kelvin")

# kelvin ke fahrenheit
kelvin = float(input('masukan suhu dalam kelvin:'))
celcius = kelvin - 273
fahrenheit = ((9/5 )* celcius )+ 32
print("suhu kelvin dalam celcius", celcius,"celcius")
print("suhu kelvin dalam fahrenheit",fahrenheit,"fahrenheit")




print('\n====OPERASI KOMPARASI====\n')
# ====== OPERASI KOMPARASI =====
# Setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('========lebih besar dari======== (>)')
hasil = a > 3
print(a, '>', 3, '=',hasil)
hasil = b > 3
print(b, '>', 3, '=',hasil)
hasil = b > 2
print(b, '>', 2, '=',hasil)

# kurang dari <
print('========kurang dari========= (<)')
hasil = a < 3
print(a, '<', 3, '=',hasil)
hasil = b < 3
print(b, '<', 3, '=',hasil)
hasil = b < 2
print(b, '<', 2, '=',hasil)

# lebih dari samadengan >=
print('========lebih dari samadengan========= (>=)')
hasil = a >= 3
print(a, '>=', 3, '=',hasil)
hasil = b >= 3
print(b, '>=', 3, '=',hasil)
hasil = b >= 2
print(b, '>=', 2, '=',hasil)

# kurang dari samadengan <=
print('========kurang dari samadengan========= (<=)')
hasil = a <= 3
print(a, '<=', 3, '=',hasil)
hasil = b <= 3
print(b, '<=', 3, '=',hasil)
hasil = b <= 2
print(b, '<=', 2, '=',hasil)

#  samadengan ==
print('========samadengan========= (==)')
hasil = a == 4
print(a, '==', 4, '=',hasil)
hasil = b == 4
print(b, '==', 4, '=',hasil)
hasil = b == 2
print(b, '==', 2, '=',hasil)

#  tidak samadengan !=
print('========samadengan========= (!=)')
hasil = a != 4
print(a, '!=', 4, '=',hasil)
hasil = b != 4
print(b, '!=', 4, '=',hasil)
hasil = b != 2
print(b, '!=', 2, '=',hasil)

# is adalah membandingkan objek, / sebagai objek identity

'''PS D:\alfatih45> python
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> type(x)
<class 'int'>
>>> id(x) 
1925613289840
>>> hex(id(x)) 
'0x1c0577f0170'
>>> y = 10
>>> hex(id(y)) 
'0x1c0577f0210' '''
x = 5 # ini adalah assignment membuat object
y = 5
print('======komparasi is=======')
print('nilai x =,',x,',id =',hex(id(x)))
print('nilai y =,',y,',id =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id =',hex(id(x)))
print('nilai y =,',y,',id =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)


# komprasi is not
print('======is not=====')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =,',x,',id =',hex(id(x)))
print('nilai y =,',y,',id =',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =,',x,',id =',hex(id(x)))
print('nilai y =,',y,',id =',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)


print('====OPERASI LOGIKA ATAU BOOLEAN====')
# OPERASI LOGIKA ATAU BOOLEAN

# NOT, OR, AND, XOR


# NOT
print('======NOT======')
a = True
c = not a

print('data a =',a)
print('-----------NOT')
print('data c =',c)

print('======NOT======')
a = False
c = not a

print('data a =',a)
print('-----------NOT')
print('data c =',c)

print('=======OR======')
# OR jika salah satu true maka hasilnya true
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,' =',c)
a = True
b = False
c = a or b
print(a,' or',b,'=',c)
a = True
b = True
c = a or b
print(a,' or',b, ' =',c)


# AND jika dua buah nilai tru, maka hasil true
print('======and======')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,' =',c)
a = True
b = False
c = a and b
print(a,' and',b,'=',c)
a = True
b = True
c = a and b
print(a,' and',b, ' =',c)

# XOR akan true jika salah satu true sisanya false
print('======xor======')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' xor',b, ' =',c)

print('\n===LATIHAN LOGIKA DAN KOMPARASI===\n')
# latihan  logika dan komparasi

# membuat gabungan area rentang angka
# ++++++3----------10+++++++
print('++++++3----------10+++++++')
inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# ++++++3---------
# memeriksa angka kurang dari 3
print('memeriksa angka kurang dari 3')
isKurangDari = (inputUser <3)
print("kurang dari 3  =", isKurangDari)

# ---------10+++++++++
# memeriksa angka lebih dari 10
print('memeriksa angka lebih dari 10')
isLebihDari = (inputUser > 10)
print("lebih dari 10  =",isLebihDari)

# +++++++3--------10++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan:", isCorrect)



#--------3++++++++10-------
# ini khasus irisan
print("\n",10*"=","\n")
print('--------3++++++++10-------')
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))


# ------3++++++++++++++
# ini lebih dari 3
isLebihDari = inputUser > 3
print("lebih dari 3 =",isLebihDari)


# ++++++++++10----------
# ini kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 =",isKurangDari)

#--------3++++++++10-------
isCorrect = isKurangDari and isLebihDari
print("angak yang anda masukan:",isCorrect)


# LATIHAN
#--------0+++++++5--------8+++++++11------
# masukan angka yang bernilai lebih dari 0 dan kurang dari 5 
# atau masukan angka yang bernilai lebih dari 8 dan kurang dari 11 
#-------0++++++
#ini lebih dari 0
#inputUser = float(input("masukan angka yang bernilai\nlebih dari 0\ndan\nkurang dari 5\natau angka yang bernilai\nlebih dari 8\ndan\nkurang dari 11\n:"))
#isLebihDari = inputUser > 0
#print("lebih dari 0 =",isLebihDari)

#++++++5-----
#ini kurang dari 5
#isKurangDari = inputUser < 5
#print("kurang dari 5 =",isKurangDari)

#------8+++++
#ini lebih dari 8
#isLebihDari =inputUser > 8
#print("lebih dari 8 =",isLebihDari)

#++++11----
#kurang dari 11
#isKurangDari = inputUser < 11
#print("kurang dari 11 =",isKurangDari)

#--------0+++++++5--------8+++++++11------
#isCorrect = isLebihDari and isLebihDari or isLebihDari and isKurangDari
#print("angka yang anda masukan:",isCorrect)














#print('\n',10*'=','\n')





#++++++++0-------5++++++++8-------11++++++
# masukan angka yang bernilai kurang dari 0 atau lebih besar dari 5 dan kurang dari 8 atau lebih besar dari 11
#++++0---
# ini kurang dari 0
#inputUser = float(input("masukan angka yang bernilai\nkurang dari 0\natau\nlebih besar dari 5\ndan\nkurang dari 8\natau\nlebih besar dari 11\n:"))
#isKurangDari = inputUser < 0
#print("kurang dari 0 =",isKurangDari)

#----5++++
#ini lebih dari 5
#isLebihDari = inputUser > 5
#print("lebih dari 5 =",isLebihDari)

#++++++8------
#ini kurang dari 8
#isKurangDari = inputUser < 8
#print("kurang dari 8 =",isKurangDari)

#-----11+++++
#ini lebih dari 11
#isLebihDari = inputUser > 11
#print("lebih dari 11 =",isLebihDari)

#++++++++0-------5++++++++8-------11++++++
#isCorrect = isKurangDari or isLebihDari and isKurangDari or isLebihDari
#print("angka yang anda masukan:",isCorrect)


print("\n",10*"=","\n")
print('===OPERASI BITWISE===')
# operasi bitwise , operasi biner, binary

a = 9
b = 5

#bitwise or (|)
c = a | b
print('\n======OR======')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise and (&)
c = a & b
print('\n======AND======')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise xor (^)
c = a ^ b
print('\n======XOR======')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n======XOR======')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))
print('-------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,', binary :',format(e^d,'08b'))


print('\n=====shiftting======\n')
# SHIFTTING============

# shift right (>>)
c = a >> 2
print('\n======>>======')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))


# shift right (<<)
c = a << 2
print('\n======<<======')
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',c,',binary :',format(c,'08b'))


print('\n====OPERATOR ASSIGNMENT====\n')
## operator assignment
# operasi yang dapat di lakukan dengan penyingkatan

#operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print("nilai a =",a)

#a = a + 1 # dapat di singkat menjadi 
a += 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 #artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 #artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi",a)

a /= 2 #artinya adalah a = a / 5
print("nilai a /= 5, nilai a menjadi",a)

b = 10
print("\nnilai b =",b)
b %= 3
print("nilai b %= 3, nilai a menjadi",b)

b = 10
print("\nnilai b =",b)
b //= 3
print("nilai b %= 3, nilai a menjadi",b)

a = 5 # ini adalah assignment
print("nilai a =",a)
a **= 3
print("nilai b **= 3, nilai a menjadi",a)


print('\n====OPERASI BITWISE DI ASSIGNMENT====\n')
# operasi bitwise di assignment
# or |
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

c = False
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# and &
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi",c)

c = True
print("\nnilai c =",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)

# xor ^
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi",c)

c = True
print("\nnilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)


# geser geser (>>,<<)
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))



print('\n',10*'=','\n')
print('====PENGENALAN STRING====\n')
# PENGENALAN STRING
data = "ini adalah string"
print(data)
print(type(data))

# 1 Cara membuat string
'''
-dengan menggunakan single quote '...'
-dengan menggunakan double quote "..."
'''
data = 'menggunakan single quote'
#print(data)

data ="menggunakan double quote"
print(data)

print('"hallo, apa kabar"')
print("'hallo, apa kabar'")


# oprrasi dan manipulasi string
print('\n====OPERASI DAN MANIPULASI STRING====\n')

# 1. menyambung string (concatenate)
print('====menyambung string====')
nama_depan = "Azzam"
nama_tengah = "Al"
nama_akhir = "Fatih"
nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string (len)
print('====menghitung panjang====')
panjang = len(nama_lengkap)
print("panjang dari "+ nama_lengkap + " = " + str(panjang))

# operator untuk string logika (in, not in)
print('====operator untuk string====')
d = "L"
status = d in nama_lengkap
print( d + " ada di " + nama_lengkap + " = " + str(status))# mengecek komponen

D = "l"
status = D in nama_lengkap
print( D + " ada di " + nama_lengkap + " = " + str(status))# mengecek komponen 

d = "L"
status = d not in nama_lengkap
print( d + " tidak ada di " + nama_lengkap + " = " + str(status))# mengecek komponen 

# mengulang string
print('====mengulang string====')
print("wk"*10) # di balik (10*"wk")

#indexing "mengambil data dari string" index mulai dari 0
print('\n====indexing []====\n')# di mulai dari 0
print("index ke-0 : " + nama_lengkap [0])
print("index ke-1 : " + nama_lengkap [1])
print("index ke-(-1) : " + nama_lengkap [-1])
print("index ke-(-2) : " + nama_lengkap [-2])
print("index ke-[0:4] : " + nama_lengkap [0:5])# 0 sampai sebelum 5
print("index ke-[6:13] : " + nama_lengkap [6:14])# 0 sampai sebelum 5
print("index ke-[0,2,4,6,8,10,12,] : " + nama_lengkap [0:13:2])# 0 sampai 14 dengan increatmen (di loncatin) 2


# item paling kecil 
print('===item paling kecil (min)===')
print("paling kecil : " + min (nama_lengkap))
#item paling besar
print('===item paling besar (max)')
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII CODE untuk sepasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

## OPERATOR DALAM BENTUK METHOD
print("\n",10*"=","\n")

print('\n====OPERATOR DALAM BENTUK METHOD====\n')

# .count menghitung dalam 1 karakter peletakanya setelah data di tambah . 
print('====.coun')
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data +" = " + str(jumlah))

# merubah case dari string
# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool casting ke str 
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool 
print(salam + " is upper = "+ str(apakah_upper))

# isalpha   (untuk mengecek semuanya huruf)
apakah_huruf = salam.isalpha()
print(salam + " is alpha = " + str(apakah_huruf))

# isalnum   (untuk mengecek huruf dan angka)
apakah_isalnum = salam.isalnum()
print(salam + " is alnum = "  + str(apakah_isalnum))

# isdecimal (untuk mengecek angka saja)
apakah_isdecimal = salam.isdecimal()
print(salam + " is decimal = " + str(apakah_isdecimal))

# isspace   (untuk mengecek spasi, tab, newline \n)
apakah_isspace = salam.isspace()
print(salam + " is space = " + str(apakah_isspace))

# istitle   (untuk mengecek semua kata di mulai dengan huruf besar)
judul = "Belajar Python Pemula"
cek_title = judul.istitle()
print(judul + " is title = " + str(cek_title))


# ngecek komponen startswith() endswith()
cek_start = "Ahmad Azzam".startswith("Ahmad")
print("star = " +str(cek_start))
cek_end = "Ahmad Azzam".endswith("Azzam")
print("end = " + str(cek_end))

## penggabungan komponen .join() .split()
pisah = ['ahmad','azzam','alfatih']
gabungan = ','.join(pisah)# bisa di ganti dengan spasi {' '.join}
print(pisah)
print(gabungan)
print(gabungan.split(','))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)# bisa d tambahin objek .rjust(10,"=")
print("="+kanan+"=")
kanan = "kanan".rjust(10,"=")
print("="+kanan+"=")

kiri = "kiri".ljust(10)
print("="+kiri+"=")

tengah = "tengah".center(10,"=")
print("="+tengah+"=")

# kebalikannya .strip()
tengah = tengah.strip("=")
print("'"+tengah+"'")
