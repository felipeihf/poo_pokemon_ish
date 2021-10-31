import pokedex
import os
import sistemacombate

comando_usuario = 0 # Flag de continuidad

while comando_usuario != 4:
    print("""--------------- POKEMON --------------
            Elija su opción:
            (1) Pokedex
            (2) Duelo Pokemon
            (3) Estadisticas de Batalla
            (4) Salir\n""")

    try:
        comando_usuario = int(input("""Ingrese la opción que desea
                                (Número del 1 al 4, segun corresponda): """))
    except:
        print("""
                    (!!!!!!!) ERROR: Por favor, ingrese un número con el formato solicitado.
            """)


                                    # MENU #
    if comando_usuario == 1:
        os.system('cls')
        opcion_pokedex = int(input("""Bievenido al registro Pokedex.\n
                                    Ingrese la operación a realizar:\n
                                    (1) Registrar nuevo Pokemon (SOLO FUEGO/AGUA/HIERBA)
                                    (2) Mostrar Pokedex actual
                                    (3) Actualizar datos de Pokemon existente
                                    (4) Borrar Pokemon
                                    (5) Salir
                                    """))
        if opcion_pokedex == 1:
            os.system('cls')
            pokedex.PokeCRUD.crear_nuevo_pkm()
        elif opcion_pokedex == 2:
            os.system('cls')
            pokedex.PokeCRUD.mostrar_registros()
        elif opcion_pokedex == 3:
            os.system('cls')
            pokedex.PokeCRUD.editar_pokemon()
        elif opcion_pokedex == 4:
            os.system('cls')
            pokedex.PokeCRUD.borrar_pokemon()



                                    # BATALLA #
    elif comando_usuario == 2:

        os.system('cls')
        print("""----------- D U E L O   P O K E M O N -----------""")

        # USAR AQUI MODULO DE SISTEMA DE COMBATE

                                    # LOG DE COMBATE #
    elif comando_usuario == 3:
        os.system('cls')
        print("""----------- E S T A D I S T I C A S -----------""")

        #USAR AQUI MODULO DE ESTADISTICAS

    elif comando_usuario == 4:
        print("Saliendo del juego... Gracias por jugar.")






