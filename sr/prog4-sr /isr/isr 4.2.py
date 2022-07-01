# Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

import random


def randomnubmers(n):
    arr = [random.randint(-1000, 1000) for i in range(n)]
    return arr

def sortingparity(arr):
  odd = []
  even = []
  for i in arr:
    if i%2 == 0:
      even.append(i)
    else:
      odd.append(i)
  print(f'Odd numbers: {odd}\neven numbers: {even}')


def sortingminusplus(arr):
  minus = []
  plus = []
  cnt = 0
  for i in arr:
    if i > 0:
      plus.append(i)
    elif i == 0:
      cnt += 1
    else:
      minus.append(i)
  print(f'Numbers greater than zero: {plus}\nnumbers less than zero: {minus}\nzeros: {cnt}')  

def main(max):
  a = randomnubmers(max)
  print(a)
  print(sortingminusplus(a))
  print(sortingparity(a))

main(20)