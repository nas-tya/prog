# Задание: разработать функцию, возвращающую список чисел
# ряда Фибоначчи с использованием бесконечных итераторов (модуль
# itertools).

import itertools


def fibonacci_numbers(number):
    fibonacci_list = [0, 1]
    for i in itertools.count(0):
        if i > 1:
            fibonacci_list += [fibonacci_list[-2] + fibonacci_list[-1]]
        if i >= number - 1:
            break
    return fibonacci_list


print(fibonacci_numbers(6))
