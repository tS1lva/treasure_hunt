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

    linha1 = [wall,wall,wall,wall,wall,wall,wall]
    linha2 = [wall,user,dot,dot,dot,dot,wall]
    linha3 = [wall,dot,wall,dot,wall,wall,wall]
    linha4 = [wall,dot,dot,dot,wall,dot,wall]
    linha5 = [wall,dot,wall,wall,wall,dot,wall]
    linha6 = [wall,dot,dot,treasure,dot,dot,wall]
    linha7 = [wall,wall,wall,wall,wall,wall,wall]

    mapa = [linha1,linha2,linha3,linha4,linha5,linha6,linha7]

    printMapa(mapa)

