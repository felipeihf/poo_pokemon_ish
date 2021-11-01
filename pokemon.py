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
        if self.pv_actuales <= 100:
            self.pv_actuales += random.randint(1, 5)
        elif self.pv_actuales > 100 and self.pv_actuales <= 1000:
            self.pv_actuales += random.randint(10, 50)
        elif self.pv_actuales > 1000 and self.pv_actuales <= 10000:
            self.pv_actuales += random.randint(100, 500)

    def despedirse(self):
        print(f"{self.nombre_pokemon} se retira del combate!")


class TipoAgua(Pokemon):

    def __init__(self, nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza):
        super().__init__(nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza)

        self.plus_hidrobomba = 1.5

    @classmethod
    def esquiva_fuego():
        probabilidad_esquivar = [True, False]
        return random.choice(probabilidad_esquivar)


class TipoHierba(Pokemon):

    def __init__(self, nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza):
        super().__init__(nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza)

        self.plus_rayosolar = 1.5

    @classmethod
    def esquiva_agua():
        probabilidad_esquivar = [True, False]
        return random.choice(probabilidad_esquivar)


class TipoFuego(Pokemon):

    def __init__(self, nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza):
        super().__init__(nombre_pkm, id_pkm, pv_pkm, pa_pkm, tipo_pkm, debilidad, fortaleza)

        self.plus_rafagafuego = 1.5

    @classmethod
    def esquiva_hierba():
        probabilidad_esquivar = [True, False]
        return random.choice(probabilidad_esquivar)

# FIN MODELOS POKEMON #


# ---------------------#






