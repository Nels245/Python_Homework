# Задача 6. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите день недели (число): '))

if day % 6 == 0 or day % 7 == 0:
    print('да')
else:
    print('нет')