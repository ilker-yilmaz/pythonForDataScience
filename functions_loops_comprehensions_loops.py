#################################################
# Fonksiyonlar, Koşullar, Döngüler, Comrehensions
#################################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comrehensions (Comprehensions)


##########################
# Fonksiyonlar (Functions)
##########################
# - Fonksiyonlar bir programda bir işi yürütmek için kullanılan bir yapıdır.
# - Belirli görevleri yerine getirmek için kullanılan kod parçalarıdır.

#########################
# Fonksiyon Okuryazarlığı
#########################

print("ilker")

print("ilker", "yılmaz", sep="___")


############################
# Fonksiyonların Tanımlanması
#############################

def calculate_age(year):
    return 2022 - year


print(calculate_age(2000))


# iki argüman alan fonksiyonların tanımlanması
def calculate_age_2(name, year):
    return f"{name} is {2022 - year} years old"


print(calculate_age_2("ilker", 2000))


############################
# Docstring (Documentation String)
#############################

# fonksiyonlarımıza herkesin anlayabileceği
# ortak bir dil ile bilgi notu ekleme yoludur.

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float
    """
    return arg1 + arg2


print(help(summer))


######################################
# Fonksiyonların Statement/Body Bölümü
######################################

# def fonksiyon_adi(arg1, arg2):
#     statements (function body)


def say_hello(string):
    print("Hello")
    print("Hi")
    print(string)


say_hello("ilker")


def multiplication(arg1, arg2):
    c = arg1 * arg2
    print(c)


multiplication(2, 3)

# girilen değerleri bir liste içinde saklayacak fonksiyon

liste = []


def list_creator(arg1, arg2):
    for i in range(arg1, arg2):
        print(i)
        liste.append(i)
        print(liste)
    return liste


list_creator(1, 10)


###################################################################
# Ön Tanımlı Argümanlar/Parametreler (Default Arguments/Parameters)
###################################################################

def divide(arg1, arg2):
    return arg1 / arg2


print(divide(10, 2))


def divide1(arg1, arg2=1):
    return arg1 / arg2


print(divide1(10))
print(divide1(10, 3))


############################################
# Ne zaman fonksiyon Yazma ihtiyacımız olur?
############################################

# Don't Repeat Yourself (DRY)
# Kendini tekrar etme..

def calculate_age(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate_age(10, 20, 30)


######################################################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################################################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(76,100,67) * 10


def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


a = calculate(76, 100, 67) * 10
print(a)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output


type(calculate(76, 100, 67))
varm, moisture, charge, output = calculate(76, 100, 67)

print(varm, moisture, charge, output)


#########################################
# Fonksiyon İçerisinden Fonksiyon Çağırma
#########################################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(76, 100, 67) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(10, 100)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(76, 100, 67, 100)

#######################################################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################################################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(10, 20)

#######################
# Koşullar (Conditions)
#######################

# True-False'u Hatırlayalım.
1 == 1
2 == 2

# if
if 1 == 1:
    print("1 == 1")

# elif
if 1 == 2:
    print("1 == 2")
elif 1 == 1:
    print("1 == 1")

# else
if 1 == 2:
    print("1 == 2")
else:
    print("1 != 2")

# if-else-if-else
if 1 == 1:
    print("1 == 1")
elif 1 == 2:
    print("1 == 2")
elif 1 == 3:
    print("1 == 3")
else:
    print("1 != 1, 2 veya 3")


def number_check(number):
    if number == 1:
        print("1")
    elif number == 2:
        print("2")
    elif number == 3:
        print("3")
    else:
        print("1, 2 veya 3 değil")


print(number_check(1))

##################
# Döngüler (LOOPS)
##################

# for loop
students = ["ilker", "fırat", "mehmet", "ahmet", "resul", "furkan", "gaffar"]
for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print((salary * 20) / 100 + salary)


def new_salary(salary, rate):
    return int((salary * rate) / 100 + salary)


print(new_salary(1000, 20))

for salary in salaries:
    print(new_salary(salary, 20))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

###########################
# Uygulama - Mülakat Sorusu
###########################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# aslında anlatılmak istenen şey:
# tek indekstekileri küçük harflerle değiştir
# çift indekstekileri büyük harflerle değiştir

def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for i in range(len(string)): # string'in uzunluğu kadar döngü oluştur
        if i % 2 == 0: # eğer indeksteki sayı çift ise
            new_string += string[i].upper() # çift indeksteki sayıyı büyük harfe çevir
        else:
            new_string += string[i].lower() # tek indeksteki sayıyı küçük harfe çevir
    return new_string


mulakatcevabi = alternating("hi my name is john and i am learning python")

print(mulakatcevabi)
