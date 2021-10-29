import pokedex
import os
import pokemon
import pokeconstantes
import json

comando_usuario = 0 #Flag / Bandera

while comando_usuario != 4:
    print("""--------------- POKEMON --------------
            Elija su opción:
            (1) Pokedex
            (2) Duelo Pokemon
            (3) Estadisticas de Batalla
            (4) Salir""")

    try:
        comando_usuario = int(input("Ingrese la opción que desea (Número del 1 al 4, segun corresponda): "))
    except:
        print("          ---------------------------------------------------------         ")
        print("      ERROR: Por favor, ingrese un número con el formato solicitado.        ")
        print("          ---------------------------------------------------------         ")



# MUESTRA POKEDEX #
    if comando_usuario == 1:
        os.system('cls')
        for key in pokedex.registro_pokedex:
            print(key)
        try:
            seleccion_detalle = int(input("Ingrese el número del Pokemon que desea revisar: "))
            if seleccion_detalle in range(1, 10):
                print(pokedex.registro_pokedex[seleccion_detalle])
        except:
            print("Debe ingresar un número entre 1 y 9.")



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


# Crea 9 Pokemon estandar al iniciar el script




