'''
1. Dados los diccionarios siguientes donde las llaves son números de camiseta y el valor
los nombres de los jugadores:

Realice lo siguiente:
A. Haga un programa que permita escribir por teclado un equipo (Chile o Argentina),
un número de camiseta y entregue el nombre del jugador. Considere el caso en el cual
el número entregado por teclado no exista.
B. Haga un programa que permita ingresar el nombre de un jugador y un equipo, y
entregue el número de camiseta de ese jugador. Si el nombre no existe, debe entregar
un mensaje diciendo: “jugador no existe”
C. Haga un programa que permita ingresar por teclado un número de camiseta y
entregue los jugadores (de ambos equipos si fuese el caso) que usan ese número.
D. Haga un programa que permita ingresar el nombre de un jugador y elimine ese
jugador del diccionario. Note que no se ingresa por teclado el equipo (debe buscar el
nombre en ambos diccionarios). Si el nombre del jugador no existe, entonces debe
entregar un mensaje diciendo: “jugador no existe”
'''
def imprimeJugador(nroCamiseta, diccionario, nombrePais):
    if nroCamiseta in diccionario:
        print(diccionario[nroCamiseta])   
    else:
        print('No hay jugador con ese Número en', nombrePais) 

def imprimeCamiseta(diccionario, nom):
    encontrado = False
    for camiseta, nombre in diccionario.items():
        if nombre.upper() == nom.upper():
            encontrado = True
            print(f'El jugador {nom} usa la camiseta {camiseta}')
    if not encontrado:
        print('Jugador No encontrado')    

def imprimeJugadores(nroCamiseta,dChile, dArgentina):
    existe = False
    if nroCamiseta in dChile:
        existe = True
        print('Chile:',dChile[nroCamiseta])   
    if nroCamiseta in dArgentina:
        existe = True
        print('Argentina:',dArgentina[nroCamiseta])  
    if not existe:
        print('No hay jugadores con esa camiseta ni en Chile ni en Argentina')

def eliminaJugador(nom,dChile, dArgentina):
    encontrado = False
    for vez in range(2):
        if vez == 0:
            diccionario = dChile
        else:
            diccionario = dArgentina
        for camiseta, nombre in diccionario.items():
            if nombre.upper() == nom.upper():
                encontrado = True
                clave = camiseta
                break
        if encontrado:
            diccionario.pop(clave)
            print('Diccionario Modificado!!')
            print(diccionario)
            break
    if not encontrado:
        print('No existe el jugador')


    