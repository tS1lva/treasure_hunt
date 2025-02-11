import pathFinder
def printMapa(mapa):
    for i in range(len(mapa)):
        for j in range (len(mapa[i])):
            print(mapa[i][j], end="")
        print("")

if __name__ == '__main__':
    wall ="#"
    dot = "."
    user = "S"
    treasure = "T"

    user_coord = [1,1]

    mapa = [
        [wall, wall, wall, wall, wall, wall, wall],
        [wall, user, dot, dot, dot, dot, wall],
        [wall, dot, wall, dot, wall, wall, wall],
        [wall, dot, dot, dot, wall, dot, wall],
        [wall, dot, wall, wall, wall, dot, wall],
        [wall, dot, dot, treasure, dot, dot, wall],
        [wall, wall, wall, wall, wall, wall, wall]
    ]

    printMapa(mapa)
    print(pathFinder.find_user(mapa))

    user_coord = pathFinder.walk(mapa, user_coord)
    print("nova coord user")
    print(user_coord)

    printMapa(mapa)

