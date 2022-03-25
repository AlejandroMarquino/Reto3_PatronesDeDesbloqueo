panelDesbloqueo = { # defino un diccionario de diccionarios asociando las posiciones de casilla con las letras.
    "A": {
        "punto" : "A",
        "fila" : 1,
        "columna" : 1,
        "usado" : False
    },
    "B": {
        "punto" : "B",
        "fila" : 1,
        "columna" : 2,
        "usado" : False
    },
    "C": {
        "punto" : "C",
        "fila" : 1,
        "columna" : 3,
        "usado" : False
    },
    "D": {
        "punto" : "D",
        "fila" : 2,
        "columna" : 1,
        "usado" : False
    },
    "E": {
        "punto" : "E",
        "fila" : 2,
        "columna" : 2,
        "usado" : False
    },
    "F": {
        "punto" : "F",
        "fila" : 2,
        "columna" : 3,
        "usado" : False
    },
    "G": {
        "punto" : "G",
        "fila" : 3,
        "columna" : 1,
        "usado" : False
    },
    "H": {
        "punto" : "H",
        "fila" : 3,
        "columna" : 2,
        "usado" : False
    },
    "I": {
        "punto" : "I",
        "fila" : 3,
        "columna" : 3,
        "usado" : False
    },
}

combinaciones = 0

inicioValido = False
while inicioValido == False:
    inicio = input("Introduzca el punto de partida [A-I]:\n").upper()
    if inicio in ["A","B","C","D","E","F","G","H","I"]:
        inicioValido = True

inicioValido = False
while inicioValido == False:
    numeroUniones = int(input("Introduzca el número máximo de puntos conectados [1-9]:\n"))
    if numeroUniones in range(1,10):
        inicioValido = True

dedo = panelDesbloqueo[inicio] # dedo de usuario
dedo["usado"] = True

def excepciones(dedo,punto,panelDesbloqueo):
    if dedo['punto'] == "A":
        if punto == "C":
            if panelDesbloqueo['B']['usado'] == True:
                return False
        if punto == "G":
            if panelDesbloqueo['D']['usado'] == True:
                return False
        if punto == "I":
            if panelDesbloqueo['E']['usado'] == True:
                return False   
    if dedo['punto'] == "C":
        if punto == "A":
            if panelDesbloqueo['B']['usado'] == True:
                return False
        if punto == "I":
            if panelDesbloqueo['F']['usado'] == True:
                return False
        if punto == "G":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "G":
        if punto == "A":
            if panelDesbloqueo['D']['usado'] == True:
                return False
        if punto == "I":
            if panelDesbloqueo['H']['usado'] == True:
                return False
        if punto == "C":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "I":
        if punto == "C":
            if panelDesbloqueo['F']['usado'] == True:
                return False
        if punto == "G":
            if panelDesbloqueo['H']['usado'] == True:
                return False
        if punto == "A":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "B":  
        if punto == "H":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "D":  
        if punto == "F":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "F":  
        if punto == "D":
            if panelDesbloqueo['E']['usado'] == True:
                return False
    if dedo['punto'] == "H":  
        if punto == "B":
            if panelDesbloqueo['E']['usado'] == True:
                return False
            
def moverDedo(panelDesbloqueo,dedo,combinaciones,numeroUniones): # Empieza la recursividad, la funcion se llama a si misma.
    if numeroUniones != 0:
        numeroUniones = numeroUniones + 1
        moverDedo(panelDesbloqueo,dedo,combinaciones,numeroUniones)
    else:
        for punto in panelDesbloqueo.copy():    
            if panelDesbloqueo[punto]["usado"] == False:
                if not excepciones(dedo,punto,panelDesbloqueo):
                    dedo = panelDesbloqueo[punto]
                    dedo["usado"] = True
                    combinaciones += 1
    
# Cada vez que realiza un movimiento almacena en memoria un panel nuevo, una copia del anterior y vuelve a empezar desde esa copia para tener
# en consideración los puntos ya utilizados anteriorimente.

moverDedo(panelDesbloqueo,dedo,combinaciones,numeroUniones)

print(combinaciones)