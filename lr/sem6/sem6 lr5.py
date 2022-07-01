# Лабораторная работа 5
"""
Бражкина А.Д.

Решение задачи регрессии.

Есть файл web_traffic.tsv, который представляет статистику посещений веб-сервера компании и нашей задачей является предсказание значения посещения, для того, чтобы выделить в нужный момент времени дополнительную мощность сервера и не допустить его перегрузки.

Слева находится индекс или номер часа по порядку, в который производился замер посещаемости, а справа - количество запросов сайта за этот час.
"""

import pandas as pd
import scipy as sp

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

data = pd.read_csv('web_traffic.tsv',delimiter='\t',names=["hour", "requests"]).dropna() # рефакторинг: dropna отсеивает nan

target_var_name = 'requests'

hours_data = data['hour']
requests_data = data[target_var_name]

import numpy as np
from numpy import isnan

# TO REFACTOR
# hours_data = hours_data[~isnan(requests_data)]
# requests_data = requests_data[~isnan(requests_data)]
# исследовали библитеку pandas и нашли способ отсеивать значения nan 
# более элегантно или эффективно

requests_data.head()

plt.scatter(hours_data, requests_data, s=3)
plt.title('Трафик веб-сайта за последний месяц')

plt.xlabel('время')
plt.ylabel('запросы/час')

plt.xticks([w*7*24 for w in range(10)],["неделя %i" %w for w in range(10)])
plt.autoscale(tight=False)

plt.grid(True, linestyle='-', color='0.8')
plt.show()

from sklearn.metrics import mean_squared_error

def error(f,x,y):
    return np.sum((f(x)-y)**2)
    # return mean_squared_error(f(y), x)

# Рефакторинг этой функции: найти в документации каким образом 
# вычисляется mse с помощью функции из scikit-learn

# два предположения по поводу тренда: 

# 1 - предполагаем один тренд линейный или степенной тренд
# 2 - не один тренд, а два - линейных или один линейный, а второй - степенной
# где-то по границе 3.5 недели

f1p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 1, full=True)
print("Параметры модели {}".format(f1p))

f1 = np.poly1d(f1p)
print(f"{error(f1, hours_data, requests_data):.5}")

"""Таким образом, наша модель будет выглядеть следующим образом:
```
    f(x) = 2.59619213 * x + 989.02487106
```
MSE = 3.1739e+08
"""

plt.title('Трафик веб-сайта за последний месяц')
plt.xlabel('время')
plt.ylabel('запросы/час')
plt.xticks([w*7*24 for w in range(10)],["неделя %i" %w for w in range(10)])
plt.autoscale(tight=False)
plt.grid(True, linestyle='-', color='0.8')

# визуализация данных
plt.scatter(hours_data, requests_data, s=3)

# отобразим модель #1 
f1x = np.linspace(0, hours_data[len(hours_data)], len(hours_data))
f1y = f1(f1x)
plt.plot(f1x, f1y, linewidth=1.0, color='red')

plt.show()

"""## Самостоятельная работа (~ 20 минут)

1. Реализовать модели степени полинома 2, 3, 5, 10, 20
2. Посчитать для каждой из них метрику ошибки MSE и дать характеристику того, что получилось.
3. Визуализировать каждую модель на графике так, чтобы это было отображено на одной координатной плоскости.


В дискорде в личном сообщении написать в качестве ответа следующее: 

1. Параметры модели (вектор чисел) x5 (для каждой модели)
2. Метрику MSE (x5) для каждой модели.
3. Скриншот с графиками: 7 графиков (scatterplot (done), линия для степени полинома 1 (done), график для степени полинома 2, 3, 5, 10, 20)

Цвета для графиков степеней полинома: 
- 1 - black
- 2 - blue
- 3 - lime
- 5 - magenta
- 10 - cyan
- 20 - red
"""

# создание моделей степени полинома 2, 3, ... 20
f2p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 2, full=True)
f2 = np.poly1d(f2p)
print("Параметры модели 2 (степень полинома 2) {}".format(f2p))
print(f"MSE = {error(f2, hours_data, requests_data):.5}\n")

f3p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 3, full=True)
f3 = np.poly1d(f3p)
print("Параметры модели 3 (степень полинома 3) {}".format(f3p))
print(f"MSE = {error(f3, hours_data, requests_data):.5}\n")

f5p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 5, full=True)
f5 = np.poly1d(f5p)
print("Параметры модели 5 (степень полинома 5) {}".format(f5p))
print(f"MSE = {error(f5, hours_data, requests_data):.5}\n")

f10p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 10, full=True)
f10 = np.poly1d(f10p)
print("Параметры модели 10 (степень полинома 10) {}".format(f10p))
print(f"MSE = {error(f10, hours_data, requests_data):.5}\n")

f20p, residuals, rank, sv, rcond = np.polyfit(hours_data, requests_data, 20, full=True)
f20 = np.poly1d(f20p)
print("Параметры модели 20 (степень полинома 20) {}".format(f20p))
print(f"MSE = {error(f20, hours_data, requests_data):.5}")

plt.title('Трафик веб-сайта за последний месяц')
plt.xlabel('время')
plt.ylabel('запросы/час')
plt.xticks([w*7*24 for w in range(10)],["неделя %i" %w for w in range(10)])
plt.autoscale(tight=False)
plt.grid(True, linestyle='-', color='0.8')

# визуализация данных
plt.scatter(hours_data, requests_data, s=3)

# отобразим модель #1 (степень полинома 1)
fx = np.linspace(0, hours_data[len(hours_data)], len(hours_data))
f1y = f1(fx)
plt.plot(fx, f1y, linewidth=1.0, color='black')

# отобразим модель #2 (степень полинома 2)
f2y = f2(fx)
plt.plot(fx, f2y, linewidth=1.0, color='blue')

# отобразим модель #3 (степень полинома 3)
f3y = f3(fx)
plt.plot(fx, f3y, linewidth=1.0, color='lime')

# отобразим модель #5
f5y = f5(f1x)
plt.plot(f1x, f5y, linewidth=2.0, color='magenta')

# отобразим модель #10 
f10y = f10(f1x)
plt.plot(f1x, f10y, linewidth=2.0, color='cyan')

# отобразим модель #20
f20y = f20(f1x)
plt.plot(f1x, f20y, linewidth=2.0, color='red')



plt.show()

divider = int(3.5*7*24)
divider2 = int(4.1*7*24)
print(divider, divider2)
# print(hours_data.shape)
hours_data_1, requests_data_1 = hours_data[:divider], requests_data[:divider]
hours_data_2, requests_data_2 = hours_data[divider:divider2], requests_data[divider:divider2]

hours_data_test, requests_data_test = hours_data[divider2:], requests_data[divider2:]

print(requests_data_1.shape, requests_data_2.shape, requests_data_test.shape)

f3p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 3, full=True)
f3 = np.poly1d(f3p)
print(f"MSE (для данных ДО 3.5 недели)= {error(f3, hours_data_1, requests_data_1):.5}")
print(f"MSE (только для данных с 3.5 недели)= {error(f3, hours_data_2, requests_data_2):.5}")

f20p, residuals, rank, sv, rcond = np.polyfit(hours_data_2, requests_data_2, 20, full=True)
f20 = np.poly1d(f20p)
print(f"MSE (для данных c 3.5 недели по 4.1 недели)= {error(f20, hours_data_2, requests_data_2):.5}")
print(f"MSE (только для данных с 3.5 недели)= {error(f20, hours_data_test, requests_data_test):.5}")

"""# Ответить на вопрос

Какая модель для гипотезы, при которой весь набор данных представляет собой два диапазона значений (от 0 недели до 3.5 недели и с 3.5 недели до конца), подходит наилучшим образом?
Модель, в данном случае, это степень полинома. 
Мы уже знаем (см. ячейку выше), что степень полинома 20 плохо подходит для тестовых данных (hours_data_test и requests_data_test) потому что ошибка для тестовых данных на 9 порядков выше, чем ошибка для тренировочного набора данных.
"""

hours_data_2, requests_data_2 = hours_data[divider:], requests_data[divider:]

# 1

f1p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 1, full=True)
f1 = np.poly1d(f1p) 

lerr = error(f1, hours_data_1, requests_data_1)
print(f"MSE для тренировочных данных: {lerr:.5}")
terr = error(f1, hours_data_2, requests_data_2)
print(f"MSE для тестовых данных: {terr:.5}")
print("степень 1 ^ \n")

# 2

f2p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 2, full=True)
f2 = np.poly1d(f2p) 

lerr = error(f2, hours_data_1, requests_data_1)
print(f"MSE для тренировочных данных: {lerr:.5}")
terr = error(f2, hours_data_2, requests_data_2)
print(f"MSE для тестовых данных: {terr:.5}")
print("степень 2 ^ \n")

# 3
f3p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 3, full=True)
f3 = np.poly1d(f3p) 

lerr = error(f3, hours_data_1, requests_data_1)
print(f"MSE для тренировочных данных: {lerr:.5}")
terr = error(f3, hours_data_2, requests_data_2)
print(f"MSE для тестовых данных: {terr:.5}")
print("степень 3 ^ \n")

# 5

f5p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 5, full=True)
f5 = np.poly1d(f5p) 

lerr = error(f5, hours_data_1, requests_data_1)
print(f"MSE для тренировочных данных: {lerr:.5}")
terr = error(f5, hours_data_2, requests_data_2)
print(f"MSE для тестовых данныx: {terr:.5}")
print("степень 5 ^ \n")

# 10

f10p, residuals, rank, sv, rcond = np.polyfit(hours_data_1, requests_data_1, 10, full=True)
f10 = np.poly1d(f10p) 

lerr = error(f10, hours_data_1, requests_data_1)
print(f"MSE для тренировочных данных: {lerr:.5}")
terr = error(f10, hours_data_2, requests_data_2)
print(f"MSE для тестовых данных: {terr:.5}")
print("степень 10 ^ \n")

"""Лучше брать модель 5, т.к. разница в mse наименьшая"""