def count_parity(str: str):
    open_parenthesis, close_parenthesis = 0, 0
    while len(str) > 0:
        c = str[0]
        str = str[1:]
        if c == "(":
            open_parenthesis += 1
        elif c == ")":
            close_parenthesis += 1
        yield [open_parenthesis, close_parenthesis]


def main():
    string = input("Введите текст: ")
    p = [p for p in count_parity(string)][-1]
    print(p[0] == p[1], p)


main()
