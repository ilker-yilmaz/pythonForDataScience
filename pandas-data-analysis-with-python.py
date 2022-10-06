########
# Pandas
########

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation and Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

###############
# Pandas Series
###############

# pandas serileri tek boyutlu ve index bilgisi barındıran bir veri tipidir.
# pandas dataframe ise çok boyutlu ve index bilgisi barındıran bir veri tipidir.

import pandas as pd # pandas kütüphanesini pd olarak import ettik.

# pandas serisi oluşturmak için pd.Series() fonksiyonunu kullanırız.
pd_series = pd.Series([1, 2, 3, 4, 5]) # bu liste üzerinden bir pandas serisi oluşturulacak.
print("pd_series:\n",pd_series)
print("type of pd_series: ",type(pd_series))
print("pd_series.index: ",pd_series.index) # pandas serisinin index bilgisi.
print("pd_series.values: ",pd_series.values) # pandas serisinin değer bilgisi. bu bir numpy array'idir.
print("pd_series.dtype: ",pd_series.dtype) # pandas serisinin veri tipi.
print("pd_series.ndim: ",pd_series.ndim) # pandas serisinin boyut sayısı. bu seri tek boyutludur ve index bilgisi vardır.
print("pd_series.head: ",pd_series.head(3)) # pandas serisinin ilk 3 elemanını gösterir.
print("pd_series.tail: ",pd_series.tail(3)) # pandas serisinin son 3 elemanını gösterir.


# pandas serisi oluştururken index bilgisi de verilebilir.
pd_index_series = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
#print("pd_index_series:\n",pd_index_series)
#print("type of pd_index_series: ",type(pd_index_series))


###########################
# Veri Okuma (Reading Data)
###########################

import pandas as pd

# csv dosyası okuma
df = pd.read_csv("datasets/Advertising.csv")
print("df:\n",df)
print("df.head():\n",df.head()) # ilk 5 satırı gösterir.

#########################################
# Veriye Hızlı Bakış (Quick Look at Data)
#########################################

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic") # seaborn kütüphanesindeki titanic veri setini yükler.
print("titanic.head():\n",titanic.head()) # ilk 5 satırı gösterir.
print("titanic.tail():\n",titanic.tail()) # son 5 satırı gösterir.
print("titanic.shape: ",titanic.shape) # veri setinin boyut bilgisi.
print("titanic.info:\n",titanic.info()) # veri setinin bilgileri.
print("titanic.columns: ",titanic.columns) # veri setinin sütun bilgileri.
print("titanic.index: ",titanic.index) # veri setinin index bilgileri.
print("titanic.describe():\n",titanic.describe().T) # veri setinin istatistiksel bilgileri. sonuna da .T ekleyerek transpoze edebiliriz. bu sayede daha kolay okunabilir hale gelir.
print("titanic.isnull().values.any(): ",titanic.isnull().values.any()) # veri setinde null değer var mı?
print("titanic.isnull().sum():\n",titanic.isnull().sum()) # veri setinde değişkenlerdeki eksiklik durumu incelemesi
print("titanic['embark_town'].value_counts()",titanic["embark_town"].value_counts()) # veri setindeki embark_town değişkenindeki kategorik değerlerin sayıları.


#################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#################################################

