# INICIO SISTEMA DE JUEGO #

class BatallaPokemon:

    def __init__(self, poke1, poke2):
        self.turnoactual = 0
        self.pokemon1 = poke1
        self.pokemon2 = poke2

    def termina_batalla(self):
        pass


class TurnoEntrenador:

    pass


class ComandoJugador:
    pass


# diccionario por cada maestro

entrenador_1 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Registro de Turnos': [None, ],
                }

entrenador_2 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Registro de Turnos': [None, ],
                }