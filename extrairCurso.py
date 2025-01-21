import requests
from bs4 import BeautifulSoup

# URL do site que você deseja extrair o texto
url = "https://escoladepos.ufg.br/cursos/curso-de-especializacao-em-construcao-civil/"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Criando o objeto BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraindo apenas o texto da página
    texto = soup.get_text(
        strip=True
    )  # Extrai o texto completo, removendo espaços extras

    # Salvando o texto extraído em um arquivo .txt (opcional)
    with open("texto_extraido.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

    print("Texto extraído com sucesso!")
    print(texto[:500])  # Exibindo os primeiros 500 caracteres do texto extraído
else:
    print(f"Erro ao acessar o site. Código HTTP: {response.status_code}")
