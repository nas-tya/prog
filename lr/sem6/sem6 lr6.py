# -*- coding: utf-8 -*-
"""Бражкина А.Д. ЛР 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3KgNwapshjygE0c1yDm_S-oES4ErBG1

# ЛР 6
Бражкина А.Д.

Импортируем необходимые пакеты
"""

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

"""# Полиномиальная модель (3 степень) с учётом размера жилья"""

# полиномиальная (3) с учетом размера жилья
f3p, residuals, rank, sv, rcond = np.polyfit(x, y, 3, full=True)
f3 = np.poly1d(f3p)

fx = np.linspace(min(x), max(x),500) 

plt.scatter(x, y, s=10)
plt.plot(fx,f3(fx),linewidth=1.0,color='r')
plt.title("Зависимость стоимости от площади")
plt.xlabel("площадь")
plt.ylabel("цена")
plt.show()

test = [1650, 2200]

for i in test:
  print('Площадь = {}, возможная стоимость = {}'.format(i, f3(i)))


print('MAE: ', mean_absolute_error(y, [f3(i) for i in x]))
print('MSE: ', mean_squared_error(y, [f3(i) for i in x]))

"""# Линейная модель с учётом размера жилья и количества комнат"""

# линейная с учетом размера жилья и количества комнат
x = data[:,[0, 1]] # square_house and rooms
y = data[:,2] # cost

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

model = LinearRegression()
model.fit(x, y)

test = [[1650, 3], [2200, 4]]
pred = model.predict(test)

for i in range(0, 2):
    print('Площадь = {}, количество комнат = {}, возможная стоимость = {}'.format(test[i][0], test[i][1], pred[i]))

print('MAE: ', mean_absolute_error(y, model.predict(x)))
print('MSE: ', mean_squared_error(y, model.predict(x)))

"""Визуализация модели с несколькими фичами, взятая с https://medium.com/swlh/multi-linear-regression-using-python-44bd0d10082d"""

import seaborn as sns

# линейная с учетом размера жилья и количества комнат

X = data[:,[0, 1]] # square_house and rooms
Y = data[:,2] # cost

X = X[~np.isnan(y)]
Y = Y[~np.isnan(y)]

x = X[:, 0]
y = X[:, 1]
z = Y

xx_pred = np.linspace(min(x), max(x), 500)  # площадь
yy_pred = np.linspace(1, max(y))  # комнаты
xx_pred, yy_pred = np.meshgrid(xx_pred, yy_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

ols = LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

# Evaluate model by using it's R^2 score 
r2 = model.score(X, Y)

# построение графика
plt.style.use('fivethirtyeight')

fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
    ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
    ax.set_xlabel('Площадь', fontsize=12)
    ax.set_ylabel('Комнаты', fontsize=12)
    ax.set_zlabel('Цена', fontsize=12)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')

# отображение графиков (как они повернуты, куда смотрят)) 
ax1.view_init(elev=15, azim=40)
ax2.view_init(elev=15, azim=15)
ax3.view_init(elev=25, azim=60)

fig.suptitle('Зависимость стоимости от площади и количества комнат' % r2, fontsize=15, color='k')

fig.tight_layout()

"""# Выводы

Я оценивала две ошибки: MAE и MSE.

MAE - Mean Average Error

![image.png](data:image/png;base64,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)

MSE - Mean Squared Error

![image.png](data:image/png;base64,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)


MSE более чувствительная метрика, поэтому значения получились больше. 


"""