# Задание *4 к уроку 6
# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно
# создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as _file:
        for line in _file:
            yield line


with open('users_hobby.txt', 'w+', encoding='utf-8') as f:
    for u, h in zip(csv_reader('users.csv'), csv_reader('hobby.csv')):
        f.write(f'{u.strip()}: {h.strip()}\n')