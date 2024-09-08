import requests
from bs4 import BeautifulSoup

page = requests.get(
   "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")  
soup = BeautifulSoup(page.content, 'html.parser')


top_items = []

# Extrair e armazenar em top_items de acordo com as instruções
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

print(top_items)