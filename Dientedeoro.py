#validadores de los menús
opcion=0
tratamiento=0
descuento=""
c_carillas=""
#variables de total de los tratamientos
t_carillas=0
t_implantes=0
t_ortodoncia=0
x='*'*50
#Descuentos para aplicar
desc_auxiliar=15
desc_admin=10
desc_docen=5
no_desc=0
#precios de los tratamientos
carillas=250000
implantes=475000
ortodoncia=800000
while opcion!=3:
    
    print(f"{x}")
    print("\tClinica Dental El Diente de Oro")
    print(f"{x}")
    print("1.-Cotización")
    print("2.-Renunciar")
    print("3.-Salir")
    print(f"{x}")

    while True:
        try:
            opcion=int(input("Ingrese la opción que desea: "))
            if 0<opcion<4:
                break
            else:
                print("Valores ingresados invalidos.")
        except ValueError:
            print("Ingrese solo números del 1-3.")
    if opcion==1:
        tratamiento=0
        while tratamiento!=4:
            print(x)
            print("Los tratamientos incluyen:")
            print("-Limpieza y destartraje.")
            print("-Aplicación de sellante.")
            print("-Aplicación de fluor.")
            print("Los tratamientos a ofrecer son:")
            print(f"1.-Carillas porcelana\t {carillas}")
            print(f"2.-Implantes dentales\t {implantes}")
            print(f"3.-Ortodoncia Brakets\t {ortodoncia}")
            print(f"4.-Salir")
            print(x)
            while True:
                try:
                    tratamiento=int(input("Ingrese el tratamiento que desea: "))
                    if 0<tratamiento<5:
                        break
                    else:
                        print("Valores del 1-4.")
                except:
                    print("Ingrese solo números del 1-4")
            #Se consulta la cantidad de planes que va a desea y se van sumando para mostrar en la boleta y sacar el calculo final
            if tratamiento==1:
                while True:
                    try:
                        c_carillas=int(input("Cuantas carillas de porcelana desea?\n"))
                        if c_carillas>0:
                            break
                        else:
                            print("Valores sobre 0.")
                    except ValueError:
                        print("Debe ingresar solo números.")
                t_carillas+=c_carillas #se suma la cantidad de tratamientos
            elif tratamiento==2:
                while True:
                    try:
                        c_implantes=int(input("Cuantos implantes dentales desea?\n"))
                        if c_implantes>0:
                            break
                        else:
                            print("Valores sobre 0.")
                    except ValueError:
                        print("Debe ingresar solo números.")
                t_implantes+=c_implantes #se suma la cantidad de tratamientos
            elif tratamiento==3:
                while True:
                    try:
                        c_ortodoncia=int(input("Cuantas ortodoncias Brackets desea?\n"))
                        if c_ortodoncia>0:
                            break
                        else:
                            print("Valores sobre 0.")
                    except ValueError:
                        print("Debe ingresar solo números.")
                t_ortodoncia+=c_ortodoncia #se suma la cantidad de tratamientos
        while True:
            print(x)
            print("Los descuentos existentes son:")
            print(f"1.-Trabajador auxiliar {desc_auxiliar}%")
            print(f"2.-Trabajador administrativo {desc_admin}%")
            print(f"3.-Trabajador docente {desc_docen}%")
            print("4.-No tiene descuento")
            print(x)
            try:
                descuento=int(input("Ingrese el descuento que tiene: "))
                if 0<descuento<5:
                    break
                else:
                        print("Valores del 1-4.")
            except ValueError:
                print("Ingrese solo números del 1-4")
        #Se calcula el total de cada uno de los planes por separado
        total_carillas=(t_carillas*carillas)
        total_implantes=(t_implantes*implantes)
        total_ortodoncia=(t_ortodoncia*ortodoncia)
        #pago total de todo sin descuento
        total_pago=(t_carillas*carillas)+(t_implantes*implantes)+(t_ortodoncia*ortodoncia)
        #Se muestra la cotizacion de los 3 descuentos aplicados
        if descuento==1:
            #Se calcula el descuento y el total a pagar con descuento incluido
            desc=(total_pago*(desc_auxiliar/100))
            total_desc=total_pago-(desc)
            print(x)
            print("\t\tCotización")
            print(x)
            print(f"{t_carillas} tratamiento(s) Carillas Porcelana\t {total_carillas}")
            print(f"{t_implantes} tratamiento(s) Implantes Dentales\t {total_implantes}")
            print(f"{t_ortodoncia} tratamiento(s) Ortodoncia Brackets\t {total_ortodoncia}")
            print(x)
            print(f"subtotal\t{round(total_pago)}")
            print(f"Descuento {round(desc_auxiliar)}%\t{round(desc)}")
            print(x)
            print(f"Total\t{round(total_desc)}")
            print(x)
            print(f"Son 12 cuotas de:\t{round(total_desc/12)}")
            print("")
            print("Sonría Bonito!!!")
        elif descuento==2:
            #Se calcula el descuento y el total a pagar con descuento incluido
            desc=(total_pago*(desc_admin/100))
            total_desc=total_pago-(desc)
            print(x)
            print("\t\tCotización")
            print(x)
            print(f"{t_carillas} tratamiento(s) Carillas Porcelana\t {total_carillas}")
            print(f"{t_implantes} tratamiento(s) Implantes Dentales\t {total_implantes}")
            print(f"{t_ortodoncia} tratamiento(s) Ortodoncia Brackets\t {total_ortodoncia}")
            print(x)
            print(f"subtotal\t{round(total_pago)}")
            print(f"Descuento {round(desc_admin)}%\t{round(desc)}")
            print(x)
            print(f"Total\t{round(total_desc)}")
            print(x)
            print(f"Son 12 cuotas de:\t{round(total_desc/12)}")
            print("")
            print("Sonría Bonito!!!")
        elif descuento==3:
            #Se calcula el descuento y el total a pagar con descuento incluido
            desc=(total_pago*(desc_docen/100))
            total_desc=total_pago-(desc)
            print(x)
            print("\t\tCotización")
            print(x)
            print(f"{t_carillas} tratamiento(s) Carillas Porcelana\t {total_carillas}")
            print(f"{t_implantes} tratamiento(s) Implantes Dentales\t {total_implantes}")
            print(f"{t_ortodoncia} tratamiento(s) Ortodoncia Brackets\t {total_ortodoncia}")
            print(x)
            print(f"subtotal\t{round(total_pago)}")
            print(f"Descuento {round(desc_docen)}%\t{round(desc)}")
            print(x)
            print(f"Total\t{round(total_desc)}")
            print(x)
            print(f"Son 12 cuotas de:\t{round(total_desc/12)}")
            print("")
            print("Sonría Bonito!!!")
        #Cotización del cliente sin descuento
        else:
            
            print(x)
            print("\t\tCotización")
            print(x)
            print(f"{t_carillas} tratamiento(s) Carillas Porcelana\t {total_carillas}")
            print(f"{t_implantes} tratamiento(s) Implantes Dentales\t {total_implantes}")
            print(f"{t_ortodoncia} tratamiento(s) Ortodoncia Brackets\t {total_ortodoncia}")
            print(x)
            print(f"subtotal\t{round(total_pago)}")
            print(f"Descuento {round(no_desc)}%")
            print(x)
            print(f"Total\t{round(total_pago)}")
            print(x)
            print(f"Son 12 cuotas de:\t{round(total_pago/12)}")
            print("")
            print("Sonría Bonito!!!")
    if opcion==2:
        if c_carillas!="":
            print("Se elimaron los datos anteriormente seleccionados.")
            c_carillas=0
            c_implantes=0
            c_ortodoncia=0
            t_carillas=0
            t_implantes=0
            t_ortodoncia=0
        else:
            print("No hay datos ingresados para borrar.")
if opcion==3:
    print(x)
    print("¡¡Gracias por preferir Diente De Oro !!")
    print(x)