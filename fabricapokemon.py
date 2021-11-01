import random

class Pokemon:

    def __init__(self, name, id, pv, pa, type, weak, strong):
        self.nombre = name
        self.id = id
        self.puntos_vida = pv
        self.puntos_ataque = pa
        self.tipo = type
        self.debilidad = weak
        self.fortaleza = strong


    def atacar(self, pv_objetivo):
        return pv_objetivo - random.randint(1, self.puntos_ataque)

    def autoregeneracion(self):
        return self.puntos_vida * round(random.uniform(1.01, 1.05), 2)

    def despedirse(self):
        return f"{self.nombre} está fuera de combate!"

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_puntosvida(self, nuevos_pv):
        self.puntos_vida = nuevos_pv

    def set_puntosataque(self, nuevos_pa):
        self.puntos_ataque = nuevos_pa

    def get_nombre(self):
        return self.nombre

    def get_puntosvida(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_debilidad(self):
        return self.debilidad

    def get_fortaleza(self):
        return self.fortaleza




class TipoAgua(Pokemon):

    def __init__(self, name, id, pv, pa, type, weak, strong):
        super().__init__(name, id, pv, pa, type, weak, strong)

    def debilidad(self):
        pass

    def hidrobomba(self):
        return self.puntos_ataque * 2

    def esquiva_fuego(self):
        probabilidad = [True, False]
        resultado = random.choice(probabilidad)
        if resultado:
            return 1
        else:
            return 0


class TipoFuego(Pokemon):

    def __init__(self, name, id, pv, pa, type, weak, strong):
        super().__init__(name, id, pv, pa, type, weak, strong)

    def llamarada(self):
        return self.puntos_ataque * 2

    def esquiva_hierba(self):
        probabilidad = [True, False]
        resultado = random.choice(probabilidad)
        if resultado:
            return 1
        else:
            return 0

class TipoHierba(Pokemon):

    def __init__(self, name, id, pv, pa, type, weak, strong):
        super().__init__(name, id, pv, pa, type, weak, strong)

    def rayosolar(self):
        return self.puntos_ataque * 2

    def esquiva_agua(self):
        probabilidad = [True, False]
        resultado = random.choice(probabilidad)
        if resultado:
            return 1
        else:
            return 0
