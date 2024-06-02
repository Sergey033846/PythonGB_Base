# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных:
# В первой строке подаётся число n – количество холодильников. 
# В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

# Формат выходных данных:
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.


# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1:
# 1 2 3

# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton

# Sample Output 2:
# 1 2 7 8

# list_input = ['222anton456',
#                'a1n1t1o1n1',
#                '0000a0000n00t00000o000000n',
#                'gylfole',
#                'richard',
#                'ant0n',]
# output - 1 2 3

list_input = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
               'anton',
               'aoooooooooontooooo',
               'elelelelelelelelelel',
               'ntoneeee',
               'tonee',
               '253235235a5323352n25235352t253523523235oo235523523523n',
               'antoooooooooooooooooooooooooooooooooooooooooooooooooooon',
               'unton',]
# output - 1 2 7 8

word_anton = 'anton'

for i in range(len(list_input)):
    i_str = list_input[i]
    start_search_index = -1
    
    for char_anton in word_anton:
        start_search_index = i_str.find(char_anton, start_search_index + 1)
        if start_search_index == -1:
            break
    
    if start_search_index != -1:
        print(i + 1, end=' ')
