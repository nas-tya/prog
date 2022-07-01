# Задание: используя свободные источники (bn.ru, avito.ru и
# т. д.), собрать данные о ценах на недвижимость, выставленную на
# продажу в разных районах города. Преобразовать данные в формат
# csv. Разработать скрипт для визуализации данных, используя
# библиотеку matplotlib. Для визуализации использовать тип “точечная
# диаграмма” (scatterplot).



import csv
import numpy as np
import matplotlib.pyplot as plt


with open("ISR4-1.csv") as file:
    csv_reader = csv.reader(file, delimiter=";")
    line_number = 0
    for row in csv_reader:
        if line_number == 0:
            print(f"Имена столбцов: {', '.join(row)}.\n")
            line_number += 1
        else:
            print(f"Квартира за {row[0]} руб. находится в {row[1]}.")


data = np.genfromtxt("ISR4-1.csv", delimiter=";", skip_header=1,
                     names=["Price", "District"], dtype=None, encoding=None)
fig, ax1 = plt.subplots()
ax1.scatter(x=data["Price"], y=data["District"], color="b",
            label="Real estate prices")
plt.xlabel("Prices")
plt.ylabel("Districts")
plt.show()
