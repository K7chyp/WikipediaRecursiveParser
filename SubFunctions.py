from bs4 import BeautifulSoup, element
from re import sub
from re import search
from re import compile


def is_href_valid(href) -> bool:
    for pattern in (
        "https",
        "Wikipedia",
        "wikimedia",
        "Category",
        "Special",
        "//",
        "Help",
        "Portal",
        "Talk",
        "Main_Page",
        "File",
    ):
        if compile(pattern).search(href) is not None:
            return False
    return True


def get_all_hrefs_from_page(soup: BeautifulSoup):
    hrefs = []
    for item in (
        part_of_page.get("href")
        for part_of_page in soup.find_all("a")
        if (
            "wiki" in str(part_of_page.get("href"))
            and is_href_valid(str(part_of_page.get("href")))
        )
    ):
        if type(item) == str:
            hrefs.append(item)
        elif type(item) == list:
            for elem in item:
                hrefs.append(elem)
    return hrefs


def clear_nums_in_brascets(string: str) -> str:
    return sub("\[[0-9]+\]", "", string)


def find_all_something_in_soup_by_class(
    soup: BeautifulSoup, tag: str, class_: dict
) -> list:
    return [
        clear_nums_in_brascets(content.text.replace("\xa0", " "))
        for content in soup.find_all(tag, class_)
    ]


def dict_preprocessing(dict_last_iteration: dict, dict_new_itrearion: dict) -> dict:
    utility_dict: dict = dict_new_itrearion.copy()
    dict_new_itrearion: dict = {**utility_dict, **dict_last_iteration}
    return dict_new_itrearion
