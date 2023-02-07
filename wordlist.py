import sys

from config import *


def exit():
    sys.exit()


def program():
    id = input(magenta + "\n[?] Введите айди листа: ")
    amount = input(magenta + "\n[?] Введите количество паролей: ")
    amount = int(amount)

    print(yellow + "\n\t\tПодождите, это займет несколько секунд- - - - - -")
    file = open("passwords.txt", "a+")
    file.write(id + id + "\n")
    for i in range(amount):
        r_num = random.randint(1000, 9999)
        r_num = str(r_num)
        file = open("passwords.txt", "a+")
        file.write(id + r_num + "\n")
        file.write(r_num + r_num + "\n")

        file.write(r_num + id + "\n")

    print(green + "\n[+] Сохранено в файл: passswords.txt")


def view():
    file = open("passwords.txt", "r")
    read = file.read()
    print(ran + "\n\t\tВот, что найдено:: \n")

    print(all_col[2 % 6] + read)


def start():
    cont = " "
    while cont != "n" and "no":
        print(
            Fore.LIGHTYELLOW_EX + "\n\t\t[1] Сгенерировать пароли\n\t\t[2] Посмотреть сгенерированные пароли\n\t\t[3] Выход\n ")

        choice = input(magenta + "[?} Выберите функцию: ")
        if choice == "1":
            program()

        elif choice == "2":
            view()
        elif choice == "3":
            exit()

        else:
            print(magenta + "\n[?] У тебя вместо мозгов коробка?")
            exit()
        cont = input(magenta + "\n[?] Хотите продолжить? [y/n]:")

        if cont == "y":
            os.system('cls')
