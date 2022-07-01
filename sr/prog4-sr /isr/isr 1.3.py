# Дополнение программы для считывания данных с использованием менеджера контекстов и реализации расширенного синтаксиса для обработки исключений.

import json


def readingjson(file):
    obj = None
    try:
        with open(file, "rt") as f:
          obj = json.loads(f.read())
          print("| Key | Value |")
          for k, v in obj.items():
            print(f"| {k} | {v}\t|\n")
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("invalid JSON")
    return obj


if __name__ == "__main__":
    assert readingjson(
        "jsonfile.json") is not None, 'function returned None type'
