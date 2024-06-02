# 2
# Рекурсивная сумма
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# 2 2
# 4

# мое первое решение

# def sum(a: int, b: int):         
#     print(f'{a=} {b=}')
#     if b == 0:
#         return a
#     if a >= b:
#         return 1 + sum(a, b - 1)
#     else:
#         return 1 + sum(b, a - 1)


# x = 3
# y = 7

# print(sum(x, y))

# ----------------

def sum(a, b):
    print(f'{a=} {b=}')
    
    if b == 0:
        return a
    
    if a == 0:
        return b
    
    if a >= b:
        return sum(a + 1, b - 1)
    else:
        return sum(b + 1, a - 1)

x = 3
y = 7

print(sum(x, y))

# ----------------

# решение автотеста

# def sum(a, b):
#     print(f'{a=} {b=}')
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)

# x = 3
# y = 7

# print(sum(x, y))
