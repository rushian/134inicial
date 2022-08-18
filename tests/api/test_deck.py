# variaveis publicas
import json

import requests

url = 'http://deckofcardsapi.com/api/deck/'


# para os creates, normalmente temos o resultado esperado a partir do response de retorno
def test_criar_novo_deck():
    # configura
    sucesso_esperado = True
    remaining_esperado = 52
    shuffled_esperado = False

    # executa
    resultado_obtido = requests.post(
        url=url + 'new/'
    )

    # valida
    # valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))

    dicionario = {
                "deckId": corpo_do_resultado_obtido['deck_id'],
                "remain": corpo_do_resultado_obtido['remaining']
                }
    json_object = json.dumps(dicionario, indent=4)
    with open("../../vendors/json/deck.json", "w") as outfile: outfile.write(json_object)
    assert corpo_do_resultado_obtido['success'] == sucesso_esperado
    assert corpo_do_resultado_obtido['remaining'] == remaining_esperado
    assert corpo_do_resultado_obtido['shuffled'] == shuffled_esperado

def test_pegar_carta():
    #configura
    with open('../../vendors/json/deck.json', 'r') as openfile:
        json_object = json.load(openfile)

    #print(f'\njson_lido: \n', json_object)
    qtd_cartas = 3
    sucesso_esperado = True

    print('\n' , json_object['remain'])
'''
    remaining_esperado = json_object['remain'] - qtd_cartas

    #executa
    resultado_obtido = requests.post(
        url=url + json_object['deckId'] + '/draw/?count=' + str(qtd_cartas)
    )

    #valida
    print(f'\nResultado obtido: ', resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    # print(f'\nCorpo do resultado obtido: \n', corpo_do_resultado_obtido)
    print(f'\nCorpo do resultado obtido: \n', json.dumps(corpo_do_resultado_obtido, indent=4))

    assert corpo_do_resultado_obtido['success'] == sucesso_esperado
    assert corpo_do_resultado_obtido['remaining'] == remaining_esperado
'''