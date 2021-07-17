# Задание 6 к уроку 6


# *show sales
from sys import argv


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as _file:
        for line in _file:
            yield line


def show_sales(*args):
    sales_f = csv_reader('bakery.csv')
    if len(args) > 0:
        for i in range(int(args[0]) - 1):
            next(sales_f)
    kol_lines_show = None
    if len(args) > 1:
        kol_lines_show = int(args[1]) - int(args[0])
    for line in sales_f:
        print(line.strip())
        if kol_lines_show is not None:
            if kol_lines_show:
                kol_lines_show -= 1
            else:
                break


if __name__ == '__main__':
    program, *args = argv
    show_sales(*args)
