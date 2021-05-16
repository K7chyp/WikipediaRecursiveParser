from BaseClassBrowser import BaseClassPageSettings
from SubFunctions import get_all_product_hrefs_from_page

class WikipediaPageParser(BaseClassPageSettings): 
    def __init__(self, url): 
        self.url = url
        super().__init__(self.url)
        self.hrefs = get_all_product_hrefs_from_page(self.soup)