# Напишите программу, которая принимает на вход 2 числа. Задайте список N элементов, 
# заполненных числами из промежутка [N, -N]. Найдите произведение элементов на указанных позициях (не индексах)

n = int(input('Введите число: '))
Position1 = int(input('Позиция №1 '))
Position2 = int(input('Позиция №2 '))
l = []
for i in range(-n, n + 1):
    l.append(i)
print(l[Position1 - 1] * l[Position2 - 1])




