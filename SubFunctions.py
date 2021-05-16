from bs4 import BeautifulSoup


def get_all_product_hrefs_from_page(soup: BeautifulSoup):
    return [
        part_of_page.get("href")
        for part_of_page in soup.find_all("a")
        if "/wiki/" in str(part_of_page) and ("https" or 'wikipedia') not in str(part_of_page).lower()
    ]
