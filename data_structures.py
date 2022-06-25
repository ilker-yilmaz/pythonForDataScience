#########################################
# Data Structures
#########################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - List, Dictionary, Tuple, Set, Boolean (TRUE-FALSE): bool
# - list: liste
# - dictionary: sözlük
# - tuple: demet
# - set: küme

#########################################
# Veri Yapılarına Giriş ve Hızlı Özet
#########################################

# sayılar (Numbers): int, float, complex
y = 46
print(type(y))

#sayılar: float
x=10.3
type(x)

#sayılar: complex
x=2j+1
type(x)

#string
a="Hello ai era"
type(a)

#boolean
True
False
type(True)
5==4
3==2
1==1
type(3==2)

#Liste (list)

x=["btc", "eth", "xrp"]
type(x)

#sözlük (dictionary)
x={"name":"Peter", "Age":36}
type(x)

# Tuple (demet)
x=("python", "ml", "ds")
type(x)

# Set (küme)
x={"python", "ml", "ds"}
type(x)

#Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


#########################################
# Sayılar (Numbers): int, float, complex
#########################################

a=5
b=10.5

a*3
a/7


#########################################
# Tipleri değiştirmek
#########################################

int(b)
float(a)


#########################################
# karakter dizileri (Strings)
#########################################

print("Hello ai era")

name="Peter"
print(name)

long_str="""    Hello ai era    """
print(long_str)

name[0]

#########################################
# karakter dizilerinde slice işlemi
#########################################

name[0:3]
long_str[0:3]

#########################################
# string içerisinde karakter sorgulama
#########################################


"veri" in long_str
"Veri" in long_str


#########################################
# String (karakter dizisi) metodları
#########################################

dir(long_str)

#########################################
# len() metodu
#########################################

name = "ilker"
print(type(name))
print(type(len))
print(len(name))

#########################################
# upper() & lower(): küçük-büyük dönüşümleri
#########################################

print("ilker".upper())
print("ilker".lower())


#########################################
# replace: karakter değiştirir
#########################################

merhaba = "merhaba ilker"
print(merhaba.replace("a", "b"))

#########################################
# split: karakter dizisini bölüyor
#########################################

print("Hello ai era".split())

#########################################
# strip: karakter dizisini kırpar
#########################################

print("ofofofo".strip("o"))


#########################################
# capitalize: ilk karakteri büyük yapar
#########################################
print("deniz".capitalize())



