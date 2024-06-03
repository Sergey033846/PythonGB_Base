# 1
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

coins = [0, 1, 0, 1, 1, 0]

n0 = 0
n1 = 0

for i in range(len(coins)):
    if (coins[i]): 
        n1 += 1
    else:
        n0 += 1

if n0 < n1:
    print(n0)
else:
    print(n1)

# решение автотеста
# coins = [0, 1, 0, 1, 1, 0]
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
