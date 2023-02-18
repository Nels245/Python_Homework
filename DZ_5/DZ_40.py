# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

data = "AAAAAAFDDCCCCCCCCCCCCA"
print(data, " - исходная строка")
# data = "11111222233344"
[c for c in data] #Сплитим строку на символы
data_new = []

#Алгоритм сжатия данных
def RLE_compr(data):
    count = 1
    for i in range(1,len(data)):
        if data[i] == data[i - 1]:
            count+=1
        elif data[i] != data[i - 1]:
            data_new.append(str(count))
            data_new.append(data[i - 1])
            count = 1
        if i == (len(data) - 1):
            data_new.append(str(count))
            data_new.append(data[i])   

    print("".join(data_new), " - сжатая строка")
    return data_new

#Алгоритм восстановления данных
def RLE_recovery(data):   # Почему то умножает всегда 6 а не на кол-во символов, почему???
    print(data)
    data_new2 = [] 
    for i in range(1, len(data), 2):
        data_new2.append(data[i] * int(data[i - i]))
        print(data[i], " * ", data[i - 1], " = ", data[i] * int(data[i - i])) #Проверка

    print("".join(data_new2))

RLE_compr(data)

RLE_recovery(data_new)