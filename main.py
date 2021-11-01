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
            pokedex.PokeCRD.crear_nuevo_pkm()
        elif opcion_pokedex == 2:
            os.system('cls')
            pokedex.PokeCRD.mostrar_registros()
        elif opcion_pokedex == 3:
            os.system('cls')
            print("No se encuentra disponible.")
        elif opcion_pokedex == 4:
            os.system('cls')
            pokedex.PokeCRD.borrar_pokemon()



                                    # BATALLA #
    elif comando_usuario == 2:

        os.system('cls')
        print("""----------- D U E L O   P O K E M O N -----------\n""")
        trainer1 = input("Entrenador 1, ingrese su nombre: ")
        poke1 = int(input("Entrenador 1, elija su Pokemon (ingrese numero de Pokedex) : "))
        trainer2 = input("Entrenador 2, ingrese su nombre: ")
        poke2 = int(input("Entrenador 2, elija su Pokemon (ingrese numero de Pokedex) : "))
        sistemacombate.BatallaPokemon(trainer1, poke1, trainer2, poke2)

                                    # LOG DE COMBATE #
    elif comando_usuario == 3:
        os.system('cls')
        print("""----------- ESTADISTICAS ULTIMO COMBATE -----------""")
        opcion = int(input("""Elija entre: (1) Jugador 1\n(2)Jugador 2\n(3)Ambos\n"""))
        if opcion == 1:
            print(sistemacombate.entrenador_1)
        elif opcion == 2:
            print(sistemacombate.entrenador_2)
        else:
            print(sistemacombate.entrenador_1)
            print(sistemacombate.entrenador_2)

    elif comando_usuario == 4:
        print("Saliendo del juego... Gracias por jugar.")






