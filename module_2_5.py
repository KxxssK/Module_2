def Vvod():
    print('Введите данные для заполнения массива. Для остановки напиши стоп')
    Stroka = int(input('Введите число строк: '))
    Stolb = int(input('Введите число столбцов: '))
    Chisla = (input('Введите числа для массива: '))
    return Stroka, Stolb, Chisla
https://github.com/KxxssK/Module_2/blob/master/module_2_5.py

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


while True:
    nach = str(input('Составить массив да / нет: '))
    if nach == 'нет':
        print('Генерация отменена')
        break
    elif nach != 'нет' and nach != 'да':
        print('Неверные данные, попробуйте снова')
        continue
    else:
        Stroka, Stolb, Chisla = Vvod()
    matrix = get_matrix(Stroka, Stolb, Chisla)
    print('Ваша матрица:', matrix)
    continue
