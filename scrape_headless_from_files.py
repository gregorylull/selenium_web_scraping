# to run:
# python scrape_headless_from_files.py urls.csv 0 12
#
# OR to run in parallel you can open up multiple terminal windows
# and execute the following commands in each window to split up your data.
#
# python scrape_headless_from_files.py urls.csv 0 4
# python scrape_headless_from_files.py urls.csv 4 8
# python scrape_headless_from_files.py urls.csv 8 12
#
# add 'time' in the very front to time how long the script takes, e.g.:
# time python scrape_headless_from_files.py urls.csv 8 12

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import chromedriver_binary
import pandas as pd

filename = int(sys.argv[1])
index_start = int(sys.argv[2])
index_stop = int(sys.argv[3])

with open(filename, 'r') as readfile:
    df = pd.read_csv(readfile, delim_whitespace=True)

# go headless
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

# this is just setting the default viewport size, width=1200, height=1200. 
chrome_options.add_argument("--window-size=1200,1200") 

# instantiating the driver only once, to reduce startup time.
driver = webdriver.Chrome(options=chrome_options)

def scrape_page(url, page_index):
    driver.get(url)
    time.sleep(1)

    # screenshot of viewport, which in this case is 1200 x 2000 pixels
    driver.save_screenshot(f'screenshot-headless-files-{page_index}.png')
    print(f'saved screenshot {page_index}')

def scrape(df, index_start, index_stop):
    # for each row of my dataframe, I am getting the url for the page I need to scrape.
    for index, row in df.iloc[index_start:index_stop, ].iterrows():
        page_index = index
        url = row['url']
        scrape_page(url, page_index)

scrape(df, index_start, index_stop)

driver.close()

print(f'\nFinished {str(sys.argv)}')






