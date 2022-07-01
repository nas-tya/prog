# Дополнение программы "Калькулятор" декоратором, сохраняющим выполняемые действия, в файл-журнал.

import math
import calcprint


def main():
    operands = list(map(float, input('Enter arguments: ').split()))
    action = input("Enter type of operation: ")
    result = calculate(*operands, action)
    calcprint.print_results(action, result, operands)
    print(result)


def write_log_dog(func):
  def write_log(*args, **kwargs):
    """
    с помощью этой функции история действий пользователя записывается в файл
    """
    f = open('calc-history.log.txt', mode='a', errors='ignore')
    # args = repr(*args).strip('[]')    # strip избавляет от квадратных скобок при выводе
    result = func(*args, **kwargs)
    f.write(f"{args}, {result}\n")
    f.close()
    return result
  return write_log


@write_log_dog
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
