import random



class Pokemon:
    def __init__(self, nombre_pkm, id_pkm, pv_pkm, tipo_pkm, debilidad, fortaleza):
        self.nombre_pokemon = nombre_pkm
        self.id_pokemon = id_pkm
        self.pv_pokemon = pv_pkm
        self.pa_pokemon = 0
        self.tipo_pokemon = tipo_pkm
        self.debilidad = debilidad
        self.fortaleza = fortaleza

    def atacar(self):
        return self.pa_pokemon

    def autoRegeneracion(self):
        self.pv_pokemon += random.randint(1, 5)

    def despedirse(self):
        print("shao lo vimo'")


class TipoAgua(Pokemon):

    def plus_hidrobomba():
        return Pokemon.pa_pokemon + 10

    def esquiva_fuego():
        pass

class TipoHierba(Pokemon):

    def plus_rayosolar():
        pass

    def esquiva_agua():
        pass


class TipoFuego(Pokemon):

    def plus_rafagafuego():
        pass

    def esquiva_hierba():
        pass




