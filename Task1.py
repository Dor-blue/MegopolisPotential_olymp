import csv

with open('history_mirror.csv', 'r', encoding='utf-8') as data:
    data = list(map(lambda x: x.strip().split(','), data.readlines()))
    #открываем CSV файл и разбиваем каждую строку по запятым

mirror_error = [] #Список со строками таблицы, удовлетворяющими учловию задачи
for el in data:
    if el[2] == 'Победа над смертью':
        mirror_error.append([el[0], el[1]])
        #Если элемент удовлетворяет условию поиска, дописываем его в список

print(f'Сообщение было зафиксировано: {mirror_error[0][0]} у пользователя {mirror_error[0][1].split()[0] + ' ' + mirror_error[0][1].split()[1][0] + '. ' + mirror_error[0][1].split()[2][0] + '.'}')

with open('mirror_error.csv', 'w', encoding='utf-8') as file:
    title = [['date', 'username']]
    full = title + mirror_error #Полный список, с заголовком, подготовленный к выводу
    writer = csv.writer(file)
    writer.writerows(full)
    #Записываем полученный список в mirror_error.csv