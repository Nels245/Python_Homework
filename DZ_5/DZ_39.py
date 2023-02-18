# 39(2). Создайте программу для игры в ""Крестики-нолики"". 
# Игра реализуется в терминале, игроки ходят поочередно, 
# необходимо вывести карту(как удобнее, можно например в виде списка, 
#  которого будут 3 списка по 3 элемента, каждый из которого обозначает 
#  соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, 
#  на которую мы хотим поставить крестик или нолик, и проверку на победу
#  ( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

empty_field =   ['_','_','_',
                '_','_','_',
                '_','_','_']
#Ошибка при выводе, выводит победителя несколько раз вместо 1

#Добавить проверку на ввод числа а не символа!!!

#Проверка клетки и числа
def place_check_1(empty_field):

    if win_check(empty_field) == True:
        return

    print("Игрок 1, выберите клетку(введите число от 1 до 9): ")
    player_1 = int(input())
    print()
    while player_1 > 9 or player_1 < 1:
        print("Введите число от 1 до 9: ")
        player_1 = int(input())

    while empty_field[player_1 - 1] != '_':
        print("Данная клетка занята, выберите другую: ")
        player_1 = int(input())
        print()
    else:
        empty_field.pop(player_1 - 1)
        empty_field.insert(player_1 - 1, 'o')

#Проверка клетки и числа
def place_check_2(empty_field):

    if win_check(empty_field) == True:
        return

    print("Игрок 2, выберите клетку(введите число от 1 до 9): ")
    player_2 = int(input())
    print()

    while player_2 > 9 or player_2 < 1:
        print("Введите число от 1 до 9: ")
        player_2 = int(input())

    while empty_field[player_2 - 1] != '_':
        print("Данная клетка занята, выберите другую: ")
        player_2 = int(input())
        print()
    else:
        empty_field.pop(player_2 - 1)
        empty_field.insert(player_2 - 1, 'x')
    
#Проверка на победу
def win_check(empty_field):
        result = False
        #Проверка горизонталей
        if empty_field[0] == empty_field[1] and empty_field[1] == empty_field[2] and empty_field[0] == 'o':
            result = True
        elif empty_field[3] == empty_field[4] and empty_field[4] == empty_field[5] and empty_field[3] == 'o':
            result = True
        elif empty_field[6] == empty_field[7] and empty_field[7] == empty_field[8] and empty_field[6] == 'o':
            result = True

        #Проверка вертикалей
        elif empty_field[0] == empty_field[3] and empty_field[3] == empty_field[6] and empty_field[0] == 'o':
            result = True
        elif empty_field[1] == empty_field[4] and empty_field[4] == empty_field[7] and empty_field[1] == 'o':
            result = True
        elif empty_field[2] == empty_field[5] and empty_field[5] == empty_field[8] and empty_field[2] == 'o':
            result = True

        #Проверка диагоналей
        elif empty_field[0] == empty_field[4] and empty_field[4] == empty_field[8] and empty_field[0] == 'o':
            result = True
        elif empty_field[2] == empty_field[4] and empty_field[4] == empty_field[6] and empty_field[2] == 'o':
            result = True

        if result == True:
            print("Победил Игрок 1!")
            return result

       #Проверка горизонталей
        if empty_field[0] == empty_field[1] and empty_field[1] == empty_field[2] and empty_field[0] == 'x':
            result = True
        elif empty_field[3] == empty_field[4] and empty_field[4] == empty_field[5] and empty_field[3] == 'x':
            result = True
        elif empty_field[6] == empty_field[7] and empty_field[7] == empty_field[8] and empty_field[6] == 'x':
            result = True

        #Проверка вертикалей
        elif empty_field[0] == empty_field[3] and empty_field[3] == empty_field[6] and empty_field[0] == 'x':
            result = True
        elif empty_field[1] == empty_field[4] and empty_field[4] == empty_field[7] and empty_field[1] == 'x':
            result = True
        elif empty_field[2] == empty_field[5] and empty_field[5] == empty_field[8] and empty_field[2] == 'x':
            result = True
        
        #Проверка диагоналей
        elif empty_field[0] == empty_field[4] and empty_field[4] == empty_field[8] and empty_field[0] == 'x':
            result = True
        elif empty_field[2] == empty_field[4] and empty_field[4] == empty_field[6] and empty_field[2] == 'x':
            result = True

        if result == True:
            print("Победил Игрок 2!")
            return result
        else:
            return result
        
#Ход игрока
def turn(empty_field):
    #Проверка свободной клетки
    place_check_1(empty_field)

    #Вывод результата хода 1 игрока
    print_field(empty_field)
    print()

    #Проверка свободной клетки
    place_check_2(empty_field)

    #Вывод результата хода 2 игрока
    print_field(empty_field)
    print()

    #Проверка победителя
    win_check(empty_field)

#Вывод игрового поля
def print_field(empty_field):
    print(empty_field[0],empty_field[1], empty_field[2], "    1 2 3")
    print(empty_field[3],empty_field[4], empty_field[5], "    4 5 6")
    print(empty_field[6],empty_field[7], empty_field[8], "    7 8 9")
# ------------------ Вывод ----------------------
print_field(empty_field)
print()

while win_check(empty_field) == False:
    turn(empty_field)
else:
    print("Игра окончена!")

