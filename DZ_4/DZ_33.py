# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input())
result = ""

for i in range(k,-1,-1): #Шаг от k к 0
    koef = random.randint(0,100) #Генерим коэффициенты
    if koef == 0:
        continue #если коэффициент зарандомился 0, мы переходим дальше
    if koef ==1:
            if i == 1:
                result += f"{koef}*x+"
            elif i == 0:
                result += f"{koef}"
            else:
                result += f"x**{i}+"
    else:
            if i == 1:
                result += f"{koef}*x+"
            elif i == 0:
                result += f"{koef}"
            else:
                result += f"{koef}*x**{i}+"

result+= " = 0"
print(result)

#Запись в файл

f = open("file.txt","w")
f.write(result)
f.close()
