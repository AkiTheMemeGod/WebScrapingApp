import requests
import selectorlib
from send_email import send_mail

urls = "https://programmer100.pythonanywhere.com/tours/"
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
    open("data.txt", "a").write(content + "\n")


def read():
    return open("data.txt", "r").read()


if __name__ == '__main__':

    extracted = extracts(scrape(urls))
    check = read()
    if extracted != "No upcoming tours":
        if extracted not in check:
            write(extracted)
            send_mail(str(extracted), "k.akashkumar@gmail.com")
