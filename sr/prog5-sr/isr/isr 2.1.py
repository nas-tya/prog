# Задание: разработать функцию, возвращающую элементы ряда
# Фибоначчи по данному максимальному значению.


def fibonacci_max(max_number):
    fibonacci_list = [0, 1]
    current_fibonacci = fibonacci_list[-1]
    while current_fibonacci <= max_number:
        fibonacci_list += [fibonacci_list[-2] + fibonacci_list[-1]]
        current_fibonacci = fibonacci_list[-1]
    fibonacci_list.pop(-1)
    return fibonacci_list


print(fibonacci_max(88))
print(fibonacci_max(89))
