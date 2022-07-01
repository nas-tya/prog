import json


def load_json(f):
    """
    Считывание и загрузка json
    """

    import json
    res = []
    data = json.load(f)
    for el in data:
        res.append((el['name'], el['email']))
        print(el['name'], el['email'])

    return res


def print_json(file):
    """
    Вывод данных из json на экран
    """
    with open(file, 'r') as f:
        data = json.load(f) 
        print(json.dumps(data, indent = 1))


def save_json(data, file):
    """
    Сохранение полученных данных в json-файл
    """
    with open(file, 'at') as f:
        json.dump(data, f)


def add_users_data():
    """
    Добавление данных о пользователях с клавиатуры
    """
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = {'name': name, 'email': email}
    save_json(data, "data-output.json")


if __name__ == '__main__':
  add_users_data()
  print_json('data-output.json')
  
