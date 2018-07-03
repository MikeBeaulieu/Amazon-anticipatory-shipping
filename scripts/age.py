'''\
    fetch population age distributation in America, based on official API
'''

from urllib import request
import json
import stor

DATA_PATH = '../data/'

def api_of(key):
    return 'http://api.census.gov/data/2010/sf1?get={},NAME&for=state:*'.format(key)

def fetch_data():
    data = {}
    for i in range(1, 50):
        key = 'P012000{}'.format(i) if i <= 9 else 'P01200{}'.format(i)
        api = api_of(key)
        print(i)
        with request.urlopen(api, timeout = 10) as res:
            context = res.read().decode('utf-8')
            data_each = json.loads(context)
            data[i] = data_each
    box = stor.Box(DATA_PATH)
    box.put('population_raw', data, force=True)

def format_data():
    box = stor.Box(DATA_PATH)
    raw = box.get('population_raw')
    data = {}
    for i in range(1, 50):
        if i == 1:
            skip_first = False
            for lst in raw[i]:
                if not skip_first:
                    skip_first = True
                    continue
                data[lst[1]] = [int(lst[0])]
        else:
            skip_first = False
            for lst in raw[i]:
                if not skip_first:
                    skip_first = True
                    continue
                data[lst[1]].append(int(lst[0]))

    data_format = []
    data_format.append(['State', 'Total', '<=4', '5-9', '10-17', '18-21', '22-49', '>=50'])
    for key in data:
        lst = data[key]
        data_format.append([key, lst[0], sum(lst[2:3] + lst[26:27]),
                                         sum(lst[3:4] + lst[27:28]),
                                         sum(lst[4:6] + lst[28:30]),
                                         sum(lst[6:9] + lst[30:33]),
                                         sum(lst[9:15] + lst[33:39]),
                                         sum(lst[15:25] + lst[39:49])])
    box.put('population', data_format, force=True)

if __name__ == '__main__':
    pass
