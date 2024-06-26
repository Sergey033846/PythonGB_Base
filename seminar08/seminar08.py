# Вводится натуральное число N. 
# С помощью list comprehension сформировать двумерный список размером N x N, 
# состоящий из нулей, а по главной диагонали - единицы. 
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). 
# Результат вывести в виде таблицы чисел как показано в примере ниже.

# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# n = 4
# list_1 = [[int(col == row) for col in range(n)] for row in range(n)]
# for i in range(n):
#     print(list_1[i])

#---------------------------------------
# Вводятся названия городов в строку через пробел. 
# Необходимо сформировать список с помощью list comprehension, содержащий названия длиной более пяти символов. 
# Результат вывести в строчку через пробел.

# Sample Input:
# Казань Уфа Москва Челябинск Омск Тур Самара
# Sample Output:
# Казань Москва Челябинск Самара

# s = 'Казань Уфа Москва Челябинск Омск Тур Самара'
# list_1 = [_ for _ in s.split() if len(_) > 5]
# print(*list_1)
#---------------------------------------

# 1.Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

# пример  - 8 11 0 -23 140 1 => 11 -23
# "8 11 0 -23 140 1 "

# s = '8 11 0 -23 140 1'
# print(*filter(lambda x: 9 < abs(int(x)) < 100, s.split()))
# print(list(filter(lambda x: 9 < abs(int(x)) < 100, s.split())))

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, s.split()))
