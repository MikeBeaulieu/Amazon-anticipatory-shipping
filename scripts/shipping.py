import time
from selenium import webdriver
from stor import Box

DATA_PATH = '../data/'

def fetch_each(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element_by_css_selector('#nav-link-accountList').click()
        driver.find_element_by_name('email').clear()
        driver.find_element_by_name('email').send_keys('BD7C05A8@mail.com')
        driver.find_element_by_id('continue').click()
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('HLW1qu@n')
        driver.find_element_by_id('signInSubmit').click()
        driver.find_element_by_css_selector('#tmmSwatches ul li:nth-child(2) a').click()
        try:
            driver.find_element_by_id('add-to-cart-button-pf').click()
        except Exception:
            driver.find_element_by_id('add-to-cart-button').click()
        driver.find_element_by_id('hlb-ptc-btn-native').click()
        driver.find_element_by_css_selector('#address-book-entry-0 div.ship-to-this-address span a').click()
        date = driver.find_element_by_css_selector('div.a-box.selected div.description span span').text
        for i in range(len(date) - 1, -1, -1):
            if date[i] == ',':
                date = date[i+2:]
                break
        cur = time.strptime('May 31', '%B %d')[7]
        date = time.strptime(date, '%B %d')[7]
        days = date - cur
        driver.find_element_by_link_text('Change quantities or delete').click()
        driver.find_element_by_css_selector('table.typeitempricegrid tr:nth-child(3) td:nth-child(2) input').click()
    finally:
        driver.close()
    return days

if __name__ == '__main__':
    box = Box(DATA_PATH)
    book_list = box.get('book_list')
    # shoe_list = box.get('shoe_list')
    # book_list = book_list[:5]
    shipment = {}
    for url in book_list:
        try:
            shipment[url] = fetch_each(url)
        except Exception:
            continue
    box.put_json('book_shipment', shipment, force=True)
    # shipment = {}
    # for url in shoe_list:
    #     if url != None:
    #         try:
    #             shipment[url] = fetch_each(url)
    #         except Exception:
    #             continue
    # box.put_json('shoe_shipment', shipment, force=True)
