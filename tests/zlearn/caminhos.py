import os
from pathlib import Path

def test_caminho():
    print('\n' + os.getcwd())
    print(os.path.abspath(__file__ + os.sep + ".." + os.sep + ".." + os.sep + ".." + os.sep) )
    print('root: ' + str(Path.cwd().root))
    print(str(Path.cwd().parent))
    print(str(Path.cwd().parents[1]))
    print(str(Path.cwd().parents[1].joinpath('vendors', 'csv')) + os.sep)
    os.chdir(Path.cwd().parents[1])
    print(str(Path.cwd().joinpath('vendors')))
    print('========= VARRER DIRETORIOS DENTRO DA VENDORS ==========')
    for diretorios, subpastas, arquivos in os.walk(Path.cwd().joinpath('vendors')):

        for subpasta in subpastas:

            for arquivo in arquivos:
                if os.path.isfile(os.path.join(diretorios, arquivo)) and os.path.join(diretorios, arquivo).endswith('json'):
                    print('O arquivo ' + arquivo + ' é um json ')
                elif os.path.isfile(os.path.join(diretorios, arquivo)) and os.path.join(diretorios, arquivo).endswith('csv'):
                    print('O arquivo ' + arquivo + ' é um csv ')
                else:
                    print('O arquivo ' + arquivo + ' nao e json nem csv')
    #-------------------

    print('========= LISTANDO CONteUDO DO prIMEIRO FOR ==========')
    for diretorios, subpastas, arquivos in os.walk(Path.cwd().joinpath('vendors')):
        print('------ diretorios  ------')
        print(diretorios)
        print('------ sub  ------')
        print(subpastas)
        print('------ file  ------')
        print(arquivos)




