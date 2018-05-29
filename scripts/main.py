'''\
    main script
'''

from crawler import http_of
from lxml import etree
import stor

DATA_PATH = '../data/'

def fetch_cities():
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    context = etree.fromstring(http_of(url))
    res = context.xpath('//table[@class="wikitable sortable"]//tr/td[position()=2]//a/text()')
    return res

def fetch_populations():
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    context = etree.fromstring(http_of(url))
    res = context.xpath('//table[@class="wikitable sortable"]//tr/td[@rowspan="1"]/text()')
    return res

if __name__ == '__main__':
    cities = fetch_cities()[:-7]
    populations = fetch_populations()[:-14:2]
    box = stor.Box(DATA_PATH)
    box.put('cities', cities)
    box.put('populations', populations)
    print(len(cities))
    print(len(populations))
