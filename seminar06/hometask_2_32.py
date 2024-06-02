# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_number = 5
max_number = 15

for i, value in enumerate(list_1):
    if min_number <= value <= max_number:
        print(i)

#print(*(i for i, value in enumerate(list_1) if min_number <= value <= max_number), sep='\n')        

# решение автотеста
# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)

