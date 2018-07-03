'''\
    fetch all major living area with population in America using info from wikipedia
'''

from crawler import page_of
from lxml import etree
import stor

DATA_PATH = '../data/'

def fetch_cities():
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    context = etree.fromstring(page_of(url))
    res = context.xpath('//table[@class="wikitable sortable"]//tr/td[position()=2]//a/text()')
    return res

def fetch_populations():
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    context = etree.fromstring(page_of(url))
    res = context.xpath('//table[@class="wikitable sortable"]//tr/td[@rowspan="1"]/text()')
    return res

if __name__ == '__main__':
    pass
