# ToDo 3: Criar uma venda de um pet para um usuario
# ToDo 4: Consultar dados do animal vendido
import json

import requests

url = 'https://petstore.swagger.io/v2/store'
headers = {'Content-Type': 'application/json'}

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
        url=url,
        headers=headers,
        data=open('vendors/json/pedido1.json')
    )

    #Valida
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == 200
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == id_pet_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado