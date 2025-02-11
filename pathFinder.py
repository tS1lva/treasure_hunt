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
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "S":
                start = (i, j)
                return start


    return "user not found"

def walk(mapa, user_coord):
    # Lógica para andar
    if return_right(mapa, user_coord[0], user_coord[1]):
        return (user_coord[0], user_coord[1] + 1)
    return user_coord  # Retorna a mesma coordenada se não puder andar

# Chamando a função e atualizando a coordenada


def returnCoord(mapa, i, j):
    return mapa[i][j]