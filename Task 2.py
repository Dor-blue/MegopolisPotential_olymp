import csv

with open('history_mirror.csv', 'r', encoding='utf-8') as data:
    data = list(map(lambda x: x.strip().split(','), data.readlines()))[1:]
    #открываем CSV файл и разбиваем каждую строку по запятым

data = sorted(data, key= lambda x: x[2]) #Сортируем список

for i in range(4):
    print(f'{data[i][0]} - {data[i][1]} - {data[i][2]} ') #выводим первые 4 записи