# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите число: '))
# Position1 = int(input('Позиция №1 '))
# Position2 = int(input('Позиция №2 '))
l = []
for i in range(-n, n + 1):
    l.append(i)
print(l)
random.shuffle(l)
print(l)
