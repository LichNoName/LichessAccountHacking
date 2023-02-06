import json
import requests


def decode_month(month):
    month = month.lower()
    if (month.isnumeric()):
        month = int(month)
        if (month < 1): return
        if (month > 12): return
        return str(month)
    res = ''
    #    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    try:
        res = str(months.index(month) + 1)
    except:
        for i in months:
            if (month == i[0] + i[1] + i[2]): res = str(months.index(i) + 1)

    if (len(res) == 1): res = '0' + res
    return res


def method1(info):
    info = info.split(" ")
    for i in range(0, len(info) - 2):
        day = info[i]
        month = info[i + 1]
        year = info[i + 2]
        if (not day.isnumeric()): continue
        try:
            if (int(day) <= 0) or (int(day) >= 32): continue
            if (not year.isnumeric()): continue
            if ((int(year) <= 1900) and (int(year) > 99)) or (int(year) >= 2018): continue
            print(day, month, year)
            if (not decode_month(month)): continue
        except:
            continue
        if (len(year) == 2):
            if (int(year) < 22):
                year = '20' + year
            else:
                year = '19' + year
        return day + decode_month(month) + year
    return ''


def method2(info):
    info = info.split(" ")
    for i in range(0, len(info)):
        k = info[i].split(".")
        if (len(k) == 3):
            day = k[0]
            month = k[1]
            year = k[2].split(".")[0].split(",")[0]
            if (not day.isnumeric()): continue
            if (int(day) <= 0) or (int(day) >= 32): continue
            if (not year.isnumeric()): continue
            if ((int(year) <= 1900) and (int(year) > 99)) or (int(year) >= 2018): continue
            print(day, month, year)
            if (int(month) <= 0) or (int(month) > 12): continue
            if (len(year) == 2):
                if (int(year) < 22):
                    year = '20' + year
                else:
                    year = '19' + year
            return day + month + year
    return ''


def get_birthday(user):
    try:
        r = requests.get("https://lichess.org/api/user/" + user)
        if (r.status_code != 200): return
        info = json.loads(r.text).get("profile").get("bio")
    except:
        return
    if (not info): return
    return method1(info) + method2(info)


def get_year(user):
    try:
        r = requests.get("https://lichess.org/api/user/" + user)
        if (r.status_code != 200): return
        info = json.loads(r.text).get("profile").get("bio")
    except:
        return
    if (not info): return
    info = info.split(" ")
    for i in info:
        if (i.isnumeric()) and (int(i) > 1950) and (int(i) < 2022): return i
    return


def get_name(user):
    try:
        r = requests.get("https://lichess.org/api/user/" + user)
        if (r.status_code != 200): return r.status_code
        info = json.loads(r.text).get("profile").get("lastName") + json.loads(r.text).get("profile").get("firstName")
    except:
        return
    return info
