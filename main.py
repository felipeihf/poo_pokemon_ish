import pokedex
import os

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



# MUESTRA POKEDEX #
    if comando_usuario == 1:
        os.system('cls')
        opcion_pokedex = int(input("""Bievenido al registro Pokedex.\n
                                    Ingrese la operación a realizar:\n
                                    (1) Registrar nuevo Pokemon (SOLO FUEGO/AGUA/HIERBA)\n
                                    (2) Mostrar Pokedex actual\n
                                    (3) Actualizar datos de Pokemon existente\n
                                    (4) Borrar Pokemon\n
                                    (5) Salir
                                    """))
        if opcion_pokedex == 1:
            os.system('cls')
            pass # RELLENAR CON INSTANCIA DE NUEVO OBJETO Y APPEND A REGISTROS
        if opcion_pokedex == 2:
            os.system('cls')
            pokedex.PokeCRUD.mostrar_registros()
        if opcion_pokedex == 3:
            os.system('cls')
            pass# Dar opciones de qué atributo se desea modificar.
                # Se dará acceso parcial a modificación de datos.
                # No modificables: id, tipo, debilidades y fortalezas.
        if opcion_pokedex == 4:
            os.system('cls')
            pass #Pasar diccionarios a listas de pares para mostrar el registro.
            # Implementar matrices de 2 o mas capas para borrado simultaneo de entradas.



# BATALLA #
    elif comando_usuario == 2:

        os.system('cls')
        print("          ---------------------------------------------------------         ")
        print("                      D U E L O   P O K E M O N                             ")
        print("          ---------------------------------------------------------         ")

        entrenador_1 = input("Ingrese nombre de entrenador 1 : ")
        entrenador_2 = input("Ingrese nombre de entrenador 2 : ")
        try:
            eleccion_pokemon_1 = int(input("Entrenador 1, elija un Pokemon de la Pokedex ingresando su ID: "))
        except:
            print("El ID ingresado no es válido, ingrese un número del 1 al 10. ")
        def pedir_accion(pokemon):
            comando = None
            while not comando:
                prompt_comando = input("Qué debería hacer")


# LOG DE COMBATE #
    elif comando_usuario == 3:
        os.system('cls')
        print("          ---------------------------------------------------------         ")
        print("                      E S T A D I S T I C A S                               ")
        print("          ---------------------------------------------------------         ")

    elif comando_usuario == 4:
        print("Saliendo del juego... Gracias por jugar.")






