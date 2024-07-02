import guiaMatrices as f
Chile = {
1: 'Claudio Bravo',
4: 'Mauricio Isla',
17: 'Gary Medel',
18: 'Gonzalo Jaro',
15: 'Jean Beausejour',
8: 'Arturo Vidal',
21: 'Marcelo Díaz',
20: 'Charles Aranguiz',
6: 'José Pedro Fuenzalida',
7: 'Alexis Sánchez',
11: 'Eduardo Vargas'
}
Argentina = {
1: 'Sergio Romero',
4: 'Gabriel Mercado',
17: 'Nicolás Otamendi',
13: 'Ramiro Funes Mori',
16: 'Marcos Rojo',
6: 'Lucas Biglia',
14: 'Javier Mascherano',
19: 'Éver Banega',
10: 'Lionel Messi',
9: 'Gonzalo Higuaín',
7: 'Ángel Di María'
}


while True:
    print('1.- Buscar por número y país')
    print('2.- Buscar por nombre y país')
    print('3.- Buscar por número en ambos equipos')
    print('4.- Eliminar un jugador del diccionario')
    print('5.- Salir')   
    op = input('Ingrese opción: ') 
    if op == '1':
        pais = int(input('Ingrese país [1: Chile - 2: Argentina]: '))
        camiseta = int(input('Ingrese N° de camiseta: '))
        if pais == 1:
            f.imprimeJugador(camiseta, Chile, 'Chile')
        else:
            f.imprimeJugador(camiseta, Argentina, 'Argentina')
    elif op == '2':
        pais = int(input('Ingrese país [1: Chile - 2: Argentina]: '))
        nombre = input('Ingrese Nombre: ')
        if pais == 1:
            f.imprimeCamiseta(Chile, nombre)
        else:
            f.imprimeCamiseta(Argentina, nombre)
    elif op == '3':
        f.imprimeJugadores(int(input('Ingrese N° de camiseta: ')),Chile,Argentina)
    elif op == '4':
        f.eliminaJugador(input('Ingrese Nombre: '),Chile,Argentina)
    elif op == '5':
        break