from temaCurs5 import WebScrapper
from pprint import pprint


if __name__ == '__main__':
    scrapper = WebScrapper()
    scrapper.get_jucatori()
    scrapper.get_jucatori(2)
    # scrapper.get_jucatori(3)
    scrapper.salveaza_in_fisier()
    scrapper.citeste_din_fisier()
    print(scrapper)
    # pprint(scrapper.get_jucatori())
    # print('\n')
    # print(scrapper)
