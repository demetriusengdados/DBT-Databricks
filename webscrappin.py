import requests
from bs4 import BeautifulSoup
import pandas as pd

#buscando as informações do site
page = requests.get("https://www.urldosite.com.br")

#fazendo o parse do conteudo HTML
soup = BeautifulSoup(page.content, 'html.parser')

#pesquisando todos os links do site (tag<a>)
links = soup.find_all("a")

#inserindo o resultado em um dicionario 
dados = {"titulo": [], "link": []}
for link in links:
    dados["titulo"].append(link.get("title"))
    dados["link"].append(link.get("href"))

#exportando para um arquivo excel 
df = pd.DataFrame(dados)
df.to_excel("listagemn_links.xlsx", index=False)