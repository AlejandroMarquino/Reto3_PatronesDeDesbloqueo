panelDesbloqueo = {
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

print(panelDesbloqueo["B"])
print(panelDesbloqueo["I"]["usado"])
print(panelDesbloqueo["C"]["fila"])
print(panelDesbloqueo["H"]["columna"])


initValid = False

while initValid == False:
    init = input("Introduzca el Punto de partida:\n").upper()
    if init in ["A","B","C","D","E","F","G","H","I"]:
        initValid = True

inicio=panelDesbloqueo[init]
inicio["usado"] = True

print(inicio['punto'])

for punto in panelDesbloqueo.copy():    
    print(punto['punto'])