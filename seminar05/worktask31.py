# Задача №31. 
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
# 1 1 2 3 5 8 13 21 34 55 89 (ряд от 0 или от 1 ?)


def fibonacci(n):       
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


k = 7
print(fibonacci(k))

list_1 = [fibonacci(i) for i in range(10)]
print(list_1)

