# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

size = int(input())

startlist = list(range(1,size + 1))
resultlist = startlist

multi = 1
for i in range(len(startlist)):
    multi *= startlist[i]
    resultlist[i] = multi
    
print(resultlist)