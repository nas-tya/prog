# Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

import random


def randomnubmers(n):
    arr = [random.randint(0, 1000) for i in range(n)]
    return arr


# сортировка вставкой
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# плавная сортировка
def smoothsort(arr):
    leo_nums = leonardo_numbers(len(arr))
    heap = []
    for i in range(len(arr)):
        if len(heap) >= 2 and heap[-2] == heap[-1] + 1:
            heap.pop()
            heap[-1] += 1
        else:
            if len(heap) >= 1 and heap[-1] == 1:
                heap.append(0)
            else:
                heap.append(1)
        restore_heap(arr, i, heap, leo_nums)

    for i in reversed(range(len(arr))):
        if heap[-1] < 2:
            heap.pop()
        else:
            k = heap.pop()
            t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
            heap.append(k_l)
            restore_heap(arr, t_l, heap, leo_nums)
            heap.append(k_r)
            restore_heap(arr, t_r, heap, leo_nums)


# генерация чисел Леонардо, не превышающих количество элементов массива
def leonardo_numbers(max):
    a, b = 1, 1
    numbers = []
    while a <= max:
        numbers.append(a)
        a, b = b, a + b + 1
    return numbers


# восстановление кучи после слияния куч или удаления корня
def restore_heap(lst, i, heap, leo_nums):
    current = len(heap) - 1
    k = heap[current]
    while current > 0:
        j = i - leo_nums[k]
        if (lst[j] > lst[i]
                and (k < 2 or lst[j] > lst[i - 1] and lst[j] > lst[i - 2])):
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            current -= 1
            k = heap[current]
        else:
            break

    while k >= 2:
        t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
        if lst[i] < lst[t_r] or lst[i] < lst[t_l]:
            if lst[t_r] > lst[t_l]:
                lst[i], lst[t_r] = lst[t_r], lst[i]
                i, k = t_r, k_r
            else:
                lst[i], lst[t_l] = lst[t_l], lst[i]
                i, k = t_l, k_l
        else:
            break


def get_child_trees(i, k, leo_nums):
    t_r, k_r = i - 1, k - 2
    t_l, k_l = t_r - leo_nums[k_r], k - 1
    return t_r, k_r, t_l, k_l


# Основная процедура
def main(n):
    print("insertion sorting")
    lst = randomnubmers(n)
    print(lst)
    insertionsort(lst)
    print(lst)

    print("\nsmooth sorting")
    lst = randomnubmers(n)
    print(lst)
    smoothsort(lst)
    print(lst)

    print("\npython sorting")
    lst = randomnubmers(n)
    print(lst)
    print(sorted(lst))


main(20)
