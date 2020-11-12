from selenium import webdriver
from Define.Config import CrawlerConf
import json


class Crawler:

    browser = None

    def __init__(self):
        print("CHROME DRIVER SETTING ...")

        # 옵션 세팅
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')

        # 크롬 드라이버 세팅
        self.browser = webdriver.Chrome(
            CrawlerConf.CHROME_DRIVER_PATH, options=options)
        print("COMPLETE !")
        return

    def GotoLink(self):
        print("GO TO :", CrawlerConf.URL)
        self.browser.get(CrawlerConf.URL)
        print("COMPLETE !")
        return

    def ReadSelector(self):
        print("START READ SELECTOR JSON FILE")
        selectors = None

        with open("./Define/Selector.json") as selectorFile:
            selectors = json.load(selectorFile)

        print("COMPLETE")

        return selectors

    def Crawler(self):

        # 현재 존재하는 옵션들 크롤링
        print("CRAWL START !")

        selectors = self.ReadSelector()

        elementList = self.browser.find_elements_by_css_selector(
            selectors["optionList"])

        print("###################### OPTION LIST ###########################")
        for element in elementList:

            optionInnerText = "<" + \
                element.get_attribute(selectors["optionAttr"]) + ">"

            if CrawlerConf.MY_WISH in optionInnerText:
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
