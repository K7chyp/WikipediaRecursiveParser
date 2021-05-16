from SubFunctions import dict_preprocessing
from BaseClassPage import WikipediaPageParser
from tqdm import tqdm

RECURSIVE: bool = bool(int(input("1: - Recursive True, 0: - False ")))
wiki_type: str = str(input("Choose wikipedia language. For instance ru or en "))
url: str = str(input("Input a wiki url page "))

WIKIPEDIA_URL = "https://{}.wikipedia.org".format(wiki_type)


def get_output_from_page(url) -> dict:
    page = WikipediaPageParser(url)
    hrefs = page.hrefs
    information_from_page: dict = {
        "text": page.text_from_page,
        "table": page.right_table,
    }
    return {str(url): information_from_page}, hrefs


if RECURSIVE:
    output, hrefs = get_output_from_page(url)
    for href in tqdm(hrefs):
        information_from_page, local_hrefs = get_output_from_page(WIKIPEDIA_URL + href)
        output: dict = dict_preprocessing(information_from_page, output)
        hrefs.append(local_hrefs)

print(output, len(hrefs))
