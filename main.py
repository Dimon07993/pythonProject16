from utils.code import print_data

list_corret_data = print_data('data/operations.json')

for corret_data in list_corret_data:
    if 'to' in corret_data:
        print(f'{corret_data["date"]} {corret_data["descr"]}')
        print(f'{corret_data["from"]} -> {corret_data["to"]}')
        print(f'{corret_data["operationAmount"]["amount"]} {corret_data["operationAmount"]["currency"]["name"]}' + '\n')
    else:
        print(f'{corret_data["date"]} {corret_data["descr"]}')
        print(f'{corret_data["from"]}')
        print(f'{corret_data["operationAmount"]["amount"]} {corret_data["operationAmount"]["currency"]["name"]}' + '\n')
