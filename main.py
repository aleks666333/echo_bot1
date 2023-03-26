import module

print('Добро пожаловать в консольный калькулятор!')

while True:
    print('Введите операцию:')
    print('1 - Сложение')
    print('2 - Вычитание')
    print('3 - Умножение')
    print('4 - Деление')
    print('0 - Выход')

    operation = int(input())

    if operation == 0:
        break

    print('Введите первое число:')
    x = int(input())
    print('Введите второе число:')
    y = int(input())

    if operation == 1:
        result = module.summa(x, y)
    elif operation == 2:
        result = module.raznost(x, y)
    elif operation == 3:
        result = module.proizvedenie(x, y)
    elif operation == 4:
        result = module.chastnoe(x, y)
    else:
        print('Ошибка ввода!')
        continue

    print('Результат:', result)
