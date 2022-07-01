from prettytable import PrettyTable


def print_results(action, result, *operands):
    """
    красивый вывод в виде таблицы
    """
    t = PrettyTable(['operands', 'action', 'result'])
    t.add_row([repr(*operands).strip('[]'), action, result])    # strip избавляет от квадратных скобок при выводе
    print(t)


def write_log(action, result, *operands, file='calc-history.log.txt'):
    """
    с помощью этой функции история действий пользователя записывается в файл
    """
    f = open(file, mode='a', errors='ignore')
    args = repr(*operands).strip('[]')    # strip избавляет от квадратных скобок при выводе
    f.write(f"{action}: {args} = {result} \n")
    f.close()
