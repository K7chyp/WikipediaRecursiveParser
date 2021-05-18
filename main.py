from Parser import recursive_page_parser


def main():
    recursive_depth: int = int(input("Input recursive depth "))
    filename: str = str(input("Input a filename .csv "))
    url: str = str(input("Input a wiki url page "))
    recursive_page_parser(url, filename, recursive_depth)


if __name__ == "__main__":
    main()
