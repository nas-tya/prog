def main():
    n=input("Введите число, факториал которого хотите получить ")
    print(factorial(n))
def factorial(n):
    e="В качестве аргументов принимаются только натуральные числа"
    try:
        n=int(n)
        if type(n) is not int:
            raise TypeError(e)    
        if n<0:
            raise TypeError(e)
    except:
         raise TypeError(e)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result


main()