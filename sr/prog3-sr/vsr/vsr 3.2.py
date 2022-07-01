import random


def main():
    granze = [int(input('Введите границы, в которых хотите угадывать число ')), int(input())]
    print(granze[1])
    game(granze)


def game(granze):
    """
       Собственно, игра
    """
    counter = 0
    flag = True
    while counter < 3 and flag:
        inp_number = int(input('Введите число '))
        r = random.randint(granze[0], granze[1])
        if inp_number >= granze[0] and inp_number <= granze[1]:
            if inp_number == r:
                print("Вы угадали!, Вы ввели число {0}, и загадано было число {1}".format(inp_number, r))
                flag = False
            else:
                print("Вы не угадали!, Вы ввели число {0}, а загадано было число {1}".format(inp_number, r))
        else:
            print('Вы ввели неверное число. Попробуйте ввести другое от {0[0]} до {0[1]}'.format(granze))
        counter += 1


main()