# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию ﬁnd_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
# по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. 
# Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*ﬁnd_farthest_orbit(orbits))
# Вывод: 
# 2.5 10

from math import pi

def ﬁnd_farthest_orbit(list_of_orbits):
    # решение через словарь, так как надо использовать списочные выражения
    # dict_s_orbits = {3.14 * orbit[0] * orbit[1]: orbit 
    #                for orbit in list_of_orbits if orbit[0] != orbit[1]}            
    # return dict_s_orbits[max(dict_s_orbits)]
       
    # однострочное решение
    #return max(filter(lambda x: x[0] != x[1], list_of_orbits), key=lambda x: pi * x[0] * x[1])

    # красивое решение
    return max(orbits, key=lambda x: 3.14 * x[0] * x[1] * (x[0] != x[1]))


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*ﬁnd_farthest_orbit(orbits))