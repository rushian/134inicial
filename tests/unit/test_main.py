import csv
import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as falha:
        print(f'Ocorreu uma falha: {falha}')


def teste_somar():
    # 1 - Configura
    num_a = 85
    num_b = 8
    resultado_esperado = 93
    # 2 - Executa
    resultado_obtido = somar(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_subtrair():
    # 1 - Configura
    num_a = 5
    num_b = 8
    resultado_esperado = -3
    # 2 - Executa
    resultado_obtido = subtrair(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_multiplicar():
    # 1 - Configura
    num_a = 2
    num_b = 9
    resultado_esperado = 18
    # 2 - Executa
    resultado_obtido = multiplicar(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_dividir_positivo():
    # 1 - Configura
    num_a = 18
    num_b = 2

    resultado_esperado = 9
    # 2 - Executa
    resultado_obtido = dividir(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    # 1 - Configura
    num_a = 18
    num_b = 0

    resultado_esperado = 'quociente zero nao gera resultado'
    # 2 - Executa
    resultado_obtido = dividir(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


# lista para uso como massa de teste, conhecido como tupla
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura

    # variaveis pelos parametros

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',
                         ler_csv('E:\\dev\pyCharm\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura

    # variaveis pelos parametros

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))
    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',
                         ler_csv('E:\\dev\pyCharm\\134inicial\\vendors\\csv\\massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # Configurado por parametrizacao do csv
    # 2 - Executa
    resultado_obtido = subtrair(int(numero_a), int(numero_b))
    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)
