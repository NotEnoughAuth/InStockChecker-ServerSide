import requests
from bs4 import BeautifulSoup
import lxml

def checkinstock(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    # return adafruit(soup, page)
    return companies[url.split('.')[1]](soup, page)


def adafruit(soup, page):
    avail = soup.find(itemprop="availability")
    try:
        return avail.text.lower().__contains__("in stock")
    except:
        print(page)


companies = {'adafruit': adafruit}
