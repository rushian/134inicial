# bibliotecas
import json

import pytest
import requests
from tests.utils.file_manager import ler_csv
# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definicoes de funcoes (defs)
def teste_incluir_pet():
    # configura
    #    Dados de entrada via pet1.json
    # resultado esperado
    status_code_esperado = 200
    pet_id_esperado = 777305
    pet_nome_esperado = "luki"
    pet_categoria_esperada = "dog"
    pet_tag_esperada = "vacinado"

    # executa
    resultado_obtido = requests.post(

        url=url,
        headers=headers,
        data=open('E:\\dev\\pyCharm\\134inicial\\vendors\\json\\pet1.json')
    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=3))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_esperada
    assert corpo_do_resultado_obtido['tags'][1]['name'] == pet_tag_esperada


def teste_consultar_pet():
    # configura
    # Dados de entrada via pet1.json
    # entrada
    pet_id = 777305
    # resultado esperado
    status_code_esperado = 200
    pet_id_esperado = 777305
    pet_nome_esperado = "luki"
    pet_categoria_esperada = "dog"
    pet_tag_esperada = "medio porte"

    # executa
    resultado_obtido = requests.get(
        url=url + '/' + str(pet_id),
        headers=headers
    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=3))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_esperada
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperada


def teste_alterar_pet():
    # configura
    # Dados de entrada via pet1.json
    # entrada

    # resultado esperado
    status_code_esperado = 200
    pet_id_esperado = 777305
    pet_nome_esperado = "luki"
    pet_categoria_esperada = "dog"
    pet_tag_esperada = "medio porte"
    pet_status_esperado = "pending"

    # executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('E:\\dev\\pyCharm\\134inicial\\vendors\\json\\pet2.json')
    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=3))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_esperada
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperada
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado

def teste_excluir_pet():
    #configura
    #   dados de entrada
    pet_id = 777305
    #   resultado esperado
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    messagem_esperada = '777305'

    #executa
    resultado_obtido = requests.delete(
        url=url + '/' + str(pet_id),
        headers=headers

    )

    #valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=3))
    assert corpo_do_resultado_obtido['code'] == status_code_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == messagem_esperada

@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
                         ler_csv('E:\\dev\\pyCharm\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))

def teste_incluir_pet_em_massa(pet_id,category_id,category_name,pet_name,tags_id,tags_name,status):
    # 1. Configura
    # 1.1 Dados de entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pets.csv
    # 1.1.1 Montagem do JSON dinamico
    corpo_json =  '{'
    corpo_json += f'"id":  "{ pet_id }" ,'
    corpo_json += '"category": {'
    corpo_json += f'"id":  "{ category_id }",'
    corpo_json += f'"name": "{ category_name }"'
    corpo_json += ' },'
    corpo_json += f'"name":  "{ pet_name}" ,'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    corpo_json += '"tags": ['
    corpo_json += '{'
    corpo_json += f'"id":  "{tags_id }",'
    corpo_json += f'"name":  "{tags_name}"'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'"status":  "{ status}"'
    corpo_json += '}'


    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200


    #Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )


    #Valida

    print(f'\nCORPO: ', corpo_json)
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=3))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name



