bandas =[]
banda={}

opcion=100
while(opcion != 5):
    print("*****FESTIVAL ALTAVOZ*****")
    print("**************************")
    print("1. Registrar Banda")
    print("2. Ver el Cartel del Festival")
    print("3. Buscar Banda")
    print("4. Modificar Banda")
    print("5. Finalizar")
    
    opcion=int(input("DIgite una opcion: "))

    if opcion == 1:
        banda={}
        banda["id"]=int(input("Digite su id: "))
        banda["nombre"]=input("nombre:")
        banda["genero"]=input("Genero: ")
    
        bandas.append(banda)
        

    elif opcion ==2:

        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")

    elif opcion == 3:
        bandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
                if bandaAuxiliar["nombre"] == bandaBuscada:
                    print("oe la encontre")
                else:
                    print("no lo encontraste")
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("Opcion Invalida")