from temaCurs5 import WebScrapper

if __name__ == '__main__':
    scrapper = WebScrapper()
    # scrapper.getJucatori()
    # scrapper.getJucatori(2)
    # scrapper.getJucatori(3)
    # scrapper.salveazaInFisier()
    scrapper.citeste_din_fisier()
    print(scrapper)
