from bs4 import BeautifulSoup
from re import sub


def get_all_product_hrefs_from_page(soup: BeautifulSoup):
    return [
        part_of_page.get("href")
        for part_of_page in soup.find_all("a")
        if "/wiki/" in str(part_of_page)
        and ("https" or "wikipedia" or "category" or "special")
        not in str(part_of_page).lower()
    ]


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
