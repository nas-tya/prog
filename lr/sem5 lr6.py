"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ. Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.

Страница документации: https://cbr.ru/development/
"""

from xml.etree import ElementTree as ET  # исследовать библиотеки для парсинга xml и использовать более оптимальную библиотеку для парсинга xml (если такая есть)
import requests


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            print("get instance")
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class CurrenciesList():
    def __init__(self):
        print("This is initialization")

    def get_currencies(self, currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        result = {}

        cur_res_xml = ET.parse(cur_res_str)  # XML Tree
        root = cur_res_xml.getroot()

        valutes = root.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')

            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text

                result[valute_id] = (valute_cur_val, valute_cur_name)

        return result


if __name__ == "__main__":
    my_cur_list = CurrenciesList()
    print(id(my_cur_list))
    my_cur_list2 = CurrenciesList()
    print(id(my_cur_list2))
    print(type(CurrenciesList))
