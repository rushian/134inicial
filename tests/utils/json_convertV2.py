# done ToDo 1: Fazer a leitura do json pra gerar a tupla de chaves alteraveis
# done ToDo 2: Verificar se o json e valido
import json
import os
import re
import pyperclip
import self as self
from operator import length_hint


def converte_json(arquivo_json):
    print('\nAbrindo arquivo ', arquivo_json)
    try:
        dados_do_arquivo = json.load(open(arquivo_json))

        # print('\n item do dicionario ', dados_do_arquivo.items())
        # print('\n chaves do dicionario ', dados_do_arquivo.keys())
        # print('\n valores do dicionario ', dados_do_arquivo.values())

        for keys, values in dados_do_arquivo.items():
            # print(type(values))
            if isinstance(values, list) and isinstance(values[0], dict):
                for i in range(0, length_hint(values)):
                    for k, v in values[i].items():
                        values[i][k] = '{' + keys + '_' + k + str(i + 1) + '}'
            elif isinstance(values, list):
                itens = []
                for i in range(0, length_hint(values)):
                    itens.append('{' + keys + str(i + 1) + '}')
                    dados_do_arquivo[keys] = itens
            elif isinstance(values, dict):
                for k, v in values.items():
                    dados_do_arquivo[keys][k] = '{' + keys + '_' + k + '}'
            else:
                dados_do_arquivo[keys] = '{' + keys + '}'

        dados_em_json = json.dumps(dados_do_arquivo, indent=4)
        # iniciar o corpo_json com a chave de abertura utilizando regex
        dados_em_json = re.sub("^", "\tcorpo_json = '", dados_em_json)
        # adicionar a chave de fechamento ao corpo_json utilizando regex
        dados_em_json = re.sub("$", "'", dados_em_json)
        # adcionar todas as demais linhas ao corpo_json e fechar aspas simples de cada linha utilizando regex
        dados_em_json = re.sub("\n", "'\n\tcorpo_json += '", dados_em_json)
        # adicionar fancy com regex nas linhas nao-lista
        dados_em_json = re.sub("(\'\s+\"\w+\":\s*\"\{\w+})", "f\g<1>", dados_em_json)
        # adicionar fancy com regex nas linhas de lista
        dados_em_json = re.sub("(\'\s+\"\{\w+\}\")", "f\g<1>", dados_em_json)

        # copiar conteudo do json para area de transferencia
        pyperclip.copy(dados_em_json)
        print('\n', dados_em_json, '\n\n DADOS COPIADOS PARA AREA DE TRANSFERENCIA!')

    except ValueError as e:
        print("JSON FORNECIDO NAO E VALIDO, VERIFIQUE A ESTRUTURA DO ARQUIVO")


def test_convert_json():
    # comando para determinar diretorio onde inicia a referencia de caminho relativo
    os.chdir(f'E:{os.sep}dev{os.sep}pyCharm{os.sep}134inicial{os.sep}')
    converte_json(f'vendors{os.sep}json{os.sep}pet1.json')
