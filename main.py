import pytest


def teste_aprendizado():
    json_tag = '"tags": ['
    lista = [['71', 'vacinado'], ['72', 'pequeno porte'], ['73', 'castrado']]
    itens_lista = len(lista)
    print(f'\nExistem  {itens_lista} tags na {lista}')
    for contador in range(1, itens_lista):
        if contador != itens_lista:
            json_tag += '{"id":' + lista[contador][0] + ',"name":"' + lista[contador][1] + '"},'
        else:
            json_tag += '{"id":' + lista[contador][0] + '"name":"' + lista[contador][1] + '"}'
    json_tag += ']'
    print(json_tag)


def teste_aprendizado1():
    lista_tags = "73,castrado"
    #lista_tags = "71, vacinado;72,pequeno porte;73,castrado"

    #lista_tags = lista_tags.split(';')
    json_tag1 = '"tags": ['
    sub_lista_tags = []
    if lista_tags.count(';') > 0:
        lista_tags = lista_tags.split(';')
        qtd_el = len(lista_tags)
        print('Quantidade de elementos' + str(qtd_el))

        for i in range(0, qtd_el):
            # Create an index range for l of n items:
            sub_lista_tags.append(lista_tags[i].split(','))
        itens_lista1 = len(sub_lista_tags)
        print(f'\nExistem  {itens_lista1} tags na lista {sub_lista_tags}')
        for contador1 in range(0, itens_lista1):
            if contador1 < itens_lista1 - 1:
                json_tag1 += '{"id":' + sub_lista_tags[contador1][0] + ',"name":"' + sub_lista_tags[contador1][1] + '"},'
            else:
                json_tag1 += '{"id":' + sub_lista_tags[contador1][0] + ',"name":"' + sub_lista_tags[contador1][1] + '"}'
    else:
        lista_tags = lista_tags.split(',')
        json_tag1 += '{"id":' + lista_tags[0] + ',"name":"' + lista_tags[1] + '"}'

    json_tag1 += ']'
    print('\n', json_tag1)



def teste_create_sublists_alt():
    big_list = "71, vacinado;72,pequeno porte;73,castrado".split(';')
    qty_el = len(big_list)
    sub_lista_tags = []
    for i in range(0, qty_el):
        # Create an index range for l of n items:
        sub_lista_tags.append(big_list[i].split(','))


    print(f'\n {sub_lista_tags}')


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
