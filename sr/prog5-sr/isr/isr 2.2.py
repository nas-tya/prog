# Задание: создать программу, возвращающую список чисел
# Фибоначчи с помощью итератора.



def fibonacci_max(max_number):
    fibonacci_list = [0, 1]
    current_fibonacci = fibonacci_list[-1]
    while current_fibonacci <= max_number:
        fibonacci_list += [fibonacci_list[-2] + fibonacci_list[-1]]
        current_fibonacci = fibonacci_list[-1]
    fibonacci_list.pop(-1)
    return fibonacci_list


for i in fibonacci_max(90):
    print(i)
