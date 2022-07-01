# Задание: на основе кода, позволяющего визуализировать
# данные о ценах на недвижимость (точечная диаграмма), отобразить
# с помощью библиотеки mathplotlib линейный график и график
# полинома второй степени (квадратичный) соответствующий изменениям
# цен на недвижимость.



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


data = np.genfromtxt("ISR4-1.csv", delimiter=";",
                     skip_header=1, names=["Price", "District"], dtype=None,
                     encoding=None)
fig, ax1 = plt.subplots()
ax1.plot(data["Price"], data["District"])
plt.xlabel("Prices")
plt.ylabel("Districts")
plt.show()
