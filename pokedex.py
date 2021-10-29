import pokeconstantes
import json

registro_pokedex = {'Pokedex': 'Pokemon Iniciales y Evoluciones',
                    '#1': pokeconstantes.BULBASAUR.nombre,
                    '#2': pokeconstantes.IVYSAUR.nombre,
                    '#3': pokeconstantes.VENUSAUR.nombre,
                    '#4': pokeconstantes.SQUIRTLE.nombre,
                    '#5': pokeconstantes.WARTORTLE.nombre,
                    '#6': pokeconstantes.BLASTOISE.nombre,
                    '#7': pokeconstantes.CHARMANDER.nombre,
                    '#8': pokeconstantes.CHARMELEON.nombre,
                    '#9': pokeconstantes.CHARIZARD.nombre,}


lista_pokedex = [None, pokeconstantes.BULBASAUR,
                        pokeconstantes.IVYSAUR,
                        pokeconstantes.VENUSAUR,
                        pokeconstantes.SQUIRTLE,
                        pokeconstantes.WARTORTLE,
                        pokeconstantes.BLASTOISE,
                        pokeconstantes.CHARMANDER,
                        pokeconstantes.CHARMELEON,
                        pokeconstantes.CHARIZARD,]


class PokeCRUD:

    def mostrar_registros(self):
        for key in registro_pokedex:
            print(key, '', registro_pokedex[key])
        seleccion_detalle = int(input("Ingrese el número del Pokemon que desea revisar: "))
        if seleccion_detalle in range(1, 10):
            print("Datos proporcionados.")
            print(json.dumps((
                lista_pokedex[seleccion_detalle].__dict__), indent=1))




