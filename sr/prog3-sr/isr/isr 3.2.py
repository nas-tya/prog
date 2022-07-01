input_str = input("Enter source string:\n")
searchable_str = input("Enter the substring:\n")
try:
    print("Your substring beginning from letter number : {0}".format(input_str.index(searchable_str) + 1))
except ValueError:
    print('I can`t find this substring!')
