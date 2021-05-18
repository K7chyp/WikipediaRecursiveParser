from BaseClassBrowser import BaseClassPageSettings
from SubFunctions import get_all_hrefs_from_page
from SubFunctions import clear_nums_in_brascets
from SubFunctions import find_all_something_in_soup_by_class


class WikipediaPageParser(BaseClassPageSettings):
    def __init__(self, url) -> None:
        self.url: str = url
        super().__init__(self.url)
        self.get_common_info_about_page()
        self.get_information_from_right_table()

    def get_common_info_about_page(self) -> None:
        self.hrefs: list = get_all_hrefs_from_page(self.soup)
        self.text_from_page: str = clear_nums_in_brascets(
            "".join(part_of_page.text for part_of_page in self.soup.find_all("p"))
        )

    def get_information_from_right_table(self):
        self.right_table = {
            name: content
            for name, content in zip(
                find_all_something_in_soup_by_class(
                    self.soup, "th", {"class": "infobox-label"}
                ),
                find_all_something_in_soup_by_class(
                    self.soup, "td", {"class": "infobox-data"}
                ),
            )
        }
