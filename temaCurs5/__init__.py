import requests
from bs4 import BeautifulSoup
from os.path import isfile
import json
from tabulate import tabulate
from json.decoder import JSONDecodeError


class WebScrapper(object):
    def __init__(self, **kwargs):
        self._url = kwargs['url'] if self._check_if_in_kwargs(
            kwargs, 'url') else 'https://www.chess.com/players'

        self._containerLista = kwargs['containerLista'] if self._check_if_in_kwargs(kwargs, 'containerLista') else {
            'htmlElement': 'div', 'class_': 'post-preview-list-component-v5 authors-list'}

        self._listaJucatori = kwargs['listaJucatori'] if self._check_if_in_kwargs(kwargs, 'listaJucatori') else {
            'htmlElement': 'div', 'class_': 'post-author-component authors-post'}

        self._containerHeader = kwargs['containerHeader'] if self._check_if_in_kwargs(kwargs, 'containerHeader') else {
            'htmlElement': 'div', 'class_': 'post-author-right'}

        self._containerHeaderH2 = kwargs['containerHeaderH2'] if self._check_if_in_kwargs(kwargs, 'containerHeaderH2') else {
            'htmlElement': 'h2', 'class_': 'post-author-author master-players-player-title'}

        self._denumireContainer = kwargs['denumireContainer'] if self._check_if_in_kwargs(kwargs, 'denumireContainer') else {
            'htmlElement': 'a', 'class_': 'master-players-player-name'}

        self._clasamentJucator = kwargs['clasamentJucator'] if self._check_if_in_kwargs(kwargs, 'clasamentJucator') else {
            'htmlElement': 'a', 'class_': 'master-players-world-stats'}

        self._rankJucator = kwargs['rankJucator'] if self._check_if_in_kwargs(kwargs, 'rankJucator') else {
            'htmlElement': 'span', 'class_': 'master-players-chess-title'}

        self._denumireJucator = kwargs['denumireJucator'] if self._check_if_in_kwargs(kwargs, 'denumireJucator') else {
            'htmlElement': 'span', 'class_': 'post-author-name'}

        self._jucatoriFormatati = dict()

    def __str__(self):
        totiJucatorii = self._get_reprezentare()
        return self._print(totiJucatorii)

    def _print(self, lista):
        return tabulate(lista, headers=['Pozitie', 'Rank', 'Denumire', 'Puncte'])

    def _check_if_in_kwargs(self, kwargs, key):
        return key in kwargs.keys()

    def _get_reprezentare(self):
        totiJucatorii = []
        listaTotiJucatorii = map(
            self._build_print_obj, self._jucatoriFormatati.keys())
        for listaJucator in listaTotiJucatorii:
            totiJucatorii.extend(listaJucator)
        return totiJucatorii

    def _build_print_obj(self, pagina):
        listaJucator = self._jucatoriFormatati[pagina]
        return list(map(lambda jucator: [jucator['loc'], jucator['rank'], jucator['denumire'], jucator['puncte']], listaJucator))

    def _build_obj(self, jucatorRand):
        containerHeader = jucatorRand.find(self._containerHeader['htmlElement'], class_=self._containerHeader['class_']).find(
            self._containerHeaderH2['htmlElement'], class_=self._containerHeaderH2['class_'])

        denumireContainer = containerHeader.find(
            self._denumireContainer['htmlElement'], class_=self._denumireContainer['class_'])

        clasamentJucator = containerHeader.find(
            self._clasamentJucator['htmlElement'], class_=self._clasamentJucator['class_']).text.strip()

        puncteJucator, locJucator = clasamentJucator.split('|')

        puncteJucatorInt, locJucatorInt = int(
            puncteJucator.strip()), int(locJucator.strip().replace('#', ''))

        rank = denumireContainer.find(
            self._rankJucator['htmlElement'], class_=self._rankJucator['class_']).text.strip()
        denumire = denumireContainer.find(
            self._denumireJucator['htmlElement'], class_=self._denumireJucator['class_']).text.strip()

        return {'loc': locJucatorInt, 'rank': rank, 'denumire': denumire, 'puncte': puncteJucatorInt}

    def get_jucatori(self, numarPagina=-1):
        if(numarPagina in self._jucatoriFormatati.keys()):
            return self._jucatoriFormatati[numarPagina]

        _url = self._url if numarPagina < 1 else f'{self._url}?page={numarPagina}'

        siteHtml = requests.get(_url)

        continut = BeautifulSoup(siteHtml.content, 'html.parser')

        containerJucatori = continut.find(
            self._containerLista['htmlElement'], class_=self._containerLista['class_'])

        listaJucatori = containerJucatori.find_all(
            self._containerLista['htmlElement'], class_=self._listaJucatori['class_'])

        jucatoriFormatati = map(self._build_obj, listaJucatori)

        self._jucatoriFormatati[str(numarPagina if numarPagina > 1 else 1)] = list(
            jucatoriFormatati)

        if(numarPagina == -1):
            return [self._jucatoriFormatati[str(numarPagina)] for numarPagina in self._jucatoriFormatati.keys()][0]
        return self._jucatoriFormatati[str(numarPagina)]

    def salveaza_in_fisier(self, pagina=-1, rescrie=True):
        with open('./temaCurs5/jucatori.txt', 'w' if rescrie else 'a') as f:
            if(pagina == -1):
                json.dump(self._jucatoriFormatati, f)

    def citeste_din_fisier(self, pagina=1):
        if(isfile('./temaCurs5/jucatori.txt')):
            with open('./temaCurs5/jucatori.txt', 'r') as f:
                try:
                    self._jucatoriFormatati = json.load(f)
                except JSONDecodeError:
                    return "Fisierul este gol"
                listaJucatori = self._build_print_obj(str(pagina))
                return self._print(listaJucatori)

        return 'Fisierul nu exista'
