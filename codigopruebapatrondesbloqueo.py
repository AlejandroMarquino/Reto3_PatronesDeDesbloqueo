PUNTOS = 10 #aunque sea una matriz 3x3, hay 10 puntos porque podríamos no seleccionar ninguno y sería una opción.

#Localizar el punto de inicio.
def patronDesbloqueo(usado, skip, noUsado, seleccionado):
    if (seleccionado <= 0):
        # si es el último punto vuelve al primero (creo)
        if (seleccionado == 0):
            return 1
        else:
            return 0
    ways = 0

    # si no ha sido usada, que se use en la próxima vuelta
    usado[noUsado] = True

    # La movida de los puntos, si ese punto no ha sido visitado y cualquier "i" está al lado, entonces
    # salta un punto o vuelve a un punto que ya has visitado para pasarlo por encima.
    for i in range(1, PUNTOS):
        if (usado[i] == False and (skip[i][noUsado] == 0 or usado[skip[i][noUsado]])):
            ways += patronDesbloqueo(usado, skip, i, seleccionado - 1)

    # que este punto no sea visitado en ninguna vuelta más, lo contrario de la línea 15 vaya.
    usado[noUsado] = False

    return ways


# funcion que devuelve el número de patrones con un mínimo m de conexiones y un máximo n de conexiones
def numeroPatrones(m, n):
    salta = [[0 for i in range(PUNTOS)] for j in range(PUNTOS)]

    # las siguientes líneas son las que tengo apuntadas en la pizarra.
    salta[1][3] = salta[3][1] = 2
    salta[7][9] = salta[9][7] = 8
    salta[1][7] = salta[7][1] = 4
    salta[3][9] = salta[9][3] = 6
    salta[1][9] = salta[9][1] = salta[2][8] = salta[8][2] = 7
    salta[3][7] = salta[7][3] = salta[4][6] = salta[6][4] = 5

    visto = [False] * PUNTOS
    rutas = 0
    for i in range(m, n + 1):
        # los números de las esquinas, 1, 3, 7, 9
        rutas += 4 * patronDesbloqueo(visto, salta, 1, i - 1)

        # los numeros de los laterales 2, 4, 6, 8
        rutas += 4 * patronDesbloqueo(visto, salta, 2, i - 1)

        # el 5 que está en medio
        rutas += patronDesbloqueo(visto, salta, 5, i - 1)

    return rutas


if __name__ == '__main__':
  minimo = input("Introduce el mínimo de puntos: ")
  maximo = input("Introduce el maximo de puntos: ")
  minConnect= int(minimo)
  maxConnect= int(maximo)


  print(numeroPatrones(minConnect, maxConnect))
