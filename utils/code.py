import json
import datetime


def load_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        return json.load(f)

def sort_data(data):
    '''сортировка по state == EXECUTED'''
    sort_operations = [operation for operation in data if 'state' in operation and operation['state'] == 'EXECUTED']

    return sorted(sort_operations, key=lambda x: x['date'])



def format_date(date):
    '''форматирование даты'''
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


def secret_card(number):
    '''шифровка карты'''
    number = number.split()
    card_number = number.pop()
    card_name = ' '.join(number)
    if card_name.lower() == 'счет':
        number = f'**{card_number[-4:]}'
    else:
        number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    return f'{card_name} {number}'



def print_data(data):
    list_corret_data = []
    sorted_list = sort_data(load_file(data))[-5:]
    for sort_list in sorted_list:
        date = format_date(sort_list['date'])
        if 'from' in sort_list:
            from_card = secret_card(sort_list['from'])
            to_card = secret_card(sort_list['to'])
            list_corret_data.append({"date" : date, "from" : from_card, "to" : to_card, "operationAmount" : sort_list['operationAmount'], "descr" : sort_list['description']})
        else:
            from_card = secret_card(sort_list['to'])
            list_corret_data.append({"date" : date, "from" : from_card, "operationAmount" : sort_list['operationAmount'],"descr" : sort_list['description']})

    return list_corret_data
