# Sem usar função

import requests

print('Github Users')
username = input('Qual é o nome do usuário?')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'###############################')
    print(f'Nome completo: {data["name"]}')
    print(f'Endereço do repositório: {data["html_url"]}')
    print(f'Repositório(s) publico(s): {data["public_repos"]}')
    print(f'###############################')
else:
    print('Não foi possível encontrar o usuário, verifique se o usuário está correto!')
