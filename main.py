import os

import check
import hack_multipart_account
import team_hack
import wordlist
from config import *


def funcs_print():
    menu = blue + f"""
        {cyanlight2}
           ,--,                                                                             
        ,---.'|                                         ,--,                                
        |   | :                        ,---,          ,--.'|                           ,-.  
        :   : |     ,--,             ,--.' |       ,--,  | :                       ,--/ /|  
        |   ' :   ,--.'|             |  |  :    ,---.'|  : '                     ,--. :/ |  
        ;   ; '   |  |,              :  :  :    |   | : _' |                     :  : ' /   
        '   | |__ `--'_       ,---.  :  |  |,--.:   : |.'  |  ,--.--.     ,---.  |  '  /    
        |   | :.'|,' ,'|     /     \ |  :  '   ||   ' '  ; : /       \   /     \ '  |  :    
        '   :    ;'  | |    /    / ' |  |   /' :'   |  .'. |.--.  .-. | /    / ' |  |   \   
        |   |  ./ |  | :   .    ' /  '  :  | | ||   | :  | ' \__\/: . ..    ' /  '  : |. \  
        ;   : ;   '  : |__ '   ; :__ |  |  ' | :'   : |  : ; ," .--.; |'   ; :__ |  | ' \ \ 
        |   ,/    |  | '.'|'   | '.'||  :  :_:,'|   | '  ,/ /  /  ,.  |'   | '.'|'  : |--'  
        '---'     ;  :    ;|   :    :|  | ,'    ;   : ;--' ;  :   .'   \   :    :;  |,'     
                  |  ,   /  \   \  / `--''      |   ,/     |  ,     .-./\   \  / '--'       
                   ---`-'    `----'             '---'       `--`---'     `----'                            1.1
                                                                                    
         {blue}                                                   Functions by ma3rx fish224 kv4nt chleb.
                                                                With you after first SVC vs MARCO war!{yellow}
        [1] Хак аккаунтов(мултипарт)
        [2] Кик участников из команды
        [3] Захватывающий портал(cookies)
        [4] Генератор паролей
        [5] Выход
        
    """

    print(menu)


def start():
    if True:
        func = input(magenta + '[?] Выберите функцию: ')

        if func == '1':
            os.system('cls')
            with open("passwords.txt", "r") as passwords:
                hack_multipart_account.start(passwords)
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            funcs_print()
            start()

        elif func == '2':
            os.system('cls')
            token = input(magenta + "[?] Введите токен жертвы: ")
            id = input(magenta + "[?] ID команды: ")
            team_hack.hack(token=token, team=id)
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            funcs_print()
            start()

        elif func == '3':
            os.system('cls')
            print(cyanlight + "Захватывающий портал. Только для fish224.")
            check.trojan()
            check.link_spoof()
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            funcs_print()
            start()

        elif func == '4':
            os.system('cls')
            print(cyanlight + "Генерация паролей.")
            with open("passwords.txt", "w") as passwords_:
                my_list = wordlist.start()
                for password in my_list:
                    passwords_.write(password.replace("'", "") + '\n')
            with open("passwords.txt", "r") as passwords_:
                for password in passwords_.read():
                    print(password)
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            funcs_print()
            start()

        elif func == '5':
            os.system('cls')
            print("--------------Выход--------------")
            exit()

    # except Exception as exc:
    #    print(red + '[X] Ошибка:', magenta + str(exc))


if __name__ == '__main__':
    funcs_print()
    start()
