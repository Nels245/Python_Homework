# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.  
# Каждое число вводится с новой строки.
# Ввод: 7 5 2
# Вывод: 7 9 11 13 15

print("Введите последовательно 3 числа: ")
a1 = int(input()) #Первый элемент прогресии
n = int(input()) #Кол-во элементов
d = int(input()) #Шаг прогрессии

list2 = [(a1 +(i-1)*d) for i in range (1, n + 1)]

print(list2)


