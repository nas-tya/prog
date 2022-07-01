# Лабораторная работа 4. Ряд Фибоначчи с помощью итераторов
## Бражкина А.Д., ИВТ2

Лабораторная работа состоит из трех заданий: 

1. Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.
2. Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.
3. Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools). 



## Задание 1

```python
def fib(n):
    
    res_lst = [0, 1]
    if n > 1:
        while True:
            cur_el = sum(res_lst[len(res_lst) - 2::])
            if cur_el <= n:
                res_lst.append(cur_el)
            else:
                break
    return res_lst
```

## Задание 2

```python
class FibonacciLst:
    def __init__(self, max):
        self.n, self.a, self.b, self.max = 0, 0, 1, max
        

    def __getitem__(self, x):
        if self.n < self.max:
            a, self.n, self.a, self.b = self.a, self.n + 1, self.b, self.a + self.b
            return a
            
        '''
        self.n - это счётчик
        self.a - это промежуточная переменная, хранящая в себе возвращаемый результат
        self.b - это переменная, в которой хранится сумма 
        
        Пример работы метода по итерациям:
        a: 0 -> 1 -> 1 -> 2 -> 3 -> 5  -> 8
   self.n: 1 -> 2 -> 3 -> 4 -> 5 -> 6  -> 7
   self.a: 1 -> 1 -> 2 -> 3 -> 5 -> 8  -> 13
   self.b: 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21
   return: 0 -> 1 -> 1 -> 2 -> 3 -> 5  -> 8
        '''
            
        else:
            raise IndexError


def check(x, n):
    res = []
    for el in x:
        if el <= n:
            res.append(el)
    return res


def main():

    lst = []
    n = 50
    fib_iter = FibonacciLst(n+1)

    for el in fib_iter:
        lst.append(el)

    
    print(check(lst, n))

```

## Задание 3

```python
from itertools import islice


def fib(n):
    res_lst = [0, 1]
    if n > 1:
        while True:
            cur_el = sum(res_lst[len(res_lst) - 2::])
            if cur_el <= n:
                res_lst.append(cur_el)
            else:
                break
    return res_lst


def fibiter(n):
    res = []
    for el in islice(fib(n), n):
        if el <= n:
            res.append(el)
    return res


def main():
  print(fibiter(10))
  
```

# Задание 4

```python
def my_genn(n):
    a, b = 0, 1
    while True:
        for _ in range(n):
          yield a
          a, b = b, a + b
        
        
def main():
  x = 50
  g = my_genn(x)

  while True:
    el = next(g)
    if el > x:
        break
    print(el)
```
