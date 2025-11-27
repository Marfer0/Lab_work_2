def menu():
    while True:
        print("Добро пожаловать в программу для поиска слов, состоящих из двух одинаковых частей\n")
        print("Выберите действие:(1) - нахождение слов в пользовательском вводе\n"
              "(2) - нахождение слов по url\n"
              "(3) - нахождение слов в файле\n")
        option = int(input())
        return option

def options(option):
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        print("неизвестная команда, введите цифру от 1 до 3")
        menu()
