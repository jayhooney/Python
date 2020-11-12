from selenium import webdriver


class Crawler:

    browser = None

    def __init__(self):
        print("CHROME DRIVER SETTING ...")
        # 크롬 드라이버 경로
        CHROME_DRIVER_PATH = "./ChromeDriver/chromedriver_mac64/chromedriver"

        # 옵션 세팅
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')

        # 크롬 드라이버 세팅
        self.browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
        print("COMPLETE !")
        return

    def GotoLink(self):
        # 한성컴퓨터 GK898B OfficeMaster 무접점 키보드 (블루투스 5.0) 제품 설명 페이지 주소
        URL = "https://www.monsterlabs.co.kr/src/category/read.html?pn=44004"
        print("GO TO :", URL)
        self.browser.get(URL)
        print("COMPLETE !")
        return

    def Crawler(self):
        # 키보드 옵션 목록 CSS SELECTOR
        keyboardOptionListSelector = "body > ul > li:nth-child(2) > a"
        # 키보드 옵션 NODE의 텍스트를 가져올 ATTR
        keyboardOptionAttr = "innerText"
        # 내가 찾는 옵션 문자열
        myWhis = "화이트 한글키캡"

        # 현재 존재하는 옵션들 크롤링
        print("CRAWL START !")
        elementList = self.browser.find_elements_by_css_selector(
            keyboardOptionListSelector)

        print("###################### OPTION LIST ###########################")
        for element in elementList:

            optionInnerText = "<" + \
                element.get_attribute(keyboardOptionAttr) + ">"

            if myWhis in optionInnerText:
                print(optionInnerText, " @@@@@@@ 큰누나가 찾던거!! 얼른 주문!! @@@@@@")
            else:
                print(optionInnerText)
        print("##############################################################")

        print("CRAWL END")

        return

    def CloseBrowser(self):
        print("CLOSE BROWSER . . .")
        self.browser.quit()
        print("COMPLETE !")
        return

    def Start(self):

        self.GotoLink()
        self.Crawler()
        self.CloseBrowser()

        return
