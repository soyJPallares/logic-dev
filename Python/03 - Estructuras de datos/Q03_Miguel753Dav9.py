def Menu():
    print("Menu")
    print("1. Nuevo Contacto")
    print("2. Buscar Contacto")
    print("3. Editar Contacto")
    print("4. Eliminar Contacto")
    print("5. Listar Contactos")
    print("   Digite 0 para salir")


def Nuevo():
    name = input("Digite el nombre: ")
    phone = input("Digite el numero de telefono: ")
    if phone.isnumeric() and len(phone) <= 11 : agenda[name] = phone
    else:
        print("Solo puedo digitar numeros en el numero de telefono")
        


def Buscar():
    name = input("Digite el nombre a buscar: ")
    if name in agenda: print(f"El numero de {name} es {agenda[name]}")
    else: print("El contacto no existe")


def Editar():
    #return "Editar Contacto"
    name = input("Digite la persona a editar: ")
    if name in agenda: 
        phone = input("Digite el numero de telefono: ")
        if phone.isnumeric() and len(phone) <= 11 : agenda[name] = phone
        else:
            print("Solo puedo digitar numeros en el numero de telefono")
    else:
        print("El contacto no existe")


def Eliminar():
    name = input("Digite el nombre de la persona a eliminar: ")
    if name in agenda: 
        phone = input("Digite el numero de telefono: ")
        if phone.isnumeric() and len(phone) <= 11 : del agenda[name]
        else:
            print("Solo puedo digitar numeros en el numero de telefono")
    else:
        print("El contacto no existe")

agenda = {}

while True:
    Menu()
    opc = int(input("Escoge una opcion: "))
    match opc:
        case 1:
            print(Nuevo())
        case 2:
            print(Buscar())
        case 3:
            print(Editar())
        case 4:
            print(Eliminar())
        case 5:
            print(agenda)
        case 0:
            break
        case _:
            print("Opcion no valida")


    
