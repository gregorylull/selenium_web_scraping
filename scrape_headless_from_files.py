
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import chromedriver_binary
import pandas as pd

index_start = int(sys.argv[1])
index_stop = int(sys.argv[2])

with open('urls.csv', 'r') as readfile:
    df = pd.read_csv(readfile, delim_whitespace=True)

# go headless
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=992,1200")

driver = webdriver.Chrome(options=chrome_options)

def scrape_page(url, page_index):
    driver.get(url)
    time.sleep(1)

    # screenshot of viewport, which in this case is 1200 x 2000 pixels
    driver.save_screenshot(f'screenshot-headless-files-{page_index}.png')
    print(f'saved screenshot {page_index}')

def scrape(df, index_start, index_stop):
    for index, row in df.iloc[index_start:index_stop, ].iterrows():
        page_index = index
        url = row['url']
        scrape_page(url, page_index)

scrape(df, index_start, index_stop)








