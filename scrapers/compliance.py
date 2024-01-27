from bs4 import BeautifulSoup
from scrapers import constants
import requests


class WebScraper:
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get("url", "")
        self.identifier = kwargs.get("identifier", "")

    def get_webpage_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from {url}: {e}")
            return None

    def parse(self, url, identifier):
        print(f"PARSING {identifier} PAGE: {url}")
        if url:
            self.url = url
        if identifier:
            self.identifier = identifier
        page_html = self.get_webpage_content(self.url)
        if not page_html:
            return None
        soup = BeautifulSoup(page_html, "html.parser")
        response = None
        if self.identifier == constants.STRIPE:
            response = self.__stripe_complaince(soup)
        elif self.identifier == constants.GAUVA:
            response = self.__gauva_page(soup)
        else:
            print(f"Unsupported complaince type: {self.identifier}")
        return response

    def __stripe_complaince(self, soup):
        return soup.article.get_text(separator="\n")

    def __gauva_page(self, soup):
        return soup.get_text(separator="\n")
