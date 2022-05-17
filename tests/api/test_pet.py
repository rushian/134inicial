#bibliotecas
import json

import pytest
import requests

#variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type':'application/json'}

#definicoes de funcoes (defs)


def teste_incluir_pet():
    # configura
    #Dados de entrada via pet1.json
    #resultado esperado
    status_code_esperado = 200
    pet_id_esperado = 771305
    pet_nome_esperado = "luki"
    pet_categoria_esperada = "dog"
    pet_tag_esperada = "vacinado"


    # executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('E:\\dev\\pyCharm\\134inicial\\vendors\\json\\pet1.json')
        )


    #valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    #print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_esperada
    assert corpo_do_resultado_obtido['tags'][1]['name'] == pet_tag_esperada
