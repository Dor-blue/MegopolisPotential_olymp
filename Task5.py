import csv

def hash(s): #Функция хеширует ФИО без пробелов, т.к. это не обозначено в условии
    summ = 0
    s = ''.join(s.split())
    for i in range(len(s)):
        a = ord(s[i])-ord('А')
        summ += a*67**i % (10**9+9)
    return(summ)


with open('history_mirror.csv', 'r', encoding='utf-8') as data:
    data = list(map(lambda x: x.strip().split(','), data.readlines()))[1:]
    #открываем CSV файл и разбиваем каждую строку по запятым

hashed = [] #список строк с хеш-суммами


for el in data:
    hashed.append([hash(el[2]), el[0], el[1], el[2]])#добавляем в строки с хеш-суммами

with open('users_with_hash.csv', 'w', encoding='utf-8') as file:
    title = [['ID', 'date', 'username', 'verdict']]
    full = title + hashed #Полный список, с заголовком, подготовленный к выводу
    writer = csv.writer(file)
    writer.writerows(full)
    #Записываем полученный список в mirror_error.csv

