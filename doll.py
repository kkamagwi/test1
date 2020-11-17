import requests
from bs4 import BeautifulSoup
import datetime


def dol_parser(url):

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    table = soup.find('td', {'class': 'exrate'})
    return table.text


dollar = dol_parser('https://www.nbkr.kg/')
d = datetime.datetime.now()
current = "В {} доллар {}".format(str(d), str(dollar))

#В python метод write служит для записи строки в файл:
# "w" - перезапись "a" = дозапись

f = open("dollar.txt", "w") 

f.write (current)
f.close()
