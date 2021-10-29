import pokemon
import pokedex


BULBASAUR = pokemon.TipoHierba("Bulbasaur", 1, 100, 10, "Agua", "Hierba", "Fuego")
IVYSAUR = pokemon.TipoHierba("Ivysaur", 2, 1000, 100, "Agua", "Hierba", "Fuego")
VENUSAUR = pokemon.TipoHierba("Venusaur", 3, 10000, 1000, "Agua", "Hierba", "Fuego")

SQUIRTLE = pokemon.TipoAgua("Squirtle", 4, 100, 10, "Agua", "Hierba", "Fuego")
WARTORTLE = pokemon.TipoAgua("Wartortle", 5, 1000, 100, "Agua", "Hierba", "Fuego")
BLASTOISE = pokemon.TipoAgua("Blastoise", 6, 10000, 1000, "Agua", "Hierba", "Fuego")

CHARMANDER = pokemon.TipoFuego("Charmander", 7, 100, 10, "Fuego", "Agua", "Hierba")
CHARMELEON = pokemon.TipoFuego("Charmeleon", 8, 1000, 100, "Fuego", "Agua", "Hierba")
CHARIZARD = pokemon.TipoFuego("Charizard", 9, 10000, 1000, "Fuego", "Agua", "Hierba")