import pytest


def imprimir_oi(nome):
    print(f'Olá, {nome}. Bem vindo ao python.')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'quociente zero nao gera resultado'


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
    print('4. Divisão')
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
            case '4':
                oper = '/'
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
                case '4':
                    resultado = dividir(n_a, n_b)

            print(f'{n_a} {oper} {n_b} = {resultado}')
            # limpando oper pro caso de enviarem vazio no numero da operacao
            oper = ''
