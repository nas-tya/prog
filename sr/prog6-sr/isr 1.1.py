import csv
from math import sqrt


def mean(data):
    sum_numbers = sum(data)
    count_numbers = len(data)
    numbers_average = sum_numbers / count_numbers
    return numbers_average


def dispersion(data):
    numbers_average = mean(data)
    data_for_dispersion = [(x_i - numbers_average) ** 2 for x_i in data]
    sum_data = sum(data_for_dispersion)
    data_dispersion = sum_data / (len(data_for_dispersion))
    return data_dispersion


def standard_deviation(data):
    std_deviation = sqrt(dispersion(data))
    return std_deviation


def csv_reader(csv_file, col_num):
    reader = csv.reader(csv_file, delimiter=";")
    data = []
    for line in reader:
        data += [float(line[col_num - 1].replace(",", "."))]
    return data


def main():
    csv_path = "data.csv"
    column_number = 1
    with open(csv_path, newline="") as file:
        data = csv_reader(file, column_number)
    print("Среднее значение: ", mean(data))
    print("Дисперсия: ", dispersion(data))
    print("Среднее квадратичное отклонение: ", standard_deviation(data))


main()
