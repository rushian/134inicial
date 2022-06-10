import os
from pathlib import Path

def test_caminho():
    print('\n' + os.getcwd())
    print(os.path.abspath(__file__ + os.sep + ".." + os.sep + ".." + os.sep + ".." + os.sep) )
    print('root: ' + str(Path.cwd().root))
    print(str(Path.cwd().parent))
    print(str(Path.cwd().parents[1]))

    os.chdir(Path.cwd().parents[1])
    print(os.getcwd())


