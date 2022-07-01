def sample(lst):
    lst_5 = lst[len(lst) // 4::-2]
    sum_of_5 = sum(lst_5)
    lst_10 = lst[1:len(lst) // 2 - 1:2]
    sum_of_10 = sum(lst_10)
    return sum_of_5, sum_of_10


def main():
    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                   610, 987, 1597, 2584, 4181, 6765, 10946]
    print(sample(fib_numbers))


main()