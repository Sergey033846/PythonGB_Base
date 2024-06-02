# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n (само число)
# Input: 5
# Output: yes

# у любого составного числа есть собственный (то есть не равный 1) делитель, не превосходящий квадратного корня из числа
# алгоритм заканчивает работу либо при нахождении делителя, либо если проверяемый делитель станет больше корня из n.
# Чиcло n является простым, если алгоритм закончился по причине того, что проверяемый делитель стал больше, чем корень из n.

    
def isprime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

k = 7

print('yes' if isprime(k) else 'no')