import requests
import lxml
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS


class RaketaParser:
    def __init__(self, url):
        self.url = url
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers = {
            "accept": "*/*",
            "user-agent": self.ua.random
        }
        self.response = self.session.get(self.url)
        self.data_text_page = self.response.text
        self.soup = BS(self.data_text_page, "lxml")

    def save_data_page(self):
        with open("data/page.html", "w", encoding="utf-8") as file:
            file.write(self.data_text_page)

    @staticmethod
    def open_data_page(self):
        with open("data/page.html", "r", encoding="utf-8") as file:
            data_text_page = file.read()

        return data_text_page

    @staticmethod
    def save_info(self, name_file: str, my_dict):
        with open(f"data/{name_file}.json", "w", encoding="utf-8") as file:
            json.dump(my_dict, file, indent=4, ensure_ascii=False)
