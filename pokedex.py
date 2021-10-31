import pokeconstantes
import json
from pokemon import *

registro_pokedex = {'Pokedex': 'Pokemon Iniciales y Evoluciones',
                    '#1': pokeconstantes.BULBASAUR.nombre_pokemon,
                    '#2': pokeconstantes.IVYSAUR.nombre_pokemon,
                    '#3': pokeconstantes.VENUSAUR.nombre_pokemon,
                    '#4': pokeconstantes.SQUIRTLE.nombre_pokemon,
                    '#5': pokeconstantes.WARTORTLE.nombre_pokemon,
                    '#6': pokeconstantes.BLASTOISE.nombre_pokemon,
                    '#7': pokeconstantes.CHARMANDER.nombre_pokemon,
                    '#8': pokeconstantes.CHARMELEON.nombre_pokemon,
                    '#9': pokeconstantes.CHARIZARD.nombre_pokemon,}


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

    def __init__(self):
        pass

# READ #
    @classmethod
    def mostrar_registros(self):

        for key in registro_pokedex:
            print(key, '', registro_pokedex[key])
        seleccion_detalle = int(input("Ingrese el número del Pokemon que desea revisar: "))
        if seleccion_detalle in range(1, 10):
            print("Datos proporcionados.")
            print(json.dumps((
                lista_pokedex[seleccion_detalle].__dict__), indent=1))

# CREATE #
    @classmethod
    def crear_nuevo_pkm(self):

        print("Para crear su Pokemon, ingrese los datos solicitados a continuación: ")
        nombre_pokemon = input("Ingrese el nombre de su Pokemon a registrar: ")
        puntos_vida = int(input("Ingrese el numero de puntos de vida del Pokemon: "))
        puntos_ataque = int(input("Ingrese el numero de puntos de ataque del Pokemon: "))
        tipo_pokemon_creado = input("Tipo de Pokemon, entre Fuego, Agua y Hierba: ")

        if tipo_pokemon_creado == 'Fuego':
            nuevo_pokemon = TipoFuego(nombre_pokemon, len(lista_pokedex),
                                    puntos_vida, puntos_ataque, 'Fuego', 'Agua', 'Hierba')
            lista_pokedex.append(nuevo_pokemon)
            registro_pokedex[f'#{len(lista_pokedex)-2}'] = nombre_pokemon
            print(json.dumps((
                lista_pokedex[-1].__dict__), indent=1))
            print("Pokemon registrado con éxito")

        elif tipo_pokemon_creado == 'Agua':
            nuevo_pokemon = TipoAgua(nombre_pokemon, len(lista_pokedex),
                                    puntos_vida, puntos_ataque, 'Agua', 'Hierba', 'Fuego')
            lista_pokedex.append(nuevo_pokemon)
            registro_pokedex[f'#{len(lista_pokedex)-2}'] = nombre_pokemon
            print(json.dumps((
                lista_pokedex[-1].__dict__), indent=1))
            print("Pokemon registrado con éxito")

        elif tipo_pokemon_creado == 'Hierba':
            nuevo_pokemon = TipoHierba(nombre_pokemon, len(lista_pokedex),
                                    puntos_vida, puntos_ataque, 'Hierba', 'Fuego', 'Agua')
            lista_pokedex.append(nuevo_pokemon)
            registro_pokedex[f'#{len(lista_pokedex)-2}'] = nombre_pokemon
            print(json.dumps((
                lista_pokedex[-1].__dict__), indent=1))
            print("Pokemon registrado con éxito")

# UPDATE #

    # @classmethod
    # def editar_pokemon(self):

    #     pokemon_indexado = int(input("""Ingrese el número del Pokemon que desea editar:\n
    #                                 La lista está disponible en la opción 1 de Pokedex."""))

    #     opcion_usuario = input("""Ingrese el campo que desea modificar:
    #                             (Nombre/Vida/Ataque/) """).lower()

    #     if pokemon_indexado in range(1, len(lista_pokedex)):
    #         if opcion_usuario == 'nombre':
    #             pass
    #         elif opcion_usuario == 'vida':
    #             pass
    #         elif opcion_usuario == 'ataque':
    #             pass
    #         else:
    #             print("Información otorgada erronea. Intente nuevamente.")
    #     else:
    #         print("La id de este Pokemon no existe en la base de datos.")

    #         nuevo_nombre = input("Nuevo Nombre: ")
    #         nuevos_pv = int(input("Nuevos puntos de ataque: "))
    #         nuevos_pa = int(input("Nuevos puntos de ataque: "))

# DELETE #

    @classmethod
    def borrar_pokemon(self):

        pokemon_indexado = int(input("""Ingrese el número del Pokemon que desea BORRAR:\n
                                    La lista está disponible en la opción 1 de Pokedex."""))

        if pokemon_indexado in range(1, len(lista_pokedex)):
            lista_pokedex.pop(pokemon_indexado)
            registro_pokedex[f'#{pokemon_indexado}'] = 'BORRADO'
            print(json.dumps((
                lista_pokedex[-1].__dict__), indent=1))
            print("Pokemon borrado con éxito")






