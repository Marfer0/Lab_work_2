import re
import requests
from bs4 import BeautifulSoup



def menu():
    while True:
        print("Добро пожаловать в программу для поиска слов, состоящих из двух одинаковых частей\n")
        print("Выберите действие:\n(1) - нахождение слов в пользовательском вводе\n"
              "(2) - нахождение слов в файле по его пути\n")
        option = int(input())
        options(option)

def options(option):
    if option == 1:
        inp = input()
        search(inp)
    elif option == 2:
        inp = input()
        file_search(inp)
    elif option not in range(1,3):
        print("неизвестная команда, введите цифру от 1 до 3")
        menu()

def search(string):
    result = []
    string = string.lower()
    string = re.split(r'[,\s.!?;]+', string)
    for item in string:
        if (re.fullmatch(r'\b(\w{2,})\1\b', item)) is not None:
            result.append(item)
    print(result,'\n')

def file_search(path):
    result = []
    file_path = path
    with open(file_path, 'r', encoding='UTF8') as file:
            text = file.read()
    if len(text) > 0:
        print(text,'\n')
        search(text)
    else:
        print("Файл пуст или не может быть открыт.\n")
menu()