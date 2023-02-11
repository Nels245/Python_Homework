
#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# import datetime
# n = int(input())
# rand = datetime.datetime.now().microsecond%(n+1)
# print(rand)
#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

# a = ["st","qwe","12","tyy"]
# for i in a:
#     if i.isdigit():
#         print(a.index(i))
#or
# a = ["st","qwe",12,"tyy"]
# for i in a:
#     if type(i)==int:
#         print(a.index(i))
#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# list_str =  []
# sub_str = "123"
# count = 0
# for i in range(len(list_str)):
#     print(i)
#     if list_str[i]==sub_str:
#         count+=1
#         if count == 2:
#             print(i)
#             break
# if count<2:
#     print(-1)
