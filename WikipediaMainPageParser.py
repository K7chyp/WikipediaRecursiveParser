from BaseClassBrowser import BaseClassPageSettings
from SubFunctions import get_all_hrefs_from_page

WIKIPEDIA_MAIN_PAGE_URL = "https://en.wikipedia.org/wiki/Main_Page"


class WikipediaMainPageParser(BaseClassPageSettings):
    def __init__(self):
        super().__init__(
            WIKIPEDIA_MAIN_PAGE_URL="https://en.wikipedia.org/wiki/Main_Page"
        )
        self.hrefs = get_all_hrefs_from_page(self.soup)