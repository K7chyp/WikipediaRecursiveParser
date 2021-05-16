from BaseClassPage import WikipediaPageParser


def main():
    print(
        WikipediaPageParser(
            "https://en.wikipedia.org/wiki/Python_(programming_language)"
        ).text_from_page
    )


if __name__ == "__main__":
    main()