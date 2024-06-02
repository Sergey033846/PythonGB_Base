# Задача №25.
# Напишите  программу,  которая  принимает  на  вход строку,  и  отслеживает,  сколько  раз  каждый  символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для  решения  данной  задачи  используйте  функцию .split()

str1 = 'a a a b c a a d c d d'

unique_chars = set(str1).difference(' ')

for char in unique_chars:
    list1 = str1.split(char)
        
    # split() возвращает на 1 подстроку больше, чем кол-во встретившихся разделителей
    # первый символ не нумеруем
    for i in range(2, len(list1)):              
        list1[i] = f'_{i - 1}{list1[i]}'
        
    str1 = char.join(list1)

print('Ответ:')
print(str1)

print('Проверка:')
print('a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2')
