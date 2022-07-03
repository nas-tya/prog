import math
import pytest


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        print("Уравнение не имеет корней.")
        return None
    elif d == 0:
        return [-b / (2 * a), None]
    else:
        return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]


def main():
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    print(quadratic_equation(a, b, c))


def test_1():
    assert quadratic_equation(4, -4, 1) == [0.5, None]


def test_2():
    assert quadratic_equation(1, -5, 6) == [3.0, 2.0]


def test_3():
    assert quadratic_equation(1, 2, 3) is None


main()
