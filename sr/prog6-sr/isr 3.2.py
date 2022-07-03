from easygui import *
import numpy as np

msg = "Решение СЛАУ 3х3"
title = "Решение квадратного уравнения"
field_names = ["a11, a12, a13", "a21, a22, a23",
               "a31, a32, a33", "b1, b2, b3"]
field_values = []
field_values = multenterbox(msg, title, field_names, ["", "", "", ""])

while 1:
    if field_values is None:
        break
    errmsg = ""
    for i in range(len(field_names)):
        if field_values[i].strip() == "":
            errmsg = errmsg + ('"%s" необходимо заполнить.\n\n' % field_names[i])
    if errmsg == "":
        break
    field_values = multenterbox(errmsg, title, field_names, field_values)

A = [[], [], [], []]
i = -1

for el in field_values:
    i += 1
    line = el.split(",")
    line = [A[i].append(float(elem.strip())) for elem in line]

B = A.pop()
A = np.array(A)
B = np.array(B)

X = np.linalg.solve(A, B)
print("X = ", X)
result = "x1 = " + str(round(X[0], 2)) + "; x2 = " + \
         str(round(X[1], 2)) + "; x3 = " + str(round(X[2], 2))
msgbox(str(result), "Результат вычислений")
