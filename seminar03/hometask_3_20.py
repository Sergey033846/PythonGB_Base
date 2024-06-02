# 3
# Задача 20.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
# k = 'ноутбук'
# 12

# решение через словарь "символ-стоимость"
# k = 'ноутбук'

# a = [ "AEIOULNSTR", "DG", "BCMP", "FHVWY", "K", "JX", "QZ",
#       "АВЕИНОРСТ", "ДКЛМПУ", "БГЁЬЯ", "ЙЫ", "ЖЗХЦЧ", "ШЭЮ","ФЩЪ" ]

# b = [ 1, 2, 3, 4, 5, 8, 10,
#       1, 2, 3, 4, 5, 8, 10 ]

# dict1 = {}

# cost = 0

# for i in range(len(a)):
#     for char in a[i]:
#         dict1[char] = b[i]

# for letter in k:
#     cost += dict1[letter.upper()]

# print(cost)

# решение через словарь "символЫ-стоимость"

k = 'ноутбук'

char_dict = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10, 
             "АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}

cost = 0

for char in k:
    for keystr, value in char_dict.items():
        if char.upper() in keystr:
            cost += value
            break

print(cost)














# решение автотеста
# word = 'ноутбук'
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
