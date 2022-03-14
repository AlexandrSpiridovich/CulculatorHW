from num2words import num2words

contin = "w"
simvol = ['+', '-', '*', '/']
number_cyk = 0
while contin == "w":
    number_cyk += 1
    try:
        f_num = float(input("Введите первое число>>"))
        if "стоп" == f_num or f_num == "stop":
            break
    except ValueError:
        print("Ошибка: введите числовое значение")
        continue

    operat = input("Введите операцию>>")
    if "стоп" == operat or operat == "stop":
        break
    elif operat not in simvol:
        print("Oops...Попробуйте другую операцию")
        continue
    try:
        s_num = float(input("Введите второе число>>"))
        if "стоп" == f_num or f_num == "stop":
            break
    except ValueError:
        print("Ошибка: введите числовое значение")
        continue

    if operat == '+':
        result = f_num + s_num
    elif operat == '-':
        result = f_num - s_num
    elif operat == '*':
        result = f_num * s_num
    else:
        try:
            result = f_num / s_num
        except ZeroDivisionError:
            print('На ноль делить нельзя')
            continue
    print(num2words(result, lang='rus'))
    print('операций совешено>>' + str(number_cyk))
    contin = input("Введите 'w', чтобы продолжить или Enter, чтобы закончить")

