
contact: dict = {
    "Miguel" : "3004451231",
    "Amada" : "3014454562",
    "Elena" : "3024451203",
    "Ainara" : "3114455694",
    "Alanna" : "3124458795",
    "Cris" : "3134459578",
    "Yaireth" : "3204547895",
    "Poncho" : "3214578495",
    "Hilda" : "3172237548"
}

def insert_phone(name):
        phone = input("Teléfono: ")
        if phone.isdigit() and (len(phone) > 0 and len(phone) <= 11):
            contact[name] = phone
        else:
            print("El teléfono debe ser numérico entre uno y 11 dígitos.")


def new():
    name = input("Nombre: ")
    insert_phone(name)


def find():
    name = input("Nombre del contacto: ")
    if name in contact: print(f"Nombre: {name} | Teléfono: {contact[name]}.")
    else: print(f"El contacto \"{name}\" no existe.")


def update():
    name = input("Introduce el nombre del contacto a actualizar: ")
    if name in contact: insert_phone(name)
    else: print(f"El contacto \"{name}\" no existe.")


def delete():
    name = input("Introduce el nombre del contacto a eliminar: ")
    if name in contact: del contact[name]
    else: print(f"El contacto {name} no existe.")


def listing():
    for name in contact:
        print(f'{name:<15} : {contact[name]:<12}')


def menu():
    print('\n***** MENU *****\n')
    print('1. Nuevo')
    print('2. Buscar')
    print('3. Editar')
    print('4. Eliminar')
    print('5. Listar')
    print('0. Salir\n')


while True:
    
    menu()
    opc = input('Digita la opción: ')
    print('')
    
    match opc:
        case '1': new()
        case '2': find()
        case '3': update()
        case '4': delete()
        case '5': listing()
        case '0': break
        case _: print('¡¡¡ Opción errada !!!')
