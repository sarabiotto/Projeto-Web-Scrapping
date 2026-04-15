import requests
from bs4 import BeautifulSoup

url = 'https://www.pciconcursos.com.br/concursos/sudeste/'
print("Acessando o site PCI Concursos...")

res = requests.get(url)
res.raise_for_status()

sopa = BeautifulSoup(res.text, 'html.parser')
cidades_alvo = ['rio claro']

vagas = sopa.select('.da, .na, .ea')

print("Iniciando a busca por vagas...\n")
encontrou_vaga = False

for vaga in vagas:
    texto_vaga = vaga.text.lower()
    
    tem_cidade = any(cidade in texto_vaga for cidade in cidades_alvo)
    tem_pcd = 'pcd' in texto_vaga or 'deficiência' in texto_vaga
    
    if tem_cidade and tem_pcd:
        encontrou_vaga = True
        texto_limpo = vaga.text.strip()
        print("-" * 50)
        print("🚨 VAGA ENCONTRADA:")
        print(texto_limpo)

if not encontrou_vaga:
    print("-" * 50)
    print("Nenhuma vaga com cota PCD encontrada para as cidades listadas neste momento.")