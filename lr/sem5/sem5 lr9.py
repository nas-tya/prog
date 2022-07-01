import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


from urllib.request import urlopen
from xml.etree import ElementTree as ET

currencies_ids_lst=['R01235', 'R01010', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A']

def get_currencies(currencies_ids_lst):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val

    return result


cur_vals = get_currencies(currencies_ids_lst)

objects = cur_vals.keys()

y_pos = np.arange(len(objects))

# Done
# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension 
# или генераторы списков (как мы их называем)

# performance = list(map(lambda x: float(x.replace(",",".")), cur_vals.values()))

performance = []
for x in cur_vals.values():
  performance.append(x.replace(',', '.'))


# Done
# TODO #2 

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков), 
# столбцы должны быть разных цветов с легендой

fig = plt.figure()
ax = fig.add_axes([0, 0, 1.2, 1])

for i in range(len(objects)):
    plt.bar(y_pos[i], performance[i])

color_rectangle = np.random.rand(7, 3)

plt.xticks(y_pos, objects)
plt.ylabel('Cost')
plt.xlabel('Valute')
plt.title('Currencies')
plt.legend(objects)


# In process
# TODO #3 

# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее 
# оптимальным образом (типом графика)

from datetime import date, datetime
import requests 

def cur_swings(currency_id):
    today_date = date.today()
    prev_year_date = today_date.replace(year=today_date.year - 1)

    p = {
        'date_req1': prev_year_date.strftime('%d/%m/%Y'),
        'date_req2': today_date.strftime('%d/%m/%Y'),
        'VAL_NM_RQ': currency_id
    }
    
    res = requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp", params=p)
    cur_res_str = res.text

    result = {}

    root = ET.fromstring(cur_res_str)

    records = root.findall('Record')
    for el in records:
        record_date = el.get('Date')
        record_value = el.find('Value').text
        result[record_date] = record_value

    return result

currency_dynamics = cur_swings('R01239')

records_dates = [datetime.strptime(x, '%d.%m.%Y') for x in currency_dynamics.keys()]
records_values = [float(x.replace(',', '.')) for x in currency_dynamics.values()]

fig = plt.figure()
ax = fig.add_axes([0, 0, 1.2, 1])
plt.plot(records_dates, records_values)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Currency Swing')
plt.show()


# done
# TODO #4 
# отобразить всё на двух графиках

fig, axs = plt.subplots(2, figsize=(6,6))
for i in range(len(objects)):
    axs[0].bar(y_pos[i], performance[i])
axs[0].legend(objects)
axs[1].plot(records_dates, records_values)
plt.show()

