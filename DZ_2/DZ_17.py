# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = list(range(int(input()))) #Сами генерируем длину списка
print(list1)
list2 = list1[::-1]
print(list2)

len1 = 0
if len(list1) % 2 == 0:
    len1 = len(list1) // 2
else:
    len1 = len(list1) // 2 + 1

list3 = list(range(len1))

for i in range(len1):
    list3[i] = list1[i] * list2[i]

print()
print(list3)
