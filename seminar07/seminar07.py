# transformation = lambda x: x

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# ---------------------------------------
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

def ﬁnd_farthest_orbit(list_of_orbits):
    # dict_s_orbits = {3.14 * orbit[0] * orbit[1]: orbit 
    #                for orbit in list_of_orbits if orbit[0] != orbit[1]}            
    # return dict_s_orbits[max(dict_s_orbits)]

    return max(filter(lambda x: x[0] != x[1], list_of_orbits), 
               key=lambda x: 3.14 * x[0] * x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))

# красивое решение
print(max(orbits, key=lambda x: 3.14 * x[0] * x[1] * (x[0] != x[1])))
