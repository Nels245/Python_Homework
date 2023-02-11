# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input())

dict = {}
summ = 0
for i in range(1,n + 1):
    dict[i] = (1 + 1/i)**i

    if len(str(dict[i])) > 4: #Здесь округляю float до 2ух знаков после запятой
        dict[i] = round(dict[i],2)

    summ += dict[i]

print(dict)
print(summ)
