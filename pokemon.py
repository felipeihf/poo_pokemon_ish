import random

# INICIO MODELOS POKEMON #

class Pokemon:
    def __init__(self, nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza):
        self._nombre_pokemon = nombre_pkm
        self._id_pokemon = id_pkm
        self._pv_actuales = pv_pkm
        self._pa_pokemon = pa_pkm
        self._tipo_pokemon = tipo_pkm
        self._debilidad = debilidad
        self._fortaleza = fortaleza

    def atacar(self):
        return self.pa_pokemon

    #Getters y Setters (excepto para id, tipos, debilidad y fortaleza)
    @property
    def nombre(self):
        return self._nombre_pokemon

    @nombre.setter
    def nombre(self, nombre):
        self._nombre_pokemon = nombre
    



    def autoRegeneracion(self):
        if self.pv_actuales <= 100:
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






