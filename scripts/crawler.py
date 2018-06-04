'''\
    Crawling package
'''
from urllib import request
import time

def page_of(uri):
    '''\
        returns context of given uri
    '''
    req = request.Request(uri, data = None, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537\
                        .36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    })
    with request.urlopen(req, timeout = 10) as res:
        context = res.read().decode('utf-8')
    return context

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    print(page_of(url))
