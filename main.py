import re
import requests
from bs4 import BeautifulSoup



def menu():
    while True:
        print("Добро пожаловать в программу для поиска слов, состоящих из двух одинаковых частей\n")
        print("Выберите действие:\n(1) - поиск слов в пользовательском вводе\n"
              "(2) - поиск слов в файле по его пути\n"
              "(3) - поиск слов на странице по её url")
        try:
            option = int(input())
            options(option)
        except ValueError:
            print("Введите число от 1 до 3.\n")

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
        if (re.fullmatch(r'\b(\w{1,})\1\b', item)) is not None:
            result.append(item)
    if len(result) > 0:
        print(result,'\n')
    else:
        print('Нужных слов не найдено!\n')
    return result


def file_search(path):
    try:
        with open(path, 'r', encoding='UTF8') as file:
            text = file.read()
        if len(text) > 0:
            search(text)
        else:
            print("Файл пуст.\n")
    except FileNotFoundError:
        print("Ошибка: файл не найден.\n")
    except PermissionError:
        print("Ошибка: нет доступа к файлу.\n")
    except Exception as e:
        print(f"Не удалось открыть файл: {e}\n")


def url_search(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator=' ')
        text = ' '.join(text.split()).lower()
        search(text)
    except requests.exceptions.MissingSchema:
        print("Ошибка: некорректный URL.\n")
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения: сайт недоступен.\n")
    except requests.exceptions.Timeout:
        print("Ошибка: время ожидания истекло.\n")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ошибка: {e}\n")
    except Exception as e:
        print(f"Не удалось получить данные с URL: {e}\n")


if __name__ == '__main__':
    menu()