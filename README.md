
# Amazon's Anticipatory Shipping
Data and scripts for research on Amazon's Anticipatory Shipping in U.S.

## Environment

 - python >= 3.6.5
 - pip == 10.0.1
 - virtualenv == 16.0.0
 - requirements.txt
## Usage

 - /data/*: all data in both json and csv format
 - /images/*: all related images
 - /scripts/*:
	 - crawlers.py: Crawling package based on default urllib
	 - driver.py: Frontend driver for extracting shipping period based on Selenium
	 - stor.py: Python object permanent storage based on pickle. Support both json and csv format
	 - to_csv.py: Script to parse data to csv
	 - zipcode.py: Script to fetch population age distributation in America, based on official API (Credit to Census Bureau)
	 - random_token.py: Script to generate 16-based random token. (for username and password)
	 - goods.py: Script to crawl all goods in one catefory.
	 - driver.py: Web driver to fetch all goods' shipping period
