# Usando função

import requests

print('Github Users')
def obter_informacoes_usuario(username):

    url = f'https://api.github.com/users/{username}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return None

# Exemplo de Uso:
username = input("Digite o nome de usuário do GitHub: ")
informacoes = obter_informacoes_usuario(username)

if informacoes:
    print(f"\nInformações do Usuário {username}:")
    print(f"URL do Perfil: {informacoes['html_url']}")
    print(f"Repositórios Públicos: {informacoes['public_repos']}")
else:
    print(f"Usuário '{username}' não encontrado.")