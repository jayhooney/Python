import time
from selenium import webdriver


def crawler():
    # 크롬 드라이버 경로
    CHROME_DRIVER_PATH = "./ChromeDriver/chromedriver_mac64/chromedriver"
    # 한성컴퓨터 GK898B OfficeMaster 무접점 키보드 (블루투스 5.0) 제품 설명 페이지 주소
    URL = "https://www.monsterlabs.co.kr/src/category/read.html?pn=44004"
    # 키보드 옵션 목록 CSS SELECTOR
    keyboardOptionListSelector = "body > ul > li:nth-child(2) > a"
    # 키보드 옵션 NODE의 텍스트를 가져올 ATTR
    keyboardOptionAttr = "innerText"
    # 내가 찾는 옵션 문자열
    myWhis = "화이트 한글키캡"

    print("CHROME DRIVER SETTING ...")
    # 옵션 세팅
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')

    # 크롬 드라이버 세팅
    browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    print("COMPLETE !")

    print("GO TO :", URL)
    browser.get(URL)
    print("COMPLETE !")

    # 현재 존재하는 옵션들 크롤링
    print("CRAWL START !")
    elementList = browser.find_elements_by_css_selector(
        keyboardOptionListSelector)

    print("###################### OPTION LIST ###########################")
    for element in elementList:

        optionInnerText = "<" + element.get_attribute(keyboardOptionAttr) + ">"

        if myWhis in optionInnerText:
            print(optionInnerText, " @@@@@@@ 큰누나가 찾던거!! 얼른 주문!! @@@@@@")
        else:
            print(optionInnerText)
    print("###############################################################")

    print("CRAWL END")

    print("CLOSE BROWSER . . .")
    browser.quit()
    print("COMPLETE !")

    return


def main():
    crawler()
    return


main()
