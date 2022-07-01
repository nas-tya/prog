# ИСР 1.2. Задание: создать пользовательский пакет для приложения
# «Гостевая книга» («Регистрация на конференцию») с прототипами
# методов, позволяющих взаимодействовать с JSON-файлом (создание,
# удаление, переименование, чтение, запись).


import json
import os


class Guestbook:
    def create_json(self, filename='guestbook.json'):
        with open(filename, 'w') as file:
            file.write('')

    def remove_json(self, filename='guestbook.json'):
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        os.remove(file_path)

    def rename_json(self, new_filename, filename='guestbook.json'):
        os.rename(filename, new_filename)

    def get_json(self, filename='guestbook.json'):
        with open(filename, 'r') as file:
            read_json = json.load(file)
        return read_json

    def write_json(self, json_text, filename='guestbook.json'):
        with open(filename, 'w') as file:
            json.dump(json_text, file, ensure_ascii=False, indent=4)

# Guestbook.create_json()
# GuestBook.remove_json('data_backup.json')
