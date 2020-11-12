import time
from selenium import webdriver

driver = webdriver.Chrome("./ChromeDriver/chromedriver_mac64/chromedriver")

driver.get('https://www.monsterlabs.co.kr/src/category/read.html?pn=44004')
time.sleep(10)

driver.quit()
