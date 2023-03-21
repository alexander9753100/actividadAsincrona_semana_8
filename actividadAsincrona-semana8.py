# Humanos 10 (Países, Gentilicios) Ej: (EL Salvador, salvadoreño)
pa1 = "Colombia"
pa2 = "Comoras"
pa3 = "Corea del Norte"
pa4 = "el salvador"
pa5 = "estados unidos"
pa6 = "guatemala"
pa7 = "honduras"
pa8 = "rusia"
pa9 = "Noruega"
pa10 = "Nicaragua"
# Animales 10 (Especie, tipo) Ej (Canina, Lobo)
ani1 ="FELINO"
ani2 = "CANINO"
ani3 = "CRUSTACIOS"
ani4 = "ARTROPODOS"
ani5 = "ANFIVIOS"
ani6 = "AVES"
ani7 = "INSECTOS"
ani8 = "MOLUSCOS"
ani9 = "MAMIFEROS"
ani10 ="REPTILES"

# pedir que ingrese el nombre 
ingre = input("ingresa nombre de usuario: ")
print("")
menu_1 = input('''menu
               
 1- humanos
 
 2- animales
 
 escoja una opcion ''')
print("")
if menu_1 == 'humanos' or menu_1 == '1':
    Menu_Dos = input(f'''
                    \tMenu de paises
                     1-{pa1}
                     2-{pa2}
                     3-{pa3}
                     4-{pa4}
                     5-{pa5}
                     6-{pa6}
                     7-{pa7}
                     8-{pa8}
                     9-{pa9}
                     10-{pa10}
                    Ingrese una opcion del menu -> ''')
    if Menu_Dos == pa1 or Menu_Dos == '1':
        print(f"{ingre} tu eres de {pa1} tu Gentilicio es colombiano ")
    
    elif Menu_Dos == pa2 or Menu_Dos == '2':
        print(f"{ingre} tu eres de {pa2} tu Gentilicio es comorense")

    elif Menu_Dos == pa3 or Menu_Dos == '3':
        print(f"{ingre} tu eres de {pa3} tu Gentilicio es coreano")

    elif Menu_Dos == pa4 or Menu_Dos == '4':
        print(f"{ingre} tu eres de {pa4} tu Gentilicio es salvadoreño")

    elif Menu_Dos == pa5 or Menu_Dos == '5':
        print(f"{ingre} tu eres de {pa5} tu Gentilicio es estadounidense ")

    elif Menu_Dos == pa6 or Menu_Dos == '6':
        print(f"{ingre} tu eres de {pa6} tu Gentilicio es guatemalteco ")
    
    elif Menu_Dos == pa7 or Menu_Dos == '7':
        print(f"{ingre} tu eres de {pa7} tu Gentilicio es hondureño")
    
    elif Menu_Dos == pa8 or Menu_Dos == '8':
        print(f"{ingre} tu eres de {pa8} tu Gentilicio es ruso")
    
    elif Menu_Dos == pa9 or Menu_Dos == '9':
        print(f"{ingre} tu eres de {pa9} tu Gentilicio es noruego")
    
    elif Menu_Dos == pa10 or Menu_Dos == '10':
        print(f"{ingre} tu eres de {pa10} tu Gentilicio es nicaraguense")

    else:
        print("La opcion no esta disponible, no sabemos tu pais")
        
#Estructura IF ELIF
# Comparar los datos almacenados con los datos capturados al usuario
# Al ejecutarse la estructura mostrar un mensaje del gentilicio de ese país o los tipos de animales pertenecientes a esa especie según la opción seleccionada.
        
elif menu_1 == "ANIMALES" or menu_1 == "2":
    Menu_Dos = input(f'''
Menu de especieles
1-{ani1}
2-{ani2}
3-{ani3}
4-{ani4}
5-{ani5}
6-{ani6}
7-{ani7}
8-{ani8}
9-{ani9}
10-{ani10}
Ingrese una opcion del menu -> ''')

    if Menu_Dos == ani1 or Menu_Dos == '1':
        print(f"{ingre} Usted a elegido la especie {ani1} los animales que se encuentran el leon ,Tigre, Guepardo, Jaguar, Puma, Leopardo común,Leopardo de las nieves ")
        
    if Menu_Dos == ani2 or Menu_Dos == '2':
        print(f"{ingre} Usted a elegido la especie {ani2} los animales que pertenecen a esta especie son el lobos (incluyendo perros), dingos, zorros, coyotes y chacales")
        
    if Menu_Dos == ani3 or Menu_Dos == '3':
        print(f"{ingre} Usted a elegido la especie {ani3} los animales que pertenecen a este especie son el cangrejos, camarones, jaivas, langostas ")
        
    if Menu_Dos == ani4 or Menu_Dos == '4':
        print(f"{ingre} Usted a elegido la especie {ani4} los animales que pertenecen a este especie son las arañas, cienpies, escorpiones, insecto palo ")
        
    if Menu_Dos == ani5 or Menu_Dos == '5':
        print(f"{ingre} Usted a elegido la especie {ani5} los animales que pertenecen a este especie son el sapo, rana, ajolote,  ")
        
    if Menu_Dos == ani6 or Menu_Dos == '6':
        print(f"{ingre} Usted a elegido la especie {ani6} los animales que pertenecen a este especie son los pericos, aguilas, palomas, torogoses ")
        
    if Menu_Dos == ani7 or Menu_Dos == '7':
        print(f"{ingre} Usted a elegido la especie {ani7} los animales que pertenecen a este especie son las orugas, moscas, cucarachas, esperanzas, langostas ")
        
    if Menu_Dos == ani8 or Menu_Dos == '8':
        print(f"{ingre} Usted a elegido la especie {ani8} los animales que pertenecen a este especie son los caracoles, babosas , conchas ")
        
    if Menu_Dos == ani9 or Menu_Dos == '9':
        print(f"{ingre} Usted a elegido la especie {ani9} los animales que pertenecen a este especie son el mono, osos , caballos, vacas, elefantes")
        
    if Menu_Dos == ani10 or Menu_Dos == '10':
        print(f"{ingre} Usted a elegido la especie {ani10} los animales que pertenecen a este especie son el cocodrilo, iguanas , los camaleones, los dragones de comodo ")
        
    else:
        print("la opcion no esta disponible")

# Estructuras anidadas
# Se formará mediante el desarrollo de los puntos de las dos estructuras anteriores.
  
print("FIN DEL PROGRAMA")


    