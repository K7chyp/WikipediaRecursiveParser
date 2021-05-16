import os
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep



class BaseClassPageSettings:
    SCROLL_PAUSE_TIME = 1

    def __init__(self, url):
        self.url = url
        self.set_browser()
        self.scroll_down_page()
        self.get_html()
        self.soup = BeautifulSoup(self.html, "lxml")

    def set_browser(self):
        self.options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(
            str(os.path.dirname(os.path.realpath(__file__)))
            + "/SeleniumFiles/chromedriver",
            options=self.options,
        )

    def get_html(self) -> None:
        self.browser.get(self.url)
        self.html: list = self.browser.page_source

    def scroll_down_page(self) -> None:
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(self.SCROLL_PAUSE_TIME)
