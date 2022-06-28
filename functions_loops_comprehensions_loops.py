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


