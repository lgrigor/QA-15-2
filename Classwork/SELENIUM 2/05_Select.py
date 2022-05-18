import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(service=ChromeService(), options=chrome_options)
browser.get("https://www.webpagetest.org/lighthouse")

select = Select(browser.find_element(By.ID, "location"))
time.sleep(3)
select.select_by_value('ec2-eu-west-1:Chrome.3GFast')

time.sleep(3)
select.select_by_index(4)

time.sleep(3)
select.select_by_visible_text('Japan')
