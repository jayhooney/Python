import time
from selenium import webdriver


# 크롬 드라이버 세팅
browser = webdriver.Chrome("./ChromeDriver/chromedriver_mac64/chromedriver")

# 한성컴퓨터 GK898B OfficeMaster 무접점 키보드 (블루투스 5.0) 페이지로 이동.
browser.get('https://www.monsterlabs.co.kr/src/category/read.html?pn=44004')

# 현재 존재하는 옵션들 크롤링
elementList = browser.find_elements_by_css_selector(
    "body > ul > li:nth-child(2) > a")

for element in elementList:
    print(element.get_attribute("innerText"))


time.sleep(10)

browser.quit()
