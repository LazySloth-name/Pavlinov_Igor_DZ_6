# Задание 1 к уроку 6
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>
def parser_string(str_in):
    if str_in.find(' - - ') > 0:
        address = str_in.split(' - - ')[0]
    else:
        address = ''
    if str_in.find(' - - ') > 0 and str_in.find('] "') > 0:
        request_type = str_in.split(' - - ')[1].split('] "')[1].split(' /')[0]
    else:
        request_type = ''
    if str_in.find(' - - ') > 0 and str_in.find('] "') > 0:
        requested_resource = str_in.split(' - - ')[1].split('] "')[1].split(' ')[1]
    else:
        requested_resource = ''
    return address, request_type, requested_resource


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


result = []
log_file = csv_reader('nginx_logs.txt')
for file_line in log_file:
    result.append(parser_string(file_line))

for i in range(20):
    print(result[i])