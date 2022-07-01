# классы - виды запросов (select, update, insert)

# класс - структура/сущность со структурой, которую реализует какой-то конкретный объект
# например пользователь Elena или Irina


class User():
    def __init__(self, name, height):
        if all(self.__check_name(name), self.__check_height(height)) == True:
            self.__name = name
            self.__height = height
        else:
            raise ValueError
            # рекомендация для проверки использовать функцию all
            # и поднять исключение, если all вернула False с помощью   raise

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (self.__check_name(name) == 1):
            self.__name = name
        else:
            raise ValueError

        if name == None:
            del self.name

    @name.deleter
    def name(self):
        print('deleter')

    @property
    def height(self):
        print('height')
        return self.__height

    @height.setter
    def height(self, height):
        if (self.__check_height(height) == 1):
            self.__height = height
        else:
            raise ValueError

        if height == None:
            del self.height

    @height.deleter
    def height(self):
        print('deleter')

    def __check_height(self, height):
        height = float(height)
        if type(height) is float:
            return True
        else:
            return False

    def __check_name(self, name):
        if (len(name) < 3):
            raise False
        else:
            return True

    def select(self, conn, sqlquery):
        sqlquery = "SELECT (?,?) FROM user WHERE (???)"



def singleton(cls):
    import functools
    instance = None
    
    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    
    return inner


@singleton
class Connection():
    def __init__(self, dbfile, dbtype='sqlite'):
        
        if not (self.__check_file(dbfile) == 1):
            return 'Файла не существует или он пустой'
        # проверка наличия файла с БД 

        self.__filename = dbfile
        self.__conn = None
        self.__cursor = None

    def __check_file(self, dbfile):
        from os.path import isfile, getsize

        self.__filename = dbfile

        if not isfile(self.__filename):
            return False

        if getsize(self.__filename) < 100:
            return False

        else:
            return True

    def connect(self):
        import sqlite3
        self.__conn = sqlite3.connect(self.__filename)
        self.__cursor = self.__conn.cursor()
        return self.__conn

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor


c = Connection('zhukov.db')
c.connect()  
c.conn  
c1 = Connection('zhukov123.db')

print(id(c1), id(c))

print(type(c))

# # READ aka SELECT
crud_read_str = "SELECT * FROM user"


# "SELECT * FROM user WHERE name='Konstantin'"
curs = c.cursor
crud_res = curs.execute(crud_read_str)

for r in crud_res:
    print(r)

