'''\
    generate random 16 base token, used for username
'''

import unittest
import random

def token(size=8):
    choices = list('0123456789ABCDEF')
    res = random.choices(choices, k=size)
    return ''.join(res)

class TestPage(unittest.TestCase):

    def test_token(self):
        ''' true if token != None '''
        self.assertIsNotNone(token())

if __name__ == '__main__':
    unittest.main()
