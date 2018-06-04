from crawler import page_of
from pyquery import PyQuery as pq
from stor import Box

DATA_PATH = '../data/'

def shoe_pages(index):
    return 'https://www.amazon.com/s/ref=sr_pg_2?rh=n%3A7141123011%2Cn%3A7586146011%2Ck%3Ashoes&page={}&keywords=shoes&ie=UTF8&qid=1527718963'.format(index)

def book_pages(index):
    return 'https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk_r?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=6GXV26VEE07RR9SGHB29&pf_rd_r=6GXV26VEE07RR9SGHB29&pf_rd_t=101&pf_rd_p=b8c0a303-a08e-4b0b-bd49-040811fd7080&pf_rd_p=b8c0a303-a08e-4b0b-bd49-040811fd7080&pf_rd_i=283155#{}'.format(index)

def electronics_pages(index):
    pass

def household_pages(index):
    pass

def food_pages(index):
    pass

def fetch_shoes():
    links = []
    for index in range(1, 3):
        page = page_of(shoe_pages(index))
        ele = pq(page)
        for i in range(0, 48):
            link = ele('#result_{} div div div a'.format(i + (index - 1) * 48)).attr('href')
            print(link)
            links.append(link)
    for i in range(0, len(links)):
        if links[i] != None and links[i][:5] != 'https':
            links[i] = 'https://www.amazon.com' + links[i]
    links = links[:50]
    print(len(links))

    # box = Box(DATA_PATH)
    # box.put('shoe_list', links, force=True)
    # box.put_json('shoe_list', links, force=True)
    return links

def fetch_books():
    links = []
    for index in range(1, 4):
        select = []
        while select == []:
            page = page_of(book_pages(index))
            ele = pq(page)
            select = ele('#zg_centerListWrapper div div.zg_itemWrapper div.a-section a.a-link-normal').not_('a.a-text-normal')
        for i in range(0, len(select), 3):
            links.append('https://www.amazon.com' + pq(select[i]).attr('href'))
    links = links[:50]
    # box = Box(DATA_PATH)
    # box.put('book_list', links)
    # box.put_json('book_list', links)
    return links

if __name__ == '__main__':
    # fetch_shoes()
    # fetch_books()
