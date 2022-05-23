# bibliotecas
import json
import os
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
        data=open('/vendors\\json\\pet1.json')
    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
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
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
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
        data=open('/vendors\\json\\pet2.json')
    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_categoria_esperada
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperada
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado


def teste_excluir_pet():
    # configura
    #   dados de entrada
    pet_id = 777305
    #   resultado esperado
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    messagem_esperada = '777305'

    # executa
    resultado_obtido = requests.delete(
        url=url + '/' + str(pet_id),
        headers=headers

    )

    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
    assert corpo_do_resultado_obtido['code'] == status_code_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == messagem_esperada


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
                         ler_csv('E:\\dev\\pyCharm\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))
def teste_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    # 1. Configura
    # 1.1 Dados de entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pets.csv
    # 1.1.1 Montagem do JSON dinamico
    corpo_json = '{'
    corpo_json += f'"id":  "{pet_id}" ,'
    corpo_json += '"category": {'
    corpo_json += f'"id":  "{category_id}",'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += ' },'
    corpo_json += f'"name":  "{pet_name}" ,'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    corpo_json += '"tags": ['
    corpo_json += '{'
    corpo_json += f'"id":  "{tags_id}",'
    corpo_json += f'"name":  "{tags_name}"'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'"status":  "{status}"'
    corpo_json += '}'

    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # Valida
    print(f'\nCORPO: \n', json.dumps(corpo_json, indent=4))
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name

#comando para determinar diretorio onde inicial a referencia de caminho relativo
os.chdir(f'E:{os.sep}dev{os.sep}pyCharm{os.sep}134inicial{os.sep}')
#lita utilizando o separador do sistema para caminho relativo
@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status',
                         ler_csv(f'vendors{os.sep}csv{os.sep}massa_incluir_pet_multitags.csv'))
def teste_incluir_pet_em_massa_com_multiplas_tags(pet_id, category_id, category_name, pet_name, tags, status):
    # 1. Configura
    # 1.1 Dados de entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pets.csv
    # 1.1.1 Montagem do JSON dinamico
    global itens_lista
    corpo_json = '{'
    corpo_json += f'"id":  "{pet_id}" ,'
    corpo_json += '"category": {'
    corpo_json += f'"id":  "{category_id}",'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += ' },'
    corpo_json += f'"name":  "{pet_name}" ,'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    # 1.1.1.1 iteração das possiveis tags doo animal
    lista_tags = tags
    json_tag = '"tags": ['
    sub_lista_tags = []
    qtd_tags = lista_tags.count(';') + 1
    # quando for mais de uma tag, os valores devem ser separados no csv por ';'
    if lista_tags.count(';') > 0:
        lista_tags = lista_tags.split(';')
        qtd_el = len(lista_tags)
        print('Quantidade de elementos' + str(qtd_el))

        for i in range(0, qtd_el):
            # Create an index range for l of n items:
            sub_lista_tags.append(lista_tags[i].split(','))
        itens_lista = len(sub_lista_tags)
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for contador in range(0, itens_lista):
            if contador < itens_lista - 1:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"},'
            else:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"}'
    # 1.1.1.2 Quando há somente 1 tag, não é necessário usar o looping do FOR
    else:
        lista_tags = lista_tags.split(',')
        json_tag += '{"id":' + lista_tags[0] + ',"name":"' + lista_tags[1] + '"}'
        # print(f'\nExiste 1 tag na lista {lista_tags}')
    json_tag += '],'
    # 1.1.2 Continuando a montagem do Json, com adicao das tags
    corpo_json += json_tag
    corpo_json += f'"status":  "{status}"'
    corpo_json += '}'
    # print(corpo_json)

    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # Valida
    mostrar_corpo_json = json.loads(corpo_json)
    print(f'\n==== CORPO ENVIADO ====')
    print(json.dumps(mostrar_corpo_json, indent=4))
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    # asserts dinamicos de acordo com as tags existeentes para um pet
    if qtd_tags > 1:
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for i in range(0, qtd_tags):
            for j in range(2):
                assert corpo_do_resultado_obtido['tags'][i]['name'] == sub_lista_tags[i][1]
    else:
        # print(f'\nExiste 1 tag na lista {lista_tags}')
        assert corpo_do_resultado_obtido['tags'][0]['name'] == lista_tags[1]

