opcion = 1
total= 0
cantTratamiento1 = 0
cantTratamiento2 = 0
cantTratamiento3 = 0
while opcion != 3:
    opcionTratamiento = 1  
    print("1) Cotización")
    print("2) Renunciar")
    print("3) Salir")
    while True:
        try:
            opcion = int(input("Eliga la opción que desee: "))
            if opcion == 1 or opcion == 2 or opcion == 3:
                break
            else:
                print("Eliga una de las opciones mostradas.")
        except:
            print("Ingrese valores numéricos.")
    if opcion == 1:
        while opcionTratamiento != 4:
            print("1) Carillas porcelanas $250000")
            print("2) Implantes dentales $475000")
            print("3) Ortodoncia brackets $800000")
            print("4) Salir y calcular cotización")
            while True:
                try:
                    opcionTratamiento = int(input("Ingrese el tratamiento que desee: "))
                    if opcionTratamiento == 1 or opcionTratamiento == 2 or opcionTratamiento == 3 or opcionTratamiento == 4:
                        break
                    else:
                        print("Ingrese una de las opciones mostradas.")
                except:
                    print("Ingrese un valor numérico.")
            if opcionTratamiento == 1:
                total = total + 250000
                cantTratamiento1 += 1
                print("Se añadio el tratamiento 1")
            elif opcionTratamiento == 2:
                total = total + 475000
                cantTratamiento2 += 1
                print("Se añadio el tratamiento 2")
            elif opcionTratamiento == 3:
                total = total + 800000
                cantTratamiento3 += 1
                print("Se añadio el tratamiento 3")
            else:
                while True:
                    print("1) SI")
                    print("2) NO")
                    try:
                        descuento = int(input("¿Posees descuento? "))
                        if descuento == 1 or descuento == 2:
                            break
                        else:
                            print("Eliga una opción válida.")
                    except:
                        print("Ingrese un valor numérico.")
                if descuento == 1:
                    while True:
                        print("1) Trabajador auxiliar: 15% de descuento")
                        print("2) Trabajador administrativo: 10% de descuento")
                        print("3) Trabajador docente: 5% de descuento")
                        try:
                            tipoDescuento = int(input("¿Posees descuento? "))
                            if tipoDescuento == 1 or tipoDescuento == 2 or tipoDescuento == 3:
                                break
                            else:
                                print("Ingrese una opción válida")
                        except:
                            print("Ingrese unv valor numérico.")
                    if tipoDescuento ==1:
                        valorDescuento = 15
                    elif tipoDescuento == 2:
                        valorDescuento = 10
                    else:
                        valorDescuento = 5
                else:
                    valorDescuento = 0
                print("-"*20)
                print("COTIZACION")
                print("-"*20)
                print(f"--> {cantTratamiento1} tratamiento(s) Carillas porcelana ${cantTratamiento1 *250000}")
                print(f"--> {cantTratamiento2} tratamiento(s) Implantes dentales ${cantTratamiento2 *475000}")
                print(f"--> {cantTratamiento3} tratamiento(s) Ortodoncia brackets ${cantTratamiento3 *800000}")
                print("-"*20)
                print(f"Subtotal ${total}")
                print(f"Descuento {valorDescuento}% ${int(total*(valorDescuento/100))}")
                print("-"*20)
                print(f"Total ${int(total-(total*(valorDescuento/100)))}")
                print("-"*20)
                print(f"Son 12 cuotas de: ${round(total/12)}")
                print("")
                print("Sonría bonito!!")
    elif opcion == 2:
        total= 0
        cantTratamiento1 = 0
        cantTratamiento2 = 0
        cantTratamiento3 = 0
        print("Se ha eliminado la cotización anterior. Puede realizar una nueva cotización o salir.")
    else:
        print("Has salido del programa")
    
