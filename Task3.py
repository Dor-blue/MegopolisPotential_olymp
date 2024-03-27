import csv

with open('history_mirror.csv', 'r', encoding='utf-8') as data:
    data = list(map(lambda x: x.strip().split(','), data.readlines()))
    #открываем CSV файл и разбиваем каждую строку по запятым

user_input = input()
#Пользовательский ввод

while user_input != 'stop':
    find = []
    for el in data:
        if user_input in el[1]:
            find.append(f'Предсказание для {el[1].split()[0] + ' ' + el[1].split()[1][0] + '. ' + el[1].split()[2][0] + '.'} - {el[2]}')
            #Перебираем весь список с предсказаниями и находим все поля, соответствующие пользоватеьскому вводу. Добавляем их в список

    if find: #Если список не пустой, выводим найденное, в противном случае выводим "Вас не нашлось в записях"
        print(*find, sep='\n')
    else:
        print('Вас не нашлось в записях')

    user_input = input() #Вновь считываем ввод пользователя

