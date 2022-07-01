def main():
    str = input('Введите строку ' )
    shf = int(input('Введите сдвиг '))
    print(ceasar(str, shf))


def ceasar(str, shf):
    """
        Шифр Цезаря
    """
    str1 = ""
    for i in str:
        k = ord(i)
        if 65 <= k <= 90 - shf or 97 <= k <= 122 - shf or 1040 <= k <= 1071 - shf or 1072 <= k <= 1103-shf:
            k += shf
        elif 90 - shf < k <= 90 or 122 - shf < k <= 122:
            k = 64+(shf-(90-k))
        elif 1071 - shf < k <= 1071 or 1103-shf < k <= 1103:
            k = 1040+(shf-(1072-k)) 
        str1 += chr(k)
    return str1


main()