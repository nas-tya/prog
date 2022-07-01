# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром Survived;
2) полом человека и параметром Survived;
3) классом, в котором пассажир ехал, и параметром Survived.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 
"""

import pandas as pd
import numpy as np
import math
# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pd.read_csv('train.csv', index_col="PassengerId")

print("Часть 1\n")

# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    male_int, female_int = data['Sex'].value_counts()
    print("Женщины: ", female_int, "    мужчины: ", male_int)

    return male_int, female_int


get_sex_distrib(data)


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = data['Embarked'].value_counts()
    print("Порт S: ", port_S, "    порт C: ", port_C, "    порт Q: ", port_Q)

    return port_S, port_C, port_Q


get_port_distrib(data)


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died = data['Survived'].value_counts()[0]
    perc_died = data['Survived'].value_counts(
        normalize=True
    )[0] * 100  # normalize=True returns the relative frequency by dividing all values by the sum of values
    print("Погибло: ", n_died, "    в процентах это: ", round(perc_died, 2))

    return n_died, perc_died


get_surv_percent(data)


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_3_cl, n_pas_1_cl, n_pas_2_cl = data['Pclass'].value_counts(
        normalize=True) * 100
    print("1 класс: ", round(n_pas_1_cl, 2), "    2 класс:",
          round(n_pas_2_cl, 2), "    3 класс:", round(n_pas_3_cl, 2))

    return n_pas_3_cl, n_pas_1_cl, n_pas_2_cl


get_class_distrib(data)


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    pearson = data['SibSp'].corr(data['Parch'], method='pearson')
    print("Коэффициент корреляции Пирсона между супругами и детьми: ",
          round(pearson, 2))

    return pearson


find_corr_sibsp_parch(data)


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;

    """
    corr_val = data['Age'].corr(data['Survived'], method='pearson')

    print("Корреляция между возрастом и выживаемостью: ", round(corr_val, 2))
    return corr_val


find_corr_age_survival(data)


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром Survived;
    """
    isex, isurvived = [], []
    for el in range(len(data)):
        if data.iloc[el]['Sex'] == 'male':
            isex.append(1)
        else:
            isex.append(0)
        isurvived.append(data.iloc[el]['Survived'])
    corr_val = pd.Series(isex).corr(pd.Series(isurvived), method='pearson')

    print("Корреляция между полом и выживаемостью: ", round(corr_val, 2))
    return corr_val


find_corr_sex_survival(data)


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром Survived.
    """

    corr_val = data['Pclass'].corr(data['Survived'], method='pearson')

    print("Корреляция между классом и выживаемостью: ", round(corr_val, 2))
    return corr_val


find_corr_class_survival(data)


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = data['Age'].mean(), data['Age'].median()

    print("Средний возраст: ", round(mean_age, 2), "     медиана: ",
          round(median, 2))
    return mean_age, median


find_pass_mean_median(data)


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = data['Fare'].mean(), data['Fare'].median()

    print("Средняя цена за билет: ", round(mean_price, 2), "     медиана: ",
          round(median, 2))
    return mean_price, median


find_ticket_mean_median(data)


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """

    pass


# find_popular_name(data)


# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    
    pass


find_popular_adult_names(data)

# ------------------------------
# Part 2
# Для набора данных из лабораторной работы 1 посчитать средние значения, медианы, максимальные и минимальные значения для столбцов Offline Spend, Online Spend.

print("\nЧасть 2 \n")

data2 = pd.read_csv('MarketingSpend.csv')

print("Среднее значение для Offline Spend: ", round(data2['Offline Spend'].mean(), 2))
print("Среднее значение для Online Spend: ", round(data2['Online Spend'].mean(), 2))

print("Медиана для Offline Spend: ", round(data2['Offline Spend'].median(), 2))
print("Медиана для Online Spend: ", round(data2['Online Spend'].median(), 2))

def get_max_and_min(data, column):
    max, min = data[column].max(), data[column].min()
    return f"Для {column} максмальное значение {max}, минимальное {min}"

print(get_max_and_min(data2, 'Online Spend'))
print(get_max_and_min(data2, 'Offline Spend'))


