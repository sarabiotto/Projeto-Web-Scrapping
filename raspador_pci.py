import requests
from bs4 import BeautifulSoup

url = 'https://www.pciconcursos.com.br/concursos/sudeste/'

cabecalhos = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Acessando o site PCI Concursos...")

res = requests.get(url, headers=cabecalhos)
res.raise_for_status()

sopa = BeautifulSoup(res.text, 'html.parser')

cidades_alvo = ['rio claro', 'piracicaba', 'limeira', 'araras']

vagas = sopa.select('.da, .na, .ea')

print(f"O site entregou {len(vagas)} vagas de concursos.\n")

encontrou_vaga = False

for vaga in vagas:
    texto_vaga = vaga.text.lower()
    
    # Continua buscando por qualquer cidade da lista sem exigir a cota PCD neste teste
    tem_cidade = any(cidade in texto_vaga for cidade in cidades_alvo)
    
    if tem_cidade:
        encontrou_vaga = True
        texto_limpo = vaga.text.strip()
        print("-" * 50)
        print("VAGA ENCONTRADA:")
        print(texto_limpo)

if not encontrou_vaga:
    print("-" * 50)
    print("Nenhuma vaga encontrada para as cidades listadas neste momento.")