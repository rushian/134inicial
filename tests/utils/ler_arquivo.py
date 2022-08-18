
def test_arquivo():
    content_variable = open ( r'E:\dev\pyCharm\134inicial\vendors\csv\massa_incluir_pet.csv' , "r" )
    file_lines = content_variable.readlines()
    content_variable.close()
    last_line = file_lines[len(file_lines) - 1]
    print ('\n'+ last_line)
