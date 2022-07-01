import math

import calcprint


def main():
    """
    здесь организован ввод значений с клавиатуры
    """
    load_params()
    operands = []
    while True:
        val = input("enter value: ")  # '1,24'
        # здесь мы можем упасть потому что тип, который ввел пользователь у нас не работает
        try:
            if val == "":
                break
            val = float(val)
        except ValueError:
            print(
                "enter the value in the right format (with a '.' if needed): "
            )
        else:
            operands.append(val)
    if len(operands) <= 1:
        return
    # проверяем на допустимость значений
    action = input("action: ")
    # потенциально в этом месте что-то может пойти не так как надо
    try:
        res = calculate(*operands, action, **PARAMS)
    except Exception:
        print("calculation error")
    else:
        print(res)

    """
    раньше значения вводились вот так:
    """
    # operands = list(map(float, input('Enter arguments: ').split()))
    # action = input("Enter type of operation: ")

    """
    вычисление результата, его вывод и запись истории действий в файл:
    """
    result = calculate(*operands, action, **PARAMS)
    calcprint.print_results(action, result, operands)
    calcprint.write_log(action, result, operands)


"""
задаёи начальные значения параметров
"""
PARAMS = {
    'precision': None,
    'output_type': None,
    'possible_types': None,
    'dest': None
}

"""
раньше точность задавалась пользователем, а не считывалась из файла.
реализовывалось это вот так:
"""


# def set_precision_by_keyboard():
#     global PARAMS
#     PARAMS['precision'] = input('Enter the precision: ')
# set_precision_by_keyboard()


def load_params(file="params.ini"):
    """
    эта функция позволяет считывать параметры из указанного файла
    """
    global PARAMS
    f = open(file, mode='r', errors='ignore')
    lines = f.readlines()
    for l in lines:
        param = l.split('=')  # param[0], param[1]
        param[1] = param[1].strip('\n')
        if param[0] != 'dest':
            param[1] = eval(param[1])
        if param[0] == 'precision':
            param[1] == float(param[1])
        if param[0] == 'output_type':
            if param[1] == 'float':
                param[1] = float
            if param[1] == 'int':
                param[1] = int
        if param[0] == 'possible_types':
            if param[1] == '(int, float)':
                param[1] = (int, float)
        PARAMS[param[0]] = param[1]


def float_to_str(f):
    """
    форматирует число так, чтобы оно выводилось не в эксп. виде
    """
    float_string = repr(f)
    if 'e' in float_string:  # ищет экспоненту в числе
        digits, exp = float_string.split('e')
        digits = digits.replace('.', '').replace('-', '')
        exp = int(exp)
        zero_padding = '0' * (abs(int(exp)) - 1)  # вычитаем 1 из-за точки
        sign = '-' if f < 0 else ''
        if exp > 0:
            float_string = '{}{}{}.0'.format(sign, digits, zero_padding)
        else:
            float_string = '{}0.{}{}'.format(sign, zero_padding, digits)
    return float_string


def convert_precision(prec):
    """
    эта функция конвертирует точность в число
    (считает количество цифр после запятой)
    """
    if type(prec) is not float:
        try:
            prec = float(prec)
        except ValueError:
            raise TypeError('wrong argument type')
    str_prec = float_to_str(prec)
    if '.' in str_prec:
        return abs(str_prec.find('.') - len(str_prec)) - 1
    else:
        return 0


def calculate(*args, **kwargs):
    """
    в этой функции оуществляются вычисления
    """
    precision = convert_precision(kwargs['precision'])  # 0.001 -> '0.001' -> 3
    print('Accuracy: ', precision)
    output_type = kwargs['output_type']

    if args[len(args) - 1] == '+':
        r = sum(args[0:len(args) - 1])
        if type(r) is not output_type:
            r = output_type(r)
        return r

    elif args[len(args) - 1] == '*':
        r = 1
        for n in args[0:len(args) - 1]:
            r *= n
        return round(r, precision)

    elif args[len(args) - 1] == '-':
        r = args[0] - sum(args[1:len(args) - 1])
        if type(r) is not output_type:
            r = output_type(r)
        return r

    elif args[len(args) - 1] == '/':
        r = 1
        for n in args[0:len(args) - 1]:
            if n != 0:
                r *= 1 / n
            else:
                return "can't divide by a zero"
        return round(r, precision)

    elif args[len(args) - 1] == "^":
        r = pow(args[0], args[1])
        return round(r, precision)

    elif args[len(args) - 1] == "log":
        r = math.log(args[0], args[1])
        return round(r, precision)
        # math.log(X, base) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

    elif args[len(args) - 1] == "atan":
        r = math.atan2(args[0], args[1])
        return round(r, precision)
        # math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

    else:
        print("there's no action like that")
