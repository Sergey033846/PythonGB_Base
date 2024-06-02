# Задача №45.
# Два  различных  натуральных  числа  n  и  m  называются дружественными,  
# если  сумма  делителей  числа  n (включая  1,  но  исключая  само  n)  равна  числу  m  и наоборот. 

# Например, 220 и 284 – дружественные числа. 

# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает  на  вход  одно  натуральное  число  k,  не превосходящее  10**5 .  
# Программа  должна  вывести  все  пары  дружественных  чисел,  каждое  из  которых  не  превосходит  k.  
# Пары  необходимо  выводить  по  одной  в строке, разделяя пробелами. 
# Каждая пара должна быть выведена  только  один  раз  (перестановка чисел  новую пару не дает).

# Ввод:
# 300
# Вывод:
# 220 284

# мое решение
# def sum_dividers_excluding_n(n: int) -> int:
#     return sum(i for i in range(1, n) if n % i == 0)


# k = 10_000

# for i in range(1, k - 1):        
#     sum_dividers_i = sum_dividers_excluding_n(i)
#     for j in range(i + 1, k):            
#         if sum_dividers_i == j and sum_dividers_excluding_n(j) == i:            
#             print(i, j)  
# --------------------------------

# решение на семинаре
k = 10_000

dict_1 = {}

for i in range(1, k):
    for j in range(1, i//2 + 1):        
        if i % j == 0:
            dict_1[i] = dict_1.get(i, 0) + j

for i, sumdiv in dict_1.items():
    if i < sumdiv and i == dict_1.get(sumdiv, False) and sumdiv == dict_1[i]:
        print(i, sumdiv)
# --------------------------------

# проверка на дружественность
# n = 220
# m = 284

# # n = 1184
# # m = 1210

# print(f'{n = } {m = }')

# dividers_n = [i for i in range(1, n) if n % i == 0 or i == 1] 
# dividers_m = [i for i in range(1, m) if m % i == 0 or i == 1] 
# print(f'{dividers_n = }')
# print(f'{dividers_m = }')

# sum_dividers_n = sum(i for i in range(1, n) if n % i == 0 or i == 1)
# sum_dividers_m = sum(i for i in range(1, m) if m % i == 0 or i == 1)
# print(f'{sum_dividers_n = } {sum_dividers_m = }')
# --------------------------
