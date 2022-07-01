"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg


"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """
        sums = {'Offline': 0, 'Online': 0}
        for _l in data:
            sums['Offline'] += _l['Offline']
            sums['Online'] += _l['Online']

        self._mean = (sums['Offline'] / len(data), sums['Online'] / len(data))

        return self._mean

    @property
    def max(self):
        self._max = {'Offline': 0, 'Online': 0}
        for _el in self._data:
            if _el['Online'] > self._max['Online']:
                self._max['Online'] = _el['Online']
            if _el['Offline'] > self._max['Offline']:
                self._max['Offline'] = _el['Offline']
        return self._max

    @property
    def min(self):
        self._min = {'Offline': 10000, 'Online': 10000}
        for _el in self._data:
            if _el['Online'] < self._min['Online']:
                self._min['Online'] = _el['Online']
            if _el['Offline'] < self._min['Offline']:
                self._min['Offline'] = _el['Offline']
        return self._min

    @property
    def disp(self): # делённая на n сумма квадрата разности текущего элемента и среднего значения
        mean = self.get_mean(self._data)
        self._disp = {'Offline': 0, 'Online': 0}
        for _el in self.data:
            self._disp['Offline'] += pow((_el['Offline'] - mean[0]), 2)
            self._disp['Online'] += pow((_el['Online'] - mean[1]), 2)
        self._disp = {'Offline': self._disp['Offline']/len(self.data),'Online': self._disp['Online']/len(self.data)}
        return self._disp

    @property
    def sigma_sq(self): # корень из дисперсии
        from math import sqrt
        self._sigma_sq = (sqrt(self._disp['Offline']),
                          sqrt(self._disp['Online']))
        return self._sigma_sq
