from SubFunctions import dict_preprocessing
from BaseClassPage import WikipediaPageParser
from tqdm import tqdm
from csv import writer

RECURSIVE: bool = bool(int(input("1: - Recursive True, 0: - False ")))
FILENAME: str = str(input('Input a filename .csv '))
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


def preprocess_output(href: str, output: dict, hrefs: list):
    information_from_page, local_hrefs = get_output_from_page(WIKIPEDIA_URL + href)
    output: dict = dict_preprocessing(information_from_page, output)
    hrefs.append(local_hrefs)
    return output, hrefs

def writerow_preprocessing(
    short_article_name: str, dict_with_information: dict
) -> list:
    return [short_article_name] + [item for _, item in dict_with_information.items()]


if RECURSIVE:
    output, hrefs = get_output_from_page(url)
    for href in tqdm(hrefs):
        if type(href) == list: 
            continue
        output, hrefs = preprocess_output(href, output, hrefs)



with open(f"{FILENAME}.csv", "w") as csv_file:
    write = writer(csv_file)
    write.writerow(['href', 'text', 'info'])
    for href, elemnts in output.items():
        write.writerow(writerow_preprocessing(href, elemnts))

