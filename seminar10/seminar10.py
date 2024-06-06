# Задача 44:  
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10

# добавлено для дополнительного тестирования
lst += ['cyborg'] * 10
random.shuffle(lst)

df = pd.DataFrame({'whoAmI':lst})

# смотрим, что получается при вызове get_dummies, чтобы сделать по образцу
# print(pd.get_dummies(df['whoAmI']))

# в get_dummies колонки отсортированы, делаем аналогично
for item in sorted(set(lst)):
    df.loc[df['whoAmI'] == str(item), str(item)] = True
    df.loc[df['whoAmI'] != str(item), str(item)] = False

# в get_dummies "исходная" колонка отсутствует, также удаляем, исходный DataFrame не изменяем
df_onehot = df.drop('whoAmI', axis=1, inplace=False)

print(df_onehot)
