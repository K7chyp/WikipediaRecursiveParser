from SubFunctions import dict_preprocessing
from SubFunctions import write_to_file
from BaseClassPage import WikipediaPageParser
from tqdm import tqdm
from re import search

URL:  str = str(input("Input a wiki url page "))
WIKIPEDIA_URL = "https://{}.wikipedia.org".format(search("\/..\.", URL).group(0)[1:-1])

def get_output_from_page(url: str) -> dict:
    page = WikipediaPageParser(url)
    hrefs = page.hrefs
    information_from_page: dict = {
        "text": page.text_from_page,
        "table": page.right_table,
    }
    return {str(url): information_from_page}, hrefs


def preprocess_output(href: str, output: dict, hrefs: list):

    information_from_page, local_hrefs = get_output_from_page(WIKIPEDIA_URL + href)
    output: dict = dict_preprocessing(information_from_page, output)
    hrefs.append(local_hrefs)
    return output, hrefs


def get_recursive(output: dict, hrefs: list):
    for href in tqdm(hrefs):
        if type(href) == list:
            continue
        output, new_hrefs = preprocess_output(href, output, hrefs)
    return output, new_hrefs


def recursive_page_parser(filename: str, recursive_depth: int) -> None:
    output, hrefs = get_output_from_page(URL)
    output, new_hrefs = get_recursive(output, hrefs)
    for _ in range(recursive_depth + 1):
        output, new_hrefs = get_recursive(output, new_hrefs)
    write_to_file(filename, output)
