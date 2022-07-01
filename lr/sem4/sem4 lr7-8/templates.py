def connect_to_db(path_to_db: str) -> object:
    """
    Connect to sqlite database
    
    :return sqlite3.Connection
    """
    pass
    # import sqlite3
    # TODO: Предусмотреть обработку исключений
    #


def create_table(table_name, domens_lst, conn):
    # TODO: Реализовать тело функции
    # примерный алгоритм:
    # проверяем есть ли conn
    # если нет, падаем / возвращаем None
    # если есть соединение, проверить есть ли таблица, если есть, то все ок и создавать не надо
    # если нет, то создадим и вернем какой-то код, если все хорошо
    pass


def insert_param_data(conn, table_name, values):
    # TODO: Реализовать тело функции
    # параметризованый запрос на добавление данных в таблицу user
    pass


# остальные функции из CRUD - по аналогии

connect_to_db()
