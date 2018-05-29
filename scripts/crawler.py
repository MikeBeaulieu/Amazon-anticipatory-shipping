'''\
    Crawling package
'''

from urllib import request

def http_of(url, encode='utf-8'):
    with request.urlopen(url) as res:
        context = res.read()
        return context.decode(encode)

def debug():
    url = 'https://en.wikipedia.org/wiki/List_of_metropolitan_statistical_areas'
    print(http_of(url))

if __name__ == '__main__':
    debug()
