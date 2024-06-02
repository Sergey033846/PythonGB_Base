# Факториал
#  5 != 1 ⋅ 2 ⋅ 3 ⋅ 4 ⋅ 5 = 120 


def factorial(n):    
    if n == 0:
        return 1
    return n * factorial(n - 1)
    

k = 5
print(factorial(k))
