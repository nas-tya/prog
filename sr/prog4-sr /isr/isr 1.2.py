# Дополнение программы для считывания данных проверкой утверждений или высказываний (assert). Создание отдельного блока для такой проверки (с помощью name) и скрипта командной строки для запуска этих проверок.

import json


def readingjson(file):
    f = None
    obj = None
    try:
        f = open(file, "rt")
        obj = json.loads(f.read())
        print("| Key | Value |")
        for k, v in obj.items():
            print(f"| {k} | {v} |\n")
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("invalid JSON")
    finally:
        if f is not None:
            f.close()
    return obj


if __name__ == "__main__":
    assert readingjson(
        "jsonfile.json") is not None, 'function returned None type'
