import requests
import selectorlib
from dependencies import send_mail
import time as t
import sqlite3 as sq
connection = sq.connect("datas.db")

urls = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extracts(source):
    x = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = x.extract(source)["tours"]
    return value


def write(content):
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM temps")
    # result = cursor.fetchall()

    # row = [i.strip() for i in content]
    row = tuple(content)
    cursor.execute(f"INSERT INTO temps VALUES (?,?)", row)
    connection.commit()


def read():
    x = open("data.txt", "r").readlines()
    return x


if __name__ == '__main__':
    while True:
        extracted = extracts(scrape(urls))
        # check = read()
        # print(check)
        if extracted != "No upcoming tours":
            write([t.strftime("%d%m%y"), extracted])
            # send_mail(str(extracted), "k.akashkumar@gmail.com")
