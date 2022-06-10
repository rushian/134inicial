# ToDo 3: Criar uma venda de um pet para um usuario
# ToDo 4: Consultar dados do animal vendido
import json
import os
from pathlib import Path

import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}
# a classe Path traz o diretorio atual com a funcao cwd(), porém ela retorna um PurePath
# por isso, para conseguir concatenar é preciso fazer o cast de str()
# conseguimos manipular a volta de diretorios com o parents[1] (o indice+1 determina quantas posicoes voltam)
caminho_json = str(Path.cwd().parents[1]) + os.sep + 'vendors' + os.sep + 'json' + os.sep
caminho_csv  = str(Path.cwd().parents[1]) + os.sep + 'vendors' + os.sep + 'csv' + os.sep

def teste_vender_pet():
    #Configura
    #dados de entrada
    #virao do arquivo pedido1.json
    #resultados_esperados
    status_code_esperado = 200
    id_pedido_esperado = 7732271
    id_pet_esperado = 777305
    status_pedido_esperado = 'placed'
    #Executa
    resultado_obtido = requests.post(
        url=url +'store/order',
        headers=headers,
        data=open(caminho_json + 'pedido1.json')
    )

    #Valida
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == 200
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == id_pet_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    #Extrai
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    #Realizar a segunda transação
    print(f'==== SEGUNDA TRASACAO ====')
    #Configura
    #Dados de entrada
    #Extraídos da primeira transacao acima

    #Resultado esperado
    pet_name_esperado = 'luki'
    status_code_esperado = 200

    #Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado