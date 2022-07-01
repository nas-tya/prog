import json
import csv


def writingjson(file):
    data = input('input your data, please: ') 
    try:
      with open(file, 'at') as f:
        f.write(json.dumps(json.loads(data)))
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("invalid JSON")


def writingcsv(file):
    data = input('input your data, please: ') 
    try:
      with open(file, 'at') as f:
        csv.writer(f).writerow([data])
    except FileNotFoundError:
        print("file not found")



if __name__ == "__main__":
    frmt = input("what format do you want to write? ")
    writingcsv("vsr1.csv") if frmt == "csv" else writingjson("vsr1.json")
