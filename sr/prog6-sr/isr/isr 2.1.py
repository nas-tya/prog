def fibonacci_generator(n):
    value = 1
    if n == 0:
        value = 0
    if n > 2:
        value = fibonacci_generator(n - 1) + fibonacci_generator(n - 2)
    return value


def fibonacci_yield(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    numbers = 8
    generator_list = [fibonacci_generator(i) for i in range(numbers + 1)]
    print(generator_list)

    fibonacci_yield_function = fibonacci_yield(numbers)
    for i in range(numbers):
        print(fibonacci_yield_function.__next__())


main()
