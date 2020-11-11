import requests
from bs4 import BeautifulSoup
import re


def phone_parser(url):

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")
    body = soup.find('body').text

    reg_expression = r'\d{3}\D{2}\d{3}\D{2}\d{3}\D\d{3}'

    return (re.findall(reg_expression, body))

