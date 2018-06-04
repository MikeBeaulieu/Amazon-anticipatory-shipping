'''\
    object permanent storage based on pickle
    box = stor.Box(path)
    box.put('simple_list', [0, 1, 2])
    simple_list = box.get('simple_list')
'''

import os
import pickle
import json

class Box(object):
    def __init__(self, path, token = None):
        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path if path[-1] == '/' else path + '/'

    def __fullpath(self, name, postfix) -> 'full path':
        return ''.join([self.path, name, '.', postfix])

    def put(self, name, data, force=False) -> 'self':
        outpath = self.__fullpath(name, 'pkl')
        if os.path.isfile(outpath):
            if not force:
                raise ValueError('data with same name already exist, use force=False to override')
            else:
                os.remove(outpath)
        with open(outpath, 'wb') as outfile:
            pickle.dump(data, outfile)
        return self

    def put_json(self, name, data_json, force=False) -> 'self':
        outpath = self.__fullpath(name, 'json')
        if os.path.isfile(outpath):
            if not force:
                raise ValueError('data with same name already exist, use force=False to override')
            else:
                os.remove(outpath)
        with open(outpath, 'w') as outfile:
            json.dump(data_json, outfile, ensure_ascii=False)

    def get(self, name) -> 'data':
        if os.path.isfile(self.__fullpath(name, 'pkl')):
            inpath = self.__fullpath(name, 'pkl')
        elif os.path.isfile(self.__fullpath(name, 'json')):
            inpath = self.__fullpath(name, 'json')
        else:
            raise ValueError('data {} not found'.format(name))
        if inpath[-3:] == 'pkl':
            with open(inpath, 'rb') as infile:
                data = pickle.load(infile)
        else:
            with open(inpath, 'r') as infile:
                data = json.load(infile)
        return data

def __debugStorage():
    lst = [0, 1, 2]
    json = {'one': 1, 'lst': lst}
    os.mkdir('./debug')
    box = Box('./debug')
    box.put('lst', lst, force=True)
    box.put_json('json', json, force=True)
    box.get('lst')
    box.get('json')

def main():
    __debugStorage()

if __name__ == '__main__':
    main()
