import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.base_url = "https://www.merriam-webster.com/dictionary/"

    def lookup_definition(self, word):
        url = self.base_url + word
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            definition = soup.find("span", class_="dtText")
            if definition:
                return definition.get_text(strip=True)
        return "Definition not found."