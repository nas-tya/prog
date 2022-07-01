"""
    Разработать программу для считывания данных JSON-формата из файла и вывод
    их в табличном виде на экран.
"""


def main():
    handle = open('MOCK_DATA.json')
    lines = handle.readlines()
    di, keys = dictionary(lines)
    handle.close()
    str0, str1 = table(di, keys)
    print(str0)
    print(str1)


def dictionary(lines):
    """
        Формирование словаря из файла
    """
    l = []
    keys = []
    s = 0
    for line in lines:
        d = {}
        k = line.find('"')
        line = line+","
        for i in line:
            begin = line.find(":", k)
            if begin != -1:
                end = line.find(",", begin)
                if end != -1:
                    key = line[k:begin].strip(",").strip('"')
                    value = line[begin:end].strip(":").strip("}").strip('"').strip("]").strip("}").strip('"')
                    d.update({key: value})
                    if s == 0:
                        keys.append(key)
                    k = end
            else:
                k += 1
        s += 1
        l.append(d)
    return l, keys


def table(di, keys):
    """
        >>> table([{"id":1,"first_name":"Susann","last_name":"Wyldish"},{"id":2,"first_name":"Oliy","last_name":"Bruton"}], ["id", "first_name", "last_name"])
        ('|id                         ||first_name                 ||last_name                  |', '|                          1||Susann                     ||Wyldish                    |\\n\\r|                          2||Oliy                       ||Bruton                     |\\n\\r')
    """
    str0 = ""
    str1 = ""
    s = 0
    for l in di:
        for i in keys:
            if s== 0:
                str0 += "|{:27}|".format(i)
            str1 += "|{:27}|".format(l[i])
        str1 += "\n\r"
        s += 1
    return str0, str1


main()

if __name__ == '__main__':
    import doctest
    doctest.testmod()