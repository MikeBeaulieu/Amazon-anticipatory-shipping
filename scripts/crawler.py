'''\
    Crawling package based on default urllib
'''

import unittest
from urllib import request

def page_of(uri):
    '''\
        returns context of given uri
    '''
    req = request.Request(uri, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537\
                        .36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    })
    with request.urlopen(req, timeout=10) as res:
        context = res.read().decode('utf-8')
    return context

class TestPage(unittest.TestCase):

    def test_page_of(self):
        ''' true if context != None '''
        test_url = 'https://www.nginx.com/'
        self.assertIsNotNone(page_of(test_url))

if __name__ == '__main__':
    unittest.main()
