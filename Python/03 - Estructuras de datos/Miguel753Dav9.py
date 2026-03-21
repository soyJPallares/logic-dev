#Listas
my_list = ["Miguel", "Amada", "Elena", "Jonatan"]
print(my_list)
my_list.append("Ainara")
print(my_list)
my_list.remove("Amada")
print(my_list)
print(my_list[3])
my_list[3] = "La Mona"
print(my_list)
my_list.sort()
print(my_list)

#Tuplas
my_tuple: tuple = ("Miguel", "Pallares", "Char", "36")
print(my_tuple[1]) #Acceso
print(my_tuple [3])
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

# Sets

my_set = {"Miguel", "Pallares", "Char", "36"}
print(my_set)
my_set.add("mdpallaresflorez@gmail.com")
my_set.add("mdpallaresflorez@gmail.com")
print(my_set)
my_set.remove("Pallares")
print(my_set)
my_set = set(sorted(my_set))
print(my_set)
print(type(my_set))

#Diccionario
my_dict: dict = {
    "name": "Miguel",
    "surname": "Pallares",
    "alias": "Char",
    "age": "11"
}
my_dict["email"] = "mdpallaresflorez@gmail.com" #Inserccion
print(my_dict)
del my_dict["surname"]
print(my_dict)
print(my_dict["name"])
my_dict["age"] = "12"
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))