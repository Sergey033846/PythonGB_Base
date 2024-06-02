# Задача №27.
# Пользователь вводит текст(строка).
# Определите,  сколько  различных  слов содержится в этом тексте.
# Словом считается  последовательность непробельных символов идущих подряд

# Cлова разделены одним или большим числом пробелов.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# Слова разделены одним или большим числом пробелов  или  символами  конца  строки.
# Input: She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore,I'm sure that the shells are sea shore shells.
# Output: 19

str1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea " \
         "shells on the sea shore I'm sure that the shells are sea shore shells"
end_of_line_chars = ''

#str1 = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea " \
#        "shells on the sea shore,I'm sure that the shells are sea shore shells."
#end_of_line_chars = '\n'

for char in end_of_line_chars:
    str1 = str1.replace(char, ' ')

words_list = str1.lower().split()

dict1 = dict()

for i in range(len(words_list)):
    word = words_list[i]

    dict1[word] = 1 + dict1.get(word, 0)
    # if word in dict1:
    #     dict1[word] += 1
    # else:
    #     dict1[word] = 1

print(str1)
print(dict1)
print(len(dict1))
