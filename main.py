import pokedex
import pokemon

comando_usuario = 0 #Flag / Bandera

while comando_usuario != 5:
    print("""--------------- DUELOS POKEMON --------------
            Bienvenid@ a venta de pasajes online.
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

    if comando_usuario == 1:
        print(pokedex.registro_pokedex)
    elif comando_usuario == 2:
        pass
    elif comando_usuario == 3:
        pass
    elif comando_usuario == 4:
        pass


# Crea 9 Pokemon estandar al iniciar el script

if __name__ == '__main__':

    Bulbasaur = pokemon.TipoHierba("Bulbasaur", 1, 100, "Agua", "Hierba", "Fuego")
    Ivysaur = pokemon.TipoHierba("Ivysaur", 2, 1000, "Agua", "Hierba", "Fuego")
    Venusaur = pokemon.TipoHierba("Venusaur", 3, 10000, "Agua", "Hierba", "Fuego")

    Squirtle = pokemon.TipoAgua("Squirtle", 4, 100, "Agua", "Hierba", "Fuego")
    Wartortle = pokemon.TipoAgua("Wartortle", 5, 1000, "Agua", "Hierba", "Fuego")
    Blastoise = pokemon.TipoAgua("Blastoise", 6, 1000, "Agua", "Hierba", "Fuego")

    Charmander = pokemon.TipoFuego("Charmander", 7, 100, "Fuego", "Agua", "Hierba")
    Charmeleon = pokemon.TipoFuego("Charmeleon", 8, 1000, "Fuego", "Agua", "Hierba")
    Charizard = pokemon.TipoFuego("Charizard", 9, 10000, "Fuego", "Agua", "Hierba")

