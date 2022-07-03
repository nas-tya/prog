import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("property_value.csv", delimiter=",")
area = data[:, 0]
quantity = data[:, 1]
cost = data[:, 2]

area = area[~np.isnan(area)]
quantity = quantity[~np.isnan(quantity)]
cost = cost[~np.isnan(cost)]

mean_area = np.mean(area)
mean_quantity = np.mean(quantity)
mean_cost = np.mean(cost)

dispersion_area = np.var(area)
dispersion_quantity = np.var(quantity)
dispersion_cost = np.var(cost)

std_area = np.std(area)
std_quantity = np.std(quantity)
std_cost = np.std(cost)

f1p = np.polyfit(area, cost, 1, full=False)
f1 = np.poly1d(f1p)
fx = np.linspace(0, area, 500)

plt.scatter(area, cost, s=10)
plt.plot(fx, f1(fx), linewidth=1.0, color="y")
plt.title("Стоимость квартиры в зависимости от площади")
plt.xlabel("Площадь")
plt.ylabel("Стоимость")
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color="0.9")
print(f1([1650.3]))  # прогнозирование
plt.show()
