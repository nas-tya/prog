# Разработать прототип программы "Калькулятор", позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл. [ без использования '@' ]

import math
import calcprint

def main():
  operands = list(map(float, input('Enter arguments: ').split()))
  action = input("Enter type of operation: ")
  result = calculate(*operands, action)
  calcprint.print_results(action, result, operands)
  write_log(action, result, operands)
  

def write_log(action, result, *operands, file='calc-history.log.txt'):
    """
    с помощью этой функции история действий пользователя записывается в файл
    """
    f = open(file, mode='a', errors='ignore')
    args = repr(*operands).strip('[]')    # strip избавляет от квадратных скобок при выводе
    f.write(f"{action}: {args} = {result} \n")
    f.close()


def calculate(*args, **kwargs):
    if args[len(args) - 1] == '+':
        r = sum(args[0:len(args) - 1])
        return r

    elif args[len(args) - 1] == '*':
        r = 1
        for n in args[0:len(args) - 1]:
            r *= n
        return round(r)

    elif args[len(args) - 1] == '-':
        r = args[0] - sum(args[1:len(args) - 1])
        return r

    elif args[len(args) - 1] == '/':
        r = 1
        for n in args[0:len(args) - 1]:
            if n != 0:
                r *= 1 / n
            else:
                return "can't divide by a zero"
        return round(r)

    elif args[len(args) - 1] == "^":
        r = pow(args[0], args[1])
        return round(r)

    elif args[len(args) - 1] == "log":
        r = math.log(args[0], args[1])
        return round(r)
        # math.log(X, base) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

    elif args[len(args) - 1] == "atan":
        r = math.atan2(args[0], args[1])
        return round(r)
        # math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

    else:
        print("there's no action like that")


main()
