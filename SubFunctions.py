from bs4 import BeautifulSoup
from re import sub


def get_all_product_hrefs_from_page(soup: BeautifulSoup):
    return [
        part_of_page.get("href")
        for part_of_page in soup.find_all("a")
        if "/wiki/" in str(part_of_page)
        and ("https" or "wikipedia") not in str(part_of_page).lower()
    ]


def clear_nums_in_brascets(string: str) -> str:
    return sub("\[[0-9]+\]", "", string)


def find_all_something_in_soup_by_class(
    soup: BeautifulSoup, tag: str, class_: dict
) -> list:
    return [clear_nums_in_brascets(content.text) for content in soup.find_all(tag, class_)]
