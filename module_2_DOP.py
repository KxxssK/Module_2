import random
import time


def table_L():
    mnogestvo = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    left_tab = int(random.choice(mnogestvo))
    return left_tab

def pasword():
    right_tab = ''
    for chislo_1 in range(1, left_tab):
        for chislo_2 in range(chislo_1 + 1, left_tab + 1):
            if left_tab % (chislo_1 + chislo_2) == 0:
                right_tab += str(chislo_1) + str(chislo_2)
    return right_tab



print('Приветствую тебя путник, у тебя осталось 10 секнуд, до дотого, как тебя раздавят шипы')

left_tab = table_L()

print(f'Ваше число: {left_tab} подберите пароль')


while True:
    gotov = input('Подобрать пароль да/нет ? ')
    if gotov == 'нет':
        print('Вы погбли ужасной смерью')
        break
    elif gotov != 'да' and gotov != 'нет':
        print('Неверные данные, попробуйте снова')
        continue
    else:
        right_tab = pasword()
    print(f'Скорее вводи этот пароль {right_tab} для числа {left_tab}, а то тебя раздавят шипы')
    print('-------------------------------------------------')
    print('Поздровляю тебя, ты первый кто вышел отсюда живым')
    break


