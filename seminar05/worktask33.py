# Задача №33. 
# Хакер Василий получил доступ к классному журналу и хочет  заменить  все  свои  минимальные  оценки  на максимальные.  
# Напишите  программу,  которая заменяет  оценки  Василия,  но  наоборот:  все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list_1 = [1, 3, 3, 3, 4]

min_grade = min(list_1)
max_grade = max(list_1)

for i, item in enumerate(list_1):
    if list_1[i] == max_grade:
        list_1[i] = min_grade

print(list_1)