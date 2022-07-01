def main():
    tup = (0, 9, 9, 1, 7, 1, 5, 5, 5, 1, 0)
    print(find(tup))


def find(*tup):
    lst = []
    lst1 = list(*tup)
    i = 0
    print(lst1[1])
    for i in range(int(len(lst1))):
        print(i)
        if i != len(lst1)+1:
            for j in range(i+1, len(lst1)):
                if lst1[i] == lst1[j]:
                    lst.append(lst1[i])
                    del lst1[j]
                    break
    return lst


main()

"""
    Разработать программу, которая для заданного количества значений возвращала
    бы список из повторяющихся элементов, содержащихся во входном наборе
    значений. Используйте упаковку и распаковку элементов.
"""