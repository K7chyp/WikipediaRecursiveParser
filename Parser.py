from SubFunctions import dict_preprocessing
from SubFunctions import writerow_preprocessing
from BaseClassPage import WikipediaPageParser
from tqdm import tqdm
from csv import writer
from re import search

RECUSIVE_DEPTH: int = int(input("Input recursive depth "))
FILENAME: str = str(input("Input a filename .csv "))
url: str = str(input("Input a wiki url page "))

WIKIPEDIA_URL = "https://{}.wikipedia.org".format(search("\/..\.", url).group(0)[1:-1])


def get_output_from_page(url) -> dict:
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


def get_recursive(output, hrefs):
    for href in tqdm(hrefs):
        if type(href) == list:
            continue
        output, new_hrefs = preprocess_output(href, output, hrefs)
    return output, new_hrefs


def recursive_page_parser(url, filename, recursive_depth):
    output, hrefs = get_output_from_page(url)
    output, new_hrefs = get_recursive(output, hrefs)
    for _ in range(recursive_depth + 1):
        output, new_hrefs = get_recursive(output, new_hrefs)

    with open(f"{filename}.csv", "w") as csv_file:
        write = writer(csv_file)
        write.writerow(["href", "text", "info"])
        for href, elemnts in output.items():
            write.writerow(writerow_preprocessing(href, elemnts))
