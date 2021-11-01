import os
import sistemaCRUD
import sistemacombate

#PARA EMPEZAR A JUGAR, SE DEBEN CREAR AL MENOS 2 POKEMON ENTRE TIPO AGUA, FUEGO O HIERBA
#EL PROGRAMA OTORGA LOS PASOS A SEGUIR PARA REGISTRARSE
#EL SISTEMA SE ENCARGA DEL RESTO

opcion = 0
while opcion != 4:
    print("""--------------- POKEMON --------------
            Elija su opción:
            (1) Pokedex
            (2) Duelo Pokemon
            (3) Estadisticas de Batalla
            (4) Salir\n""")

    try:
        opcion = int(input("""Ingrese la opción que desea
                                (Número del 1 al 4, segun corresponda): """))
    except:
        print("(!!!) ERROR: Por favor, ingrese un número con el formato solicitado.")


    if opcion == 1:
        os.system('cls')
        opcion_crud = int(input("""----------- P  O  K  E  D  E  X  -----------\n
            (1) Ver Pokedex
            (2) Crear Pokemon
            (3) Editar Pokemon (solo pv, pa y nombre)
            (4) Borrar Pokemon
            """))
        if opcion_crud == 1:
            sistemaCRUD.leer_pokemon()
        elif opcion_crud == 2:
            sistemaCRUD.crear_pokemon()
        elif opcion_crud == 3:
            sistemaCRUD.actualizar_pokemon()
        elif opcion_crud == 4:
            sistemaCRUD.borrar_pokemon()

    elif opcion == 2:
        os.system('cls')
        print("""----------- D U E L O   P O K E M O N -----------\n""")
        sistemacombate.BATALLA_POKEMON()

    elif opcion == 3:
        os.system('cls')
        print("""----------- LOG DE COMBATE -----------""")

    elif opcion == 4:
        os.system('cls')
        print("Saliendo del juego... Gracias por jugar.")