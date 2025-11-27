import re
import requests
from bs4 import BeautifulSoup



def menu():
    while True:
        print("Добро пожаловать в программу для поиска слов, состоящих из двух одинаковых частей\n")
        print("Выберите действие:\n(1) - поиск слов в пользовательском вводе\n"
              "(2) - поиск слов в файле по его пути\n"
              "(3) - поиск слов на странице по её url")
        option = int(input())
        options(option)

def options(option):
    if option == 1:
        print("Введите любой текст:\n")
        inp = input()
        search(inp)
    elif option == 2:
        print("Введите путь к файлу для поиска:\n")
        path = input()
        file_search(path)
    elif option == 3:
        print("Введите ссылку на страницу для поиска:\n")
        url = input()
        url_search(url)
    elif option not in range(1,4):
        print("неизвестная команда, введите цифру от 1 до 3\n")
        menu()

def search(string):
    result = []
    string = string.lower()
    string = re.split(r'[,\s.!?;()]+', string)
    for item in string:
        if (re.fullmatch(r'\b(\w{2,})\1\b', item)) is not None:
            result.append(item)
    print(result,'\n')

def file_search(path):
    file_path = path
    with open(file_path, 'r', encoding='UTF8') as file:
            text = file.read()
    if len(text) > 0:
        print(text,'\n')
        search(text)
    else:
        print("Файл пуст или не может быть открыт.\n")


def url_search(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator=' ')
    text = ' '.join(text.split()).lower()
    search(text)

menu()