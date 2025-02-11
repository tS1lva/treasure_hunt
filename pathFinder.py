visited = []
steps = 0

def return_up(mapa, i, j):
    return mapa[i-1][j] == "."

def return_down(mapa, i, j):
    return mapa[i+1][j] == "."

def return_right(mapa, i, j):
    return mapa[i][j+1] == "."

def return_left(mapa, i, j):
    return mapa[i][j-1] == "."

def find_user(mapa):
    #LOGICA PARA ACHAR OS INDICES DO USER (I E J)
    #USAR VARIAVEL GLOBAL PARA ATUALIZAR A POSIÇÃO DO USUARIO
    print("")

def walk(mapa):
    #LOGICA PARA ANDAR
    print("")