import numpy as np
import random
import time


def main():
    n_A = int(input("Введите размер n матрицы A: "))
    m_A = int(input("Введите размер m матрицы A: "))
    n_B = int(input("Введите размер n матрицы B: "))
    m_B = int(input("Введите размер m матрицы B: "))
    print()
    if m_A == n_B:
        A = np.array([[random.randint(1, 10) for j in range(m_A)] for i in range(n_A)])
        print(A, "\n")
        B = np.array([[random.randint(1, 10) for j in range(m_B)] for i in range(n_B)])
        print(B, "\n")
        C = A.dot(B)
        print(C, "\n")
    else:
        print("Невозможно произвести умножение матриц заданного размера.")


start_time = time.time()
main()
print("--- %s секунд(у,ы) ---" % (time.time() - start_time))
