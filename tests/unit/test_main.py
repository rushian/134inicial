from main import somar, subtrair, multiplicar, dividir

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
