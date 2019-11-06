# scraping
from selenium import webdriver
import time
import sys
import chromedriver_binary

urls = {
    'url1': 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=fn_al_kw_1',
    'url2': 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page=2'
}

url_env = sys.argv[1]
url = urls[url_env]

driver = webdriver.Chrome()

driver.get(url)
time.sleep(1)

# screenshot of viewport, which in this case is 1200 x 3000 pixels
driver.save_screenshot(f'screenshot-{url_env}.png')

