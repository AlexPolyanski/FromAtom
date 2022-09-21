import webbrowser
import json
import time
from urllib.request import urlopen

print("Давайте найдем старый сайт.")
# site = input("Введите URL сайта: ")
# era = input("Введите дату в формате ГГГГ.ММ.ДД: ")
url = "http://archive.org"
# /wayback/available?url=%s&timestamp=%s" % (site,era)
print(url)
path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
webbrowser.register('Fox', None, webbrowser.BackgroundBrowser(path))
webbrowser.get(using='Fox').open_new_tab(url)
# response = urlopen(url)
# contents = response.read()
# text = contents.decode("utf-8")
# print(str(response.getcode()))
# data = json.loads(text)
time.sleep(10)
# try:
#    old_site = data["archived_snapshots"]["closest"]["url"]
#    print("Найдена эта копия: ", old_site)
#    print("Сайт сейчас запустится в браузере...")
#    webbrowser.open(old_site)
# except Exception:
#    print("Такого сайта не существует", site)
