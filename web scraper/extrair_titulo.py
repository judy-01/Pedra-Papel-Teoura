import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extrair o título da página
page_title = soup.title.text

print(page_title)