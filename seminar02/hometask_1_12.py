# 2
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = 12
p = 27

x = 1
flag = True

while x <= 1000:
    y = x
    while flag and y <= 1000:
        if x + y == s and x * y == p:
            print(x, y)
            flag = False
        y += 1
    x += 1

# решение автотеста
# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))

# for solution in solutions:
#     print(solution[0], solution[1])
