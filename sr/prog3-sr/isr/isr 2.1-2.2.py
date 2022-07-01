"""
Описание задачи:
    Построить таблицу истинности для:
    1.((C∨B)→B)∧(A∧ B)→B
    2.(A→B)∧A) ↔ A∧B
    3.¬(A∨¬C∧A)↔¬(¬A∧C→C)
"""
delimiter = "-"
space_symbol = " "
# Задача 1: ((C∨B)→B)∧(A∧B)→B
header = "* A *" + " B *" + " C *" + " ((C∨B)→B)∧(A∧B)→B"
table_width = len(header)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)
# Значения, которые принимает A
tuple_a = (False, False, False, False, True, True, True, True)
# Значения, которые принимает B
tuple_b = (False, False, True, True, False, False, True, True)
# Значения, которые принимает C
tuple_c = (False, True, False, True, False, True, False, True)
for i in range(8):
    inp_str1 = "* " + str(int(tuple_a[i])) + " * " + str(int(tuple_b[i]))
    inp_str2 = " * " + str(int(tuple_c[i])) + " *    "
    if tuple_c[i] or tuple_b[i] == 1 and tuple_b[i] == 0:  # ((C∨B)→B)
        result1 = 0
    else:
        result1 = 1
    result3 = result1 and (tuple_a[i] and tuple_b[i])  # ((C∨B)→B)∧(A∧B)
    # ((C∨B)→B)∧(A∧B)→B:
    if (result1 and (tuple_a[i] and tuple_b[i])) == 1 and tuple_b[i] == 0:
        result4 = 0
    else:
        result4 = 1
    print(inp_str1 + inp_str2 + "   "+str(result4))
# Задача 2: (A→B)∧A)↔A∧B
header = "* A *" + " B *"+" (A→B)∧A)↔A∧B"
table_width = len(header)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)
tuple_a = (False, False, True, True)  # Значения, которые принимает A
tuple_b = (False, True, False, True)  # Значения, которые принимает B
for i in range(4):
    inp_str1 = "* " + str(int(tuple_a[i])) + " * "
    inp_str2 = str(int(tuple_b[i])) + " *       "
    if tuple_a[i] == 1 and tuple_b[i] == 0:  # A→B
        result_impl = 0
    else:
        result_impl = 1
    result_left = result_impl and tuple_a[i]  # (A→B)∧A)
    result_right = tuple_a[i] and tuple_b[i]  # A∧B
    if result_left == result_right:  # (A→B)∧A)↔A∧B
        result = 1
    else:
        result = 0
    print(inp_str1 + inp_str2 + str(result))
# Задача 3: ¬(A∨¬C∧A)↔¬(¬A∧C→C)
header = "* A *" + " C *"+" ¬(A∨¬C∧A)↔¬(¬A∧C→C)"
table_width = len(header)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)
tuple_a = (False, False, True, True)  # Значения, которые принимает A
tuple_c = (False, True, False, True)  # Значения, которые принимает C
for i in range(4):
    inp_str1 = "* " + str(int(tuple_a[i]))
    inp_str2 = " * " + str(int(tuple_c[i])) + " *       "
    # ¬(A∨¬C∧A):
    result_left = not(not(tuple_c[i]) and tuple_a[i] or tuple_a[i])
    result_ac = not(tuple_a[i]) and tuple_c[i]  # ¬A∧C
    if result_ac == 1 and tuple_c[i] == 0:  # ¬A∧C→C
        result_right = 0
    else:
        result_right = 1
    if result_left == result_right:  # ¬(A∨¬C∧A)↔¬(¬A∧C→C)
        result = 0
    else:
        result = 1
    print(inp_str1 + inp_str2 + str(result))