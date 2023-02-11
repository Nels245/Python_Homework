# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01] 

list2 = list(range(len(list1)))

for i in range(len(list1)): #отделяем дробную часть
        list2[i] = list1[i] * 100 % 100

for i in range(len(list2)): #Проверка на type float
    if list2[i] == 0:
        list2[i] = max(list2)

a = max(list2)
b = min(list2)

print(list1)
print((a  - b)/100)
