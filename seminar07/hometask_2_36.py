# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 6, 6)

# На выходе:
# 1 2  3  4  5  6
# 2 4  6  8  10 12
# 3 6  9  12 15 18
# 4 8  12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for row in range(1, num_rows + 1):
            for column in range(1, num_columns + 1):            
                #print(f'{operation(row, column)}{" " * (column != num_columns)}', end='')
                print(f'{operation(row, column):>2}{" " * (column != num_columns)}', end='')
            print()

rows = 6
columns = 6
print_operation_table(lambda x, y: x * y, rows, columns)

# решение автотеста
# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')        
#         print(''.join([str(i) for i in result[:len(result) - 1]]))

# print_operation_table(lambda x, y: x * y, 3, 3)