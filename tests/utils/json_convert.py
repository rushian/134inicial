import json
import os
import re
import pyperclip


def converte_json(arquivo_json):
    print('\nAbrindo arquivo ', arquivo_json)
    dados_do_arquivo = json.load(open(arquivo_json))
    # dados_do_arquivo = json.loads(open(arquivo_json).read())

    chaves_alteradas = [(0, 'raiz', 'id', 'pet_id'),
                        (1, 'category', 'id', 'category_id'),
                        (1, 'category', 'name', 'category_name'),
                        (0, 'raiz', 'name', 'pet_name'),
                        (2, 'tags', 'id', 'tags_id'),
                        (2, 'tags', 'name', 'tags_name'),
                        (0, 'raiz', 'status', 'status')]

    info_por_item = len(chaves_alteradas[0])
    print('\n tamanho da lista: ', len(chaves_alteradas), 'informacoes por item: ', info_por_item)
    for i in range(0, len(chaves_alteradas)):
        # print('idx atual :', i)
        for j in range(info_por_item):
            # print('chave atual :', i, j, chaves_alteradas[i][j])
            if chaves_alteradas[i][0] == 0:
                dados_do_arquivo[chaves_alteradas[i][2]] = '{' + chaves_alteradas[i][3] + '}'
            if chaves_alteradas[i][0] == 1:
                dados_do_arquivo[chaves_alteradas[i][1]][chaves_alteradas[i][2]] = '{' + chaves_alteradas[i][3] + '}'
            if chaves_alteradas[i][0] == 2:
                for k in range(len(dados_do_arquivo[chaves_alteradas[i][1]])):
                    dados_do_arquivo[chaves_alteradas[i][1]][k][chaves_alteradas[i][2]] = '{' + \
                                                                                          chaves_alteradas[i][3] + '}'

    dados_em_json = json.dumps(dados_do_arquivo, indent=4)
    # iniciar o corpo_json com a chave de abertura utilizando regex
    dados_em_json = re.sub("^", "\tcorpo_json = '", dados_em_json)
    # adicionar a chave de fechamento ao corpo_json utilizando regex
    dados_em_json = re.sub("$", "'", dados_em_json)
    # adcionar todas as demais linhas ao corpo_json e fechar aspas simples de cada linha utilizando regex
    dados_em_json = re.sub("\n", "'\n\tcorpo_json += '", dados_em_json)
    # adicionar fancy com regex
    dados_em_json = re.sub("(\'\s+\"\w+\":\s*\"\{\w+})", "f\g<1>", dados_em_json)

    # copiar conteudo do json para area de transferencia
    pyperclip.copy(dados_em_json)

    print('\n', dados_em_json, '\n\n DADOS COPIADOS PARA AREA DE TRANSFERENCIA!')


def test_convert_json():
    converte_json(f'E:{os.sep}dev{os.sep}pyCharm{os.sep}134inicial{os.sep}vendors{os.sep}json{os.sep}pet2.json')
