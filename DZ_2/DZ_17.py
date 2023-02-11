# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input())
print()

list = list(range(-n,n+1))

multi = 1

path = 'file.txt'
data = open(path, 'r')
for line in data:
    multi*=list[int(line)]
    print(line)
data.close()

print(list)
print()
print(multi)

