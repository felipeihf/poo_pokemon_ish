# INICIO SISTEMA DE JUEGO #

from pokemon import *
from pokedex import *
from pokeconstantes import *

class BatallaPokemon:

    def __init__(self, entrenador1, poke1, entrenador2, poke2):

        self.turnoactual = 0
        self.pokemon1 = poke1
        entrenador_1['Pokemon Elegido'] = poke1
        self.pokemon2 = poke2
        entrenador_2['Pokemon Elegido'] = poke2
        self.entrenador1 = entrenador1
        entrenador_1['Nombre'] = entrenador1
        self.entrenador2 = entrenador2
        entrenador_2['Nombre'] = entrenador2

    def moneda_partida(self, eleccion_trainer1):

        eleccion_trainer1 = input("Jugador 1, escriba aquí cara o sello: ").lower()
        lanzar_moneda = random.randint(0,1)
        if lanzar_moneda == 0:
            print("CARA")
        else:
            print("SELLO")
        if eleccion_trainer1 == 'cara' and lanzar_moneda == 0:
            print("Comienza el entrenador 1.")

        else:
            print("Comienza el entrenador 2.")


    #Ya se reciben los datos
    #Ya se deciden los casos en que un jugador parte primero que el otro
    #SE DEBE VERIFICAR SI SE RECIBEN BIEN LOS DATOS EN EL JUEGO


    #POR HACER:
    #Para iniciar la pelea, debe partir el jugador que gana la tirada de moneda
    #Una vez eligen sus Pokemons, lo primero que debo establecer es la ventaja de tipos
    # 3 casos: mismo tipo (no hay ventaja)
    # fuerte contra debil (el primero tiene ventaja)
    # debil contra fuerte (el segundo tiene ventaja)
    #una vez eligen los pokemons que usar, la ventaja se determina automaticamente (si la hay)

    # TURNOS #
    #La pelea debe dar la opcion entre dos ataques: el normal (con PA) y el especial del tipo.
    #Restar parametros segun ventajas y caracteristicas de pokemons
    #Chequear estado del juego (pvs actuales para ver ganador)
    #Si el ganador aun no está determinado, sigue el otro jugador
    #Turno del otro jugador, se le invita a realizar una acción

    #El vector de turno debe incluir:
    # [nro turno, accion realizada, daño realizado, pv restantes]
    #agregar lista a llave del diccionario 'Turnos realizados'



# diccionario por cada maestro

entrenador_1 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Turnos realizados': [None, ],
                }

entrenador_2 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Turnos realizados': [None, ],
                }

historial_turnos = None
