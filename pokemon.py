import random

# INICIO MODELOS POKEMON #

class Pokemon:
    def __init__(self, nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza):
        self.nombre_pokemon = nombre_pkm
        self.id_pokemon = id_pkm
        self.pv_actuales = pv_pkm
        self.pa_pokemon = pa_pkm
        self.tipo_pokemon = tipo_pkm
        self.debilidad = debilidad
        self.fortaleza = fortaleza

    def atacar(self):
        return self.pa_pokemon

    def autoRegeneracion(self):
        if self.pv_pokemon <= 100:
            self.pv_actuales += random.randint(1, 5)
        elif self.pv_actuales> 100 and self.pv_actuales <= 1000:
            self.pv_actuales += random.randint(10, 50)
        elif self.pv_actuales > 1000 and self.pv_actuales <= 10000:
            self.pv_actuales += random.randint(100, 500)

    def despedirse(self):
        print("shao lo vimo'")


class TipoAgua(Pokemon):

    def plus_hidrobomba():
        return Pokemon.pa_pokemon * 3

    def esquiva_fuego():
        pass

class TipoHierba(Pokemon):

    def plus_rayosolar():
        return Pokemon.pa_pokemon * 3

    def esquiva_agua():
        pass


class TipoFuego(Pokemon):

    def plus_rafagafuego():
        return Pokemon.pa_pokemon * 3

    def esquiva_hierba():
        pass

# FIN MODELOS POKEMON #


# ---------------------#

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




