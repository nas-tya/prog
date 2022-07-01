import math


def count_digits(b):

    if b > 0:
        digits = int(math.log10(b)) + 1
    elif b == 0:
        digits = 1

    return digits


def squareSequenceDigit(n):
    sqrtseq = []

    i = 1

    while i < 20:
        sqrtseq.append(i * i)
        i += 1

    k = 0
    output = []
    while k < len(sqrtseq):

        numb = int(sqrtseq[k])

        if count_digits(numb) == 1:
            output.append(numb)

        if count_digits(numb) == 2:
            output.append(numb // 10)
            output.append(numb % 10)

        if count_digits(numb) == 3:
            output.append(numb // 100)
            output.append((numb // 10) % 10)
            output.append(numb % 10)

        k += 1

    return output[n - 1]


if __name__ == "__main__":
    print(squareSequenceDigit(1))
    print(squareSequenceDigit(2))
    print(squareSequenceDigit(7))
    print(squareSequenceDigit(12))
    print(squareSequenceDigit(17))
    print(squareSequenceDigit(27))