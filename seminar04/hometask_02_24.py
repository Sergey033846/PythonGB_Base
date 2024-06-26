# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти  кусты  обладают  разной  урожайностью,  поэтому  ко  времени  сбора  на  них 
# выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта  система  состоит  из  управляющего  модуля  и  нескольких  собирающих  модулей. 
# Собирающий  модуль  за  один  заход,  находясь  непосредственно  перед  некоторым 
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать  за  один  заход  собирающий  модуль,  находясь  перед  некоторым  кустом 
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

#berries = [1, 2, 3, 4]
berries = [6, 2, 3, 4, 5]

max_berries = 0

for i in range(len(berries)):
    # count_berries = berries[i - 1] + berries[i] + berries[(i + 1) % len(berries)]    
    count_berries = berries[i] + berries[i - 1] + berries[i - 2]
        
    if count_berries > max_berries:
        max_berries = count_berries

print(max_berries)

# решение автотеста
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# # Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))

