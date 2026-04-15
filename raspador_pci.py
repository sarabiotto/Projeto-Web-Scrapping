import requests
from bs4 import BeautifulSoup

url = 'https://www.pciconcursos.com.br/concursos/sudeste/'
print("Acessando o site PCI Concursos...")

res = requests.get(url)
res.raise_for_status()
