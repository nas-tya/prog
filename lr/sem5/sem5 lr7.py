from urllib.request import urlopen
from xml.etree import ElementTree as ET
from prettytable import PrettyTable
import json


class BaseCurrenciesList():
    def get_currencies(self, currencies_ids_lst: list) -> dict:
        pass


class CurrenciesList(BaseCurrenciesList):
    """
        aka Concretwrapped_object
    """
    def __init__(self):
        print("This is initialization")

    def __str__(self):
        return str(self.get_currencies())

    def get_currencies(self, currencies_ids_lst=None) -> dict:

        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01010', 'R01020A', 'R01270', 'R01335', 'R01535'
            ]

        cur_res_str = urlopen('http://www.cbr.ru/scripts/XML_daily.asp')

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


class Decorator(BaseCurrenciesList):
    """
    aka Decorator из примера паттерна
    """
    _wrapped_object: BaseCurrenciesList = None

    def __init__(self, wrapped_object: BaseCurrenciesList) -> None:
        self._wrapped_object = wrapped_object

    @property
    def wrapped_object(self) -> str:
        return self._wrapped_object

    def get_currencies(self, currencies_ids_lst: list) -> dict:
        return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):
    def __str__(self, currencies_ids_lst=None):
        return self.get_currencies(currencies_ids_lst)

    def get_currencies(self, currencies_ids_lst: list) -> str:  # JSON
        return json.dumps(self._wrapped_object.get_currencies(currencies_ids_lst), ensure_ascii=False, indent = 3)



class ConcreteDecoratorCSV(Decorator):
    def __str__(self, currencies_ids_lst=None):
        return self.get_currencies(currencies_ids_lst)

    def get_currencies(self, currencies_ids_lst: list) -> str:  # CSV
        currency = self._wrapped_object.get_currencies(currencies_ids_lst)
        csv = "id, rate, name \n"
        for currency, val in currency.items():
            row = [currency, *val]
            csv += ', '.join(row) + '\n'
        csv = csv.rstrip()
        return csv


class ConcreteDecoratorTable(Decorator):
    def __str__(self, currencies_ids_lst=None):
        return self.get_currencies(currencies_ids_lst)

    def get_currencies(self, currencies_ids_lst: list) -> str:  # table
        x = PrettyTable()
        currency = self._wrapped_object.get_currencies(currencies_ids_lst)
        x.field_names = ["id", "rate", "name"]
        for currency, val in currency.items():
            x.add_row([currency, *val])
        return x


def show_currencies(currencies: BaseCurrenciesList, currencies_ids_lst=None):
    """
       aka client_code() 
    """

    print(currencies.__str__(currencies_ids_lst))


if __name__ == "__main__":

    curlistdict = CurrenciesList()  # base

    wrappedcurlist = Decorator(curlistdict)
    wrappedcurlist_json = ConcreteDecoratorJSON(curlistdict)
    wrappedcurlist_csv = ConcreteDecoratorCSV(curlistdict)
    wrappedcurlist_table = ConcreteDecoratorTable(curlistdict)

    print('\n Табличный вывод:')
    show_currencies(wrappedcurlist_table)
    print('\n Вывод в csv:')
    show_currencies(wrappedcurlist_csv)
    print('\n Вывод в json:')
    show_currencies(wrappedcurlist_json)
