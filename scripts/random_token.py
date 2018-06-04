'''\
    generate random 16 base token
'''

import random

def token(size = 8):
    choices = list('0123456789ABCDEF')
    res = random.choices(choices, k=size)
    return ''.join(res)

def debug():
    print(token())

if __name__ == '__main__':
    debug()
