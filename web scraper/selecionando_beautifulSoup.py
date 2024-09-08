import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')


all_h1_tags = []

# Definir all_h1_tags como todas as tags h1 de soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Criar seventh_p_text e defini-lo como o texto do 7º elemento p da página
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags, seventh_p_text)
