import json
from itertools import zip_longest
# Задание 3 для урока 6
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.Если в файле, хранящем
# данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.Если наоборот — выходим из скрипта
# с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as _file:
        for line in _file:
            yield line


result = {}
for u, h in zip_longest(csv_reader('users.csv'), csv_reader('hobby.csv'), fillvalue=None):
    if u is None:
        break
    if h is not None:
        h = h.strip()
    result[u.strip()] = h

print(result)

with open('nums.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(result))