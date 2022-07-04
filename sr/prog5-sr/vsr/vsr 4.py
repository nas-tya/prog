import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, mean_squared_error

"""Считываем информацию из файла с исходными данными, выбираем необходимые нам колонки, сбрасываем nan'ы"""

data = np.genfromtxt("ourdata.txt", delimiter=",")
x = data[:,0] # square_house
y = data[:,2] # cost

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

"""# Линейная модель с учётом размера жилья"""

# линейная с учетом размера жилья
f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)
f1 = np.poly1d(f1p)

fx = np.linspace(min(x), max(x),500) 

plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.title("Зависимость стоимости от площади")
plt.xlabel("площадь")
plt.ylabel("цена")
plt.show()

test = [1650, 2200]

for i in test:
  print('Площадь = {}, возможная стоимость = {}'.format(i, f1(i)))


print('MAE: ', mean_absolute_error(y, [f1(i) for i in x]))
print('MSE: ', mean_squared_error(y, [f1(i) for i in x]))

"""# Полиномиальная (вторая степень) модель с учётом размера жилья"""

# полиномиальная (2) с учетом размера жилья
f2p, residuals, rank, sv, rcond = np.polyfit(x, y, 2, full=True)
f2 = np.poly1d(f2p)

fx = np.linspace(min(x), max(x),500) 

plt.scatter(x, y, s=10)
plt.plot(fx,f2(fx),linewidth=1.0,color='r')
plt.title("Зависимость стоимости от площади")
plt.xlabel("площадь")
plt.ylabel("цена")
plt.show()
test = [1650, 2200]

for i in test:
  print('Площадь = {}, возможная стоимость = {}'.format(i, f2(i)))


print('MAE: ', mean_absolute_error(y, [f2(i) for i in x]))
print('MSE: ', mean_squared_error(y, [f2(i) for i in x]))

