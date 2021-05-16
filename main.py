from BaseClassPage import WikipediaPageParser


def main():
    print(
        len(WikipediaPageParser(
            "https://en.wikipedia.org/wiki/Diet_of_Speyer_(1529)"
        ).hrefs)
    )

 
if __name__ == "__main__":
    main()