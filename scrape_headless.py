
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import chromedriver_binary

urls = {
    'url1': 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=fn_al_kw_1',
    'url2': 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page=2'
}

url_env = sys.argv[1]
url = urls[url_env]

# go headless
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1200,3000")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
time.sleep(1)

# screenshot of viewport, which in this case is 1200 x 3000 pixels
driver.save_screenshot(f'screenshot-headless-{url_env}.png')

