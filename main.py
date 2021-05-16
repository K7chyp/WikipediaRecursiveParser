from BaseClassPage import WikipediaPageParser


def main():
    print(WikipediaPageParser("https://en.wikipedia.org/wiki/Python").hrefs)


if __name__ == "__main__":
    main()