from time import sleep
from threading import Timer
from typing import List
import random

def randomnubmers(n):
    arr = [random.randint(0, 30) for i in range(n)]
    return arr

  
# сортировка по таймеру (чем больше числа - тем хуже работает)
def sleepsort(items: List, reverse: bool = False) -> List:
    result = []
    def add(x):
        result.append(x)

    max_value = items[0]
    for item in items:
        if item > max_value:
            max_value = item

        Timer(item, add, [item]).start()

    sleep(max_value + 1)
    
    if reverse:
        return result[::-1]
    else:
        return result

def main():
  arr = randomnubmers(20)
  print(sleepsort(arr))

main()