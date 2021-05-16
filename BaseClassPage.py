from BaseClassBrowser import BaseClassPageSettings
from SubFunctions import get_all_product_hrefs_from_page
from re import sub


class WikipediaPageParser(BaseClassPageSettings):
    def __init__(self, url) -> None:
        self.url: str = url
        super().__init__(self.url)
        self.hrefs: list = get_all_product_hrefs_from_page(self.soup)
        self.text_from_page: str = sub(
            "\[[0-9]+\]",
            "",
            "".join([part_of_page.text for part_of_page in self.soup.find_all("p")]),
        )
