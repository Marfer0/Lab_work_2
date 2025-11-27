import re


def menu():
    while True:
        print("Добро пожаловать в программу для поиска слов, состоящих из двух одинаковых частей\n")
        print("Выберите действие:\n(1) - нахождение слов в пользовательском вводе\n"
              "(2) - нахождение слов по url\n"
              "(3) - нахождение слов в файле\n")
        option = int(input())
        options(option)

def options(option):
    if option == 1:
        inp = input()
        search(inp)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option not in range(1,4):
        print("неизвестная команда, введите цифру от 1 до 3")
        menu()

def search(string):
    result = []
    for item in string.lower().split():
        if (re.fullmatch(r'\b(\w{2,})\1\b', item)) is not None:
            result.append(item)
    print(result,'\n')
menu()