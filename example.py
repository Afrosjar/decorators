from decor1 import logger
import os
from datetime import datetime
from functools import wraps

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }
@logger
def get_name(doc_number):
    i = doc_number
    for a in documents:
        if a["number"] == i:
            i = a["name"]
            return(i)
    return("Документ не найден")
@logger
def get_directory(doc_number):
    a = doc_number # Запрашиваем номер документа у пользователя
    for keys, value in directories.items(): # Проходим по словарю и распаковываем сразу в две переменные. В первой будет ключ, а в второй - значение ключа
        if a in value : # Проверяем вхождение номера документа в значении ключа
            return keys #
    return ("Полки с таким документом не найдено") #
@logger
def add(document_type, number, name, shelf_number):
    a = document_type
    b = number
    c = name
    x = str(shelf_number) #Запросили номер полки
    if x not in directories: #Проверяем нет ли номера полки в директории
        return("Введите верный номер полки")
    res = {"type":a, "number":b, "name":c} #Формируем словарь
    # print(res)
    documents.append(res) #Добавляем словарь в каталог
    directories[x].append(b) #Добавляем номер на полку
    # return(directories,documents)

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))