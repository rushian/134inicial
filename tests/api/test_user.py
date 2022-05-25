# done ToDo 1: Criar um teste que adicione um usuario
# ToDo 2: realizar um login e extrair o token da reposta
# ToDo 3: Criar uma venda de um pet para um usuario
# ToDo 4: Consultar dados do animal vendido
import json
import os

import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json',
           'accept': 'application/json' }
# comando para determinar diretorio onde inicial a referencia de caminho relativo
os.chdir(f'E:{os.sep}dev{os.sep}pyCharm{os.sep}134inicial{os.sep}')

def teste_incluir_usuario():
    # Configura
    # dados de entrada
    # virao do arquivo usuario1.json

    # resultado esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '778321305'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open(f'vendors{os.sep}json{os.sep}usuario1.json')
    )

    # Valida
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada

def teste_consultar_usuario():
    # Configura
    # dados de entrada
    username = 'leo'
    password = 'entrar'

    # resultado esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )

    # Valida
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find( corpo_do_resultado_obtido['message'])

    # Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23::2] #[inicio:fim]
    print(f'O token = {token}')
