import requests
from bs4 import BeautifulSoup
import os

response = requests.get(
    "https://escoladepos.ufg.br/cursos/curso-de-especializacao-em-construcao-civil/"
)
content = response.content
site = BeautifulSoup(content, "html.parser")
# print(site.prettify())
# print(site.text)


#paragrafos = site.findAll("p")
# print(len(paragrafos))
#for paragrafo in paragrafos:
#    print(paragrafo.text)


# Exemplo de como salvar a saída do print em um arquivo .txt
paragrafos = site.findAll("p")  # Encontra todos os parágrafos

# Abre (ou cria) o arquivo no modo de escrita
with open("saida_paragrafos.txt", "w", encoding="utf-8") as arquivo:
    for paragrafo in paragrafos:
        arquivo.write(
            paragrafo.text + "\n"
        )  # Salva o texto do parágrafo no arquivo, separando por linha

print("Os textos foram salvos no arquivo 'saida_paragrafos.txt'")
