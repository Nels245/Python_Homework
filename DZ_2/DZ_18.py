# Реализуйте алгоритм перемешивания списка.
import random

list = list(range(10))
print(list)

array = [random.randint(0,10) for i in range(0,10)] #10 рандомных числе от 1 до 10
print(array)
print()

for i in range(10):
    temp = list[i]
    list[i] = list[array[i]]
    list[array[i]] = temp

print(list)

# Работает, но через раз, проблемы с границей, так и не понял почему