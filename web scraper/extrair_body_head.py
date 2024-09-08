import requests
from bs4 import BeautifulSoup

# Fazer uma solicitação
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

soup = BeautifulSoup(page.content, 'html.parser')

# Extrair o título da página
page_title = soup.title.text

# Extrair o body da página
page_body = soup.body

# Extrair a head da página
page_head = soup.head


print(page_body, page_head)