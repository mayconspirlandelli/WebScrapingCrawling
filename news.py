import requests
from bs4 import BeautifulSoup

response = requests.get('https://escoladepos.ufg.br/duvidas/')
content = response.content
site = BeautifulSoup(content, 'html.parser')
# print(site.prettify())

# class="elementor-tab-title elementor-tab-mobile-title elementor-active"
#class="elementor-heading-title elementor-size-default"
noticia = site.find('h1', attrs={'class': 'elementor-heading-title elementor-size-default'})
#print(noticia.text)

#class="elementor-element elementor-element-efec5de e-con-full e-flex e-con e-child"
divPerguntas = site.find('div', attrs={'class': 'elementor-element elementor-element-efec5de e-con-full e-flex e-con e-child'})
#print(divPerguntas.prettify())

#div_content = soup.find('div', {'id': 'elementor-tab-title-1121'})
divNaoSouAlunoTitulo = divPerguntas.find('div', {'id': 'elementor-tab-title-1121'})
print(divNaoSouAlunoTitulo.text)


divNaoSouAlunoContent = divPerguntas.find('div', {'id': 'elementor-tab-content-1121'})
#print(divNaoSouAlunoContent.prettify())

#Lista de perguntas
listaPerguntas = divNaoSouAlunoContent.find('p').find('strong')
#print(listaPerguntas.prettify())

respostaPergunta = divNaoSouAlunoContent.findAll('p')
print(len(respostaPergunta))
for paragrafo in respostaPergunta:
    print(paragrafo.prettify())


print('\n', 'NAO SOU ALUNO')
# Encontra todas as tags <p> e extrai apenas o texto
paragraphs = divNaoSouAlunoContent.findAll('p')
for paragraph in paragraphs:
    #text = paragraph.get_text(strip=True)
    #print(text)
    #ou simplesmente assim
    print(paragraph.text)


divSouAlunoContent = divPerguntas.find('div', {'id': 'elementor-tab-content-1122'})
paragraphs = divSouAlunoContent.findAll('p')
print('\n', 'SOU ALUNO')
for paragraph in paragraphs:
    print(paragraph.text)