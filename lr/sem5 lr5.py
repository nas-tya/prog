"""# Лабораторная работа 5. Визуализация данных о погоде с помощью matplotlib. 

Цель работы: научиться обрабатывать и визуализировать данные, 
полученные с помощью API (на примере сервиса openweathermap).

Описание работы: получить данные о погоде за 5 последний дней и визуализировать эти данные, используя диаграмму рассеяния (scatterplot). 
Затем, посчитать среднюю температуру за каждый день и построить рядом (на этом же изображении) линейную диаграмму изменения температур.

Замечание: можно использовать другие сервисы для получения прогноза погоды на 7 дней (gismeteo, 

Лабораторная работа состоит из 2-х основных частей:
1. Получение данных посредством API.
2. Визуализация данных.

Выполним все этапы и визуализируем данные о погоде только за вчерашний день: 01.11.2021.

Начнем с части 1: получим данные в формате json через API openweathermap
"""

# example of one call api openweathermap

import requests
import json

city, lat, lon = "Saint Petersburg, RU", 33.44, -94.04
api_key = '7ceb2a73fe117310664f58c02964b842'
dt = 1649671369
req = requests.get(
            f'http://api.openweathermap.org/data/2.5/'
            f'onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&'
            f'appid={api_key}&lang=ru&units=metric')

req_obj = json.loads(req.text)  # Преобразуем объект типа Request в json-формат
print(req_obj)

# key = "YOUR_PERSONAL_KEY_IS_HERE"

def getweather(api_key=None):
    import json
    import requests
    city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19

    dt = 1635765071  # datetime of 01/11/2021 in unix-like format
    # Для определения unixtime диапазона для получения температур, 
    # можно использовать сервис https://unixtime-converter.com/

    if api_key:
        result = dict()
        req = requests.get(
            f'http://api.openweathermap.org/data/2.5/'
            f'onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&'
            f'appid={api_key}&lang=ru&units=metric')
        
        # для других параметров см. https://openweathermap.org/api/one-call-api#history

        req_obj = json.loads(req.text)  # Преобразуем объект типа Request в json-формат

        # Сохраним результаты температур в формате json, чтобы ниже их визуализировать
        result['city'] = city
        measures = [{"dt": str(measure['dt']), "temp": str(measure['temp'])} for measure in req_obj["hourly"]]
        

        result['temps'] = measures
        return json.dumps(result)


weather_data_json = getweather(key)

"""При вызове этой функции, мы сможем использовать данные в формате json, которые она возвращает. Альтернативный подход - сразу же сформировать из этих данных корректный файл с данными в csv-формате (см. документацию https://docs.python.org/3/library/csv.html).

__Перейдем к шагу 2:__
визуализируем полученные данные с помощью matplotlib и типа диаграммы scatterplot.
"""

def visualise_data(json_data=''):

    if json_data:
        import matplotlib.pyplot as pplt
        import pandas
        # Мы можем загрузить данные в пригодный для дальнейшей обработки формат
        # с помощью метода read_json из pandas.
        data = pandas.read_json(json_data)
        # print(data)
        city_name = data['city']

        # получим отдельные столбцы с датами 
        dates = [_d['dt'] for _d in data['temps'][:]]
        # и тепературами
        temps = [_t['temp'] for _t in data['temps'][:]]

        # построим их на диаграмме рассеяния
        pplt.scatter(dates, temps)


        pplt.show()

        # построенный график необходимо оптимизировать:
        #  - добавить название 
        #  - правильно расположить ось абсцисс
        #  - упростить вывод дат (на этом графике они выводятся в формате unixtime)
        #  - вывести более строгие значения для подписей осей абсцисс и ординат 
        #  (xticks, yticks)
        # - добавить на график температуры остальных дат 
        # - добавить второй график со средними значениями

visualise_data(weather_data_json)

import matplotlib.pyplot as pplt


dates, temps = ['01/11', '31/10', '30/10'], [6, 10.0, 14.0]
pplt.scatter(dates, temps)

pplt.show()

"""# Новое решение Бражкина А.Д.
Через OpenWeather
"""

from datetime import datetime
import matplotlib.pyplot as pplt

def getweather(api_key=None):
    import json
    import requests
    city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19
    api_key = '7ceb2a73fe117310664f58c02964b842'
    dt = 1649671369 

    if api_key:

        req = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'APPID': api_key})
        
        data = req.json()
        dates = [] 
        temps = []

        for i in data['list']:
            temps.append(int('{0:+3.0f}'.format(i['main']['temp'])))
            dates.append(datetime.utcfromtimestamp(i['dt']).strftime('%d/%m %H'))
        print(temps, '\n', dates)
        
        date, temp, avg_t, avg_d = [], [], [], []

        for i in range(0, len(temps), 8):
            sum = 0
            temp.append(temps[i])
            date.append(dates[i])
            
            for j in range(8):
                sum += temps[i+j]

            avg_t.append(sum/8)
            avg_d.append(dates[i])

        fig, axs = pplt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
        axs[0].scatter(date, temp)
        axs[1].plot(avg_d, avg_t)

        axs[0].set_xlabel(u'Date')
        axs[0].set_ylabel(u'Temp')
        axs[0].set_title(u'5 days forecast')

        axs[1].set_xlabel(u'Date')
        axs[1].set_ylabel(u'Temp')
        axs[1].set_title(u'Average temp')
        
        pplt.show()


weather_data_json = getweather()

"""# Старое Решение, Бражкина А.Д.

Я использую API YandexWeather, инструкцию по получению ключа и комментарии к работе с этим API можно найти в ЛР2.
"""

# pip install yaweather

from yaweather import Russia, YaWeather #Yandex Weather API wrapper
import matplotlib.pyplot as pplt


api_key=''

def get_weather_data(place, api_key):

    if api_key=='':
        raise Exception('input your API key')

    y = YaWeather(api_key)
    res = y.forecast(place)
    dates = []  # list of dates
    temps = []  # list of tempurature
    for f in res.forecasts:  # forecast for 7 days
      day = f.parts.day_short
      dates.append(f.date)  # list of 7 dates
      temps.append(day.temp)  # list of 7 temps
    pplt.scatter(dates, temps, label= u"График погоды", color = red)

    pplt.grid(True)
    pplt.xlabel(u'Дата')
    pplt.ylabels(u'Температура')
    pplt.title(u'Погода')

    pplt.legend()

    pplt.show()


get_weather_data(Russia.SaintPetersburg, api_key)