import os
import shutil
from pathlib import Path


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
    pasta_projeto = str(Path.cwd().parents[1])
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
