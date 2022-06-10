import os
import shutil


# import sys
# sys.dont_write_bytecode = False
# sys.pycache_prefix = None


def limpar_cache(pasta_projeto):
    pastas_deletadas = 0

    for diretorio, subpastas, arquivos in os.walk(pasta_projeto):
        for subpasta in subpastas:
            if 'pytest_cache' in subpasta:
                pastas_deletadas += 1
                shutil.rmtree(os.path.join(diretorio, subpasta), ignore_errors=True)

    return pastas_deletadas


def test_limpar_cache():
    # configura
    pasta_projeto = 'E:\\dev\\pyCharm\\134inicial'
    pastas_cache = 0
    for diretorio, subpastas, arquivos in os.walk(pasta_projeto):
        for subpasta in subpastas:
            if 'pytest_cache' in subpasta:
                pastas_cache += 1
    resultado_esperado = pastas_cache
    # executa
    resultado_obtido = limpar_cache(pasta_projeto)
    # verifica

    assert resultado_obtido == resultado_esperado
