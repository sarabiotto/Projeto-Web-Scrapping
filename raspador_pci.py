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

cidades_alvo = ['rio claro']
vagas = sopa.select('.da, .na, .ea')
print("Iniciando a busca por vagas...\n")

qtd_vagas_encontradas = 0

for vaga in vagas:
    texto_vaga = vaga.text.lower()
    tem_cidade = any(cidade in texto_vaga for cidade in cidades_alvo)
    if tem_cidade:
        qtd_vagas_encontradas += 1 
        texto_limpo = vaga.text.strip()
        print("-" * 50)
        print("VAGAS:")
        print(texto_limpo)
print("-" * 50)
if qtd_vagas_encontradas > 0:
    print(f"Busca concluída! O site entregou {qtd_vagas_encontradas} vaga(s) de concurso para a sua busca.")
else:
    print("Nenhuma vaga encontrada no momento.")