visited = []
user_coord = [1,1]

def printMapa(mapa):
    for i in range(len(mapa)):
        for j in range (len(mapa[i])):
            print(mapa[i][j], end="")
        print("")

def return_up(mapa, i, j):
    return mapa[i-1][j] == "." or mapa[i-1][j] == "T"

def return_down(mapa, i, j):
    return mapa[i+1][j] == "." or mapa[i+1][j] == "T"

def return_right(mapa, i, j):
    return mapa[i][j+1] == "." or mapa[i][j+1] == "T"

def return_left(mapa, i, j):
    return mapa[i][j-1] == "." or mapa[i][j-1] == "T"

def find_user(mapa):
    #LOGICA PARA ACHAR OS INDICES DO USER (I E J)
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "S":
                start = (i, j)
                return start

    return "user not found"

def find_treasure(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "T":
                return (i, j)
    return "treasure note found"

def walk(mapa, user_coord):

    treasure_position = find_treasure(mapa)
    steps = 0

    while user_coord != treasure_position: 

        old_coord = user_coord
        
        if return_down(mapa, user_coord[0], user_coord[1]):
            user_coord = (user_coord[0] + 1, user_coord[1])

        elif return_right(mapa, user_coord[0], user_coord[1]):
            user_coord = (user_coord[0], user_coord[1] + 1)

        elif return_left(mapa, user_coord[0], user_coord[1]):
            user_coord = (user_coord[0], user_coord[1] - 1)

        elif return_up(mapa, user_coord[0], user_coord[1]):
            user_coord = (user_coord[0] - 1, user_coord[1])

        visited.append(user_coord) # coloca na lista de posições percorridas

        if user_coord != treasure_position:
            mapa[old_coord[0]][old_coord[1]] = "."
            mapa[user_coord[0]][user_coord[1]] = "S"

        else:
            mapa[old_coord[0]][old_coord[1]] = "."  # Último passo antes de parar
            mapa[user_coord[0]][user_coord[1]] = "S"

        steps += 1

        print(f"\nPasso {steps}: Nova posição do usuário {user_coord}\n")
        printMapa(mapa)

    return user_coord

# Chamando a função e atualizando a coordenada
def returnCoord(mapa, i, j):
    return mapa[i][j]