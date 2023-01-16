# Написание программы для численного интегрирования площади под кривой.
import timeit
import math


def integrate(f, a, b, n_iter):
    step = (b - a) / n_iter
    x = a
    s = 0
    while x <= (b - step):
        s += f(x)
        x += step
    return round(s * step, 8)


print(integrate(lambda x: math.sin(x), 1, 2, 1000))

# а и b - диапазон интегрирования
# f - функция (например, sin, cos, tan, ...) # может быть любая функция из библиотеки math

if __name__ == '__main__':

    # tests
    assert round(integrate(lambda x: 2 * x * x, 1, 2, 1000), 2) == 4.66
    assert round(integrate(lambda x: 2 * x, 2, 4, 1000), 2) == 12.00
    assert round(integrate(lambda x: 7 * x, 1, 5, 10000), 0) == 84

    # timing
#  print(timeit.timeit("integrate(lambda x: x+1, 0, 1, 10)",
# setup="from integrate import integrate"))
#  print(timeit.timeit("integrate(lambda x: x+1, 0, 1, 100)",
# setup="from integrate import integrate"))
#  print(timeit.timeit("integrate(lambda x: x+1, 0, 1, 1000)",
# setup="from integrate import integrate"))
#  print(timeit.timeit("integrate(lambda x: x+1, 0, 1, 10000)",
# setup="from integrate import integrate"))

# python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate" "integrate(lambda x: x*x, 1, 2, n_iter=10**4)"
  # 1000 loops, best of 100: 2.28 msec per loop

