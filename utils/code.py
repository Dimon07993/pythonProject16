import json
import datetime


def load_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        return json.load(f)

def sort_data(data):
    '''сортировка по state == EXECUTED'''
    sort_operations = [operation for operation in data if 'state' in operation and operation['state'] == 'EXECUTED']
    return sorted(sort_operations[:5], key=lambda x: x['date'])


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
    list1 = []
    d = load_file(data)
    d = sort_data(d)
    for i in d:
        date = format_date(i['date'])
        if 'from' in i:
            from_card = secret_card(i['from'])
            to_card = secret_card(i['to'])
            list1.append({"date" : date, "from" : from_card, "to" : to_card, "operationAmount" : i['operationAmount'], "descr" : i['description']})
        else:
            from_card = secret_card(i['to'])
            list1.append({"date" : date, "from" : from_card, "operationAmount" : i['operationAmount'],"descr" : i['description']})

    return list1

#print(print_data('..\data\operations.json'))

