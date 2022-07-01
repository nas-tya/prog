import json
file = open("res.csv", "w")
with open("data.json", "r") as read_file:
    data = json.load(read_file)
for strin in data:
    res_str = ''
    for i in strin.values():
        res_str += "{0};".format(i)
    file.write(res_str[:len(res_str) - 1] + "\n")
file.close()