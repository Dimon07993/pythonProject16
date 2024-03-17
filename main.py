from utils.code import print_data

s1 = print_data('data/operations.json')

for i in s1:
    print(i)
    #if 'to' in i:
    #    print(f'{i["date"]} {i["descr"]}')
    #    print(f'{i["from"]} -> {i["to"]}')
    #    print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}' + '\n')
    #else:
    #    print(f'{i["date"]} {i["descr"]}')
    #    print(f'{i["from"]}')
    #    print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}' + '\n')
#