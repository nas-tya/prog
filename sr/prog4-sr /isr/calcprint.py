from prettytable import PrettyTable


def print_results(action, result, *operands):
    """
    Вывод в виде таблицы
    """
    t = PrettyTable(['operands', 'action', 'result'])
    t.add_row([repr(*operands).strip('[]'), action, result])    # strip избавляет от квадратных скобок при выводе
    print(t)

