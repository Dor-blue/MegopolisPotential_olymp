import csv

with open('history_mirror.csv', 'r', encoding='utf-8') as data:
    data = list(map(lambda x: x.strip().split(','), data.readlines()))[1:]
    #открываем CSV файл и разбиваем каждую строку по запятым


years = {} #Создаем словарь с годами, каждому из которых будет соответствовать список запросов

for el in data:
    if el[0].split('-')[0] in years:
        years[el[0].split('-')[0]].append(el)
    else:
        years[el[0].split('-')[0]] = [el]
    #Добавляем запросы в словарь по годам

for el in years:
    print(f'В {el} году зеркало было использовано {len(years[el])}.')
    #Выводим информацию по каждому году