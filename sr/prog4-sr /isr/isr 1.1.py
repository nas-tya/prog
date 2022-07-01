# Разработать программу с реализацией функции для считывания json-данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except)

import json

def readingjson(file="jsonfile.json"):
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