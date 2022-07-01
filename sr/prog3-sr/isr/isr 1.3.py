"""
    Написать программу по вычисленю площади треугольника по формуле Герона
"""


def main():
    flag_enter = True
    while flag_enter:
        # Ввод сторон треугольника
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
        # Проверяем, существует ли треугольник
        if a + c > b and a + b > c and c + b > a:
            flag_enter = False
            # Находим площадь по формуле Герона
            result = heron(a, b, c)
            # И выводим ее
            print("Площадь треугольника: ", result)
        else:
            print("Треугольник не существует. Попробуйте ввести другие данные")


def heron(a, b, c):
    """
    Расчет площади треугольника по формуле Герона
    a, b, c -стороны треугольника
    """
    # Полупериметр
    p = a + b + c
    # Площадь
    result = pow(p * (p-a) * (p-b) * (p-c), 0.5)
    return result
main()