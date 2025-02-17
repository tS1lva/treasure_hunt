import pathFinder

if __name__ == '__main__':
    wall ="#"
    dot = "."
    user = "S"
    treasure = "T"

    mapa = [
        [wall, wall, wall, wall, wall, wall, wall],
        [wall, user, dot, dot, dot, dot, wall],
        [wall, dot, wall, dot, wall, wall, wall],
        [wall, dot, dot, dot, wall, dot, wall],
        [wall, dot, wall, wall, wall, dot, wall],
        [wall, dot, dot, treasure, dot, dot, wall],
        [wall, wall, wall, wall, wall, wall, wall]
    ]

    print("\nPosição do usuário:", pathFinder.find_user(mapa), "\n")
    pathFinder.printMapa(mapa)
    nova_coord = pathFinder.walk(mapa, pathFinder.find_user(mapa))
    print("\nPosição final do usuário:", nova_coord, "\n")
