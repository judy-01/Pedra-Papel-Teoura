import requests

res = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
txt = res.text
status = res.status_code

print(txt, status)

'''
A solicitação de HTTP retorna um objeto response com 
todos os dados de resposta (conteúdo, código, status e assim por diante). 
'''