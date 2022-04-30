import pytest


def imprimir_oi(nome):
    print(f'Olá, {nome}. Bem vindo ao python.')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

    ### Primeira chamada de metodo ####


if __name__ == '__main__':
    imprimir_oi('Luciano')

    print('Caminho do arquivo', __file__)

    #### Inicio calculadora ####
    oper = ''
    print('#### CALCULADORA ####')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('0. Sair')

    while True:
        operacao = input('Digite o número da operação ou 0 para sair: ')
        match operacao:
            case '1':
                oper = '+'
            case '2':
                oper = '-'
            case '3':
                oper = '*'
            case '0':
                print('Fim da execução')
                break
            case _:
                print('Escolha inválida')

        if oper != '':
            n_a = int(input('Primeiro valor: '))
            n_b = int(input('Segundo valor: '))
            match operacao:
                case '1':
                    resultado = somar(n_a, n_b)
                case '2':
                    resultado = subtrair(n_a, n_b)
                case '3':
                    resultado = multiplicar(n_a, n_b)

            print(f'{n_a} {oper} {n_b} = {resultado}')
            # limpando oper pro caso de enviarem vazio no numero da operacao
            oper = ''


def test_somar():
    # 1 - Configura
    num_a = 85
    num_b = 8
    resultado_esperado = 93
    # 2 - Executa
    resultado_obtido = somar(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_subtrair():
    # 1 - Configura
    num_a = 5
    num_b = 8
    resultado_esperado = -3
    # 2 - Executa
    resultado_obtido = subtrair(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_multiplicar():
    # 1 - Configura
    num_a = 2
    num_b = 9
    resultado_esperado = 18
    # 2 - Executa
    resultado_obtido = multiplicar(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado
