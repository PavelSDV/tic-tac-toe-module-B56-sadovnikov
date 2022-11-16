import random
import time
list_dict_combination = [{'11':'-','12':'-','13':'-'},
     {'21':'-','22':'-','23':'-'},
     {'31':'-','32':'-','33':'-'},
     {'11':'-','21':'-','31':'-'},
     {'12':'-','22':'-','32':'-'},
     {'13':'-','23':'-','33':'-'},
     {'11':'-','22':'-','33':'-'},
     {'13':'-','22':'-','31':'-'}]

key_combination = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def print_screen(ls_comb):
    list_screen = [['', '1', '2', '3'], ]
    num_str = 1
    temp = []
    for i in ls_comb[:3]:
        temp = list(i.values())
        temp.insert(0, str(num_str))
        list_screen.append(temp)
        num_str += 1
    for i in list_screen:
       print(*[f"{x:>3}" for x in i])  # 3 - размер отступов

print_screen(list_dict_combination)

def play_user_comp(ls_dict_combination, k_combination):
    comp_two_step_first = 0
    while True:
        сomputer_first = input('Кто будет ходить первым? Введите: 0 - Вы, 1 - компьютер ', )
        if сomputer_first not in ['0', '1']:
            print('Нет такого варианта. Введите 0 или 1')
            continue
        else:
            break
    while True:
        print('Какой уровень сложности?')
        difficulty_level = input('Введите: 0 - компьютер будет думать, 1 - поднять себе самооценку ', )
        if difficulty_level not in ['0', '1']:
            print('Нет такого варианта. Введите 1 или 0')
            continue
        else:
            break

    while True:

        if int(сomputer_first):
            if int(difficulty_level):
                comp_level_1(k_combination, ls_dict_combination)  # ход компьютера random
            else:
                comp_timer_think()
                comp_level_2(k_combination, ls_dict_combination, comp_two_step_first)  # ход компьютера выбор вариантов

            print_screen(ls_dict_combination)  # вывод на экран после хода computera
            if сheck_combination_win(ls_dict_combination, k_combination):  # проверяем комбинацию на три в ряд после хода computera
                break                           # если есть три в ряд заканчиваем цикл завершаем игру

        comp_two_step_first = 1     # Если computer ходит первым, первый ход random. Если вторым, то первый ход только в центр или в углы, когда computer думает
        сomputer_first = 1
        while True:
            num_key = input('Ваш ход. Введите номер поля: номер строки и номер колонки (например 21)  : ', )
            if num_key not in ['11', '12', '13', '21', '22', '23', '31', '32', '33']: # доступные ходы будем проверять по списку ключей
                print('Нет такого поля, введите правильные номер строки и номер колонки (например 21)')
                continue
            if num_key not in k_combination:
                print('Клетка занята')
                continue
            break

        update_list_dict_combination(ls_dict_combination, num_key, k_combination, 0)
        print_screen(ls_dict_combination)  # вывод на экран после хода usera
        if сheck_combination_win(ls_dict_combination, k_combination):  # проверяем комбинацию на три в ряд после хода usera
            break                  # если есть три в ряд заканчиваем цикл завершаем игру

    return True

def сheck_combination_win(ls_comb, k_comb):
    for i in ls_comb:
        if list(i.values()).count('X') == 3:
            print('Вы выйграли')
            return True
        if list(i.values()).count('O') == 3:
            print('Computer выйграл ')
            return True
    if not k_comb:  # если в списке ключей не осталось завершаем игру ничьей
        print('Ничья. Конец партии.')
        return True

def update_list_dict_combination(ls_comb, key, k_comb, user_or_comp_move):
    print(f'Ход на поле {key}. Строка {list(key)[0]}. Колонка {list(key)[1]}.')
    for i in ls_comb:
        for j in i.keys():
            if j == key:
                if user_or_comp_move:
                    i[j] = 'O'
                else:
                    i[j] = 'X'
    k_comb.remove(key)

def comp_level_1(k_comb, ls_comb):   # ход компьютера
    if k_comb:
        key = random.choice(k_comb)
        update_list_dict_combination(ls_comb, key, k_comb, 1)
    else:
        print('Ничья. Конец партии.')
    return

def comp_level_2(k_comb, ls_comb, comp_two_step_first):      # ход компьютера
    num_variant_comb = []
    key = ''
    for i in ls_comb:                       # перебираем словари комбинаций
        if list(i.values()).count('O') == 2 and list(i.values()).count('-') == 1:  # если есть два О ставим третий
            for j in i.keys():
                if i[j] == '-':
                    num_variant_comb.append(j)  # сохранем все варианты О_2 -_1
    if num_variant_comb:
        key = random.choice(num_variant_comb) # выбираем случайный вариант
        update_list_dict_combination(ls_comb, key, k_comb, 1)
        return

    for i in ls_comb:
        if list(i.values()).count('X') == 2 and list(i.values()).count('-') == 1:  # если есть два Х закрываем нолём
            for j in i.keys():
                if i[j] == '-':
                    num_variant_comb.append(j)  # сохранем все варианты Х_2 -_1
    if num_variant_comb:
        key = random.choice(num_variant_comb) # выбираем случайный вариант
        update_list_dict_combination(ls_comb, key, k_comb, 1)
        return

    for i in ls_comb:
        if list(i.values()).count('O') == 1 and list(i.values()).count('-') == 2:  # если есть один O ставим второй ноль
            for j in i.keys():
                if i[j] == '-':
                    num_variant_comb.append(j) # сохранем все варианты O_1 -_2
    if num_variant_comb:
        key = random.choice(num_variant_comb) # выбираем случайный вариант
        update_list_dict_combination(ls_comb, key, k_comb, 1)
        return

    if comp_two_step_first: # выбрать по ключам из доступных вариантов, первый ход, computer второй
        for i in ls_comb:
            for j in i.keys():
                if i[j] == '-' and j == '22':  # если центр пуст, ставим в центр
                    update_list_dict_combination(ls_comb, j, k_comb, 1)
                    return                      # если центр занят, ставим в любой угол
                if i[j] == '-' and (j == '11' or j == '13' or j == '31' or j == '33'):
                    num_variant_comb.append(j)  # сохранем варианты O_1 -_2
        if num_variant_comb:
            key = random.choice(num_variant_comb)  # выбираем случайный вариант только из углов
            update_list_dict_combination(ls_comb, key, k_comb, 1)
            return

    key = random.choice(k_comb) # выбрать по ключам из доступных вариантов, первый ход, computer первый
    update_list_dict_combination(ls_comb, key, k_comb, 1)
    return

def comp_timer_think():
    print('Computer думает')
    for i in range(4):
        print('\r\u002f', end='')
        time.sleep(0.2)
        print('\r\u002d', end='')
        time.sleep(0.2)
        print('\r\u005c', end='')
        time.sleep(0.2)
        print('\r\u00a6', end='')
        time.sleep(0.2)

play_user_comp(list_dict_combination, key_combination)


