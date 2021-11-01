# INICIO SISTEMA DE JUEGO #

from pokemon import *
from pokedex import *
from pokeconstantes import *
import json
import os

def turnos(eleccion_jugador, entrenador1, entrenador2):
    lados_moneda = [1, 2]
    moneda = random.choice(lados_moneda)
    if eleccion_jugador == moneda:
        os.system('cls')
        print(f"Entrenador {entrenador1} comienza el combate!")
        return True
    else:
        os.system('cls')
        print(f"Entrenador {entrenador2} comienza el combate!")
        return False

def BatallaPokemon(entrenador1, poke1, entrenador2, poke2):

        pokemon1 = vars(pokedex.lista_pokedex[poke1])
        pokemon2 = vars(pokedex.lista_pokedex[poke2])
        entrenador1 = entrenador1
        entrenador2 = entrenador2

        entrenador_1['Nombre: '] = entrenador1
        entrenador_1['Pokemon Elegido'] = pokemon1['nombre_pokemon']

        entrenador_2['Nombre: '] = entrenador2
        entrenador_2['Pokemon Elegido'] = pokemon2['nombre_pokemon']

        pv_pk1 = pokemon1['pv_actuales']
        pv_pk2 = pokemon2['pv_actuales']

        pa_pk1 = pokemon1['pa_pokemon']
        pa_pk2 = pokemon2['pa_pokemon']

        os.system('cls')
        print(f"{entrenador1} ha elegido al siguiente Pokemon: {json.dumps(pokemon1, indent=1)}")
        print(f"{entrenador2} ha elegido al siguiente Pokemon: {json.dumps(pokemon2, indent=1)}")

        elige_lado = int(input("""Jugador 1, elija un lado de la moneda: \n
                                (1) CARA\n
                                (2) SELLO\n"""))

        inicio_ronda = turnos(elige_lado, entrenador1, entrenador2)
        if inicio_ronda:

            contador_turnos = 0

            while pv_pk1 != 0 and pv_pk2 != 0:
                registro_ply1 = []
                registro_ply2 = []

                comando_ply1 = int(input(f"""{entrenador1} :
                                    ¿Qué debería hacer {pokemon1['nombre_pokemon']}
                                    (1) Ataque Normal
                                    (2) Ataque Especial
                                    (3) Retirarse"""))
                #Ataque Normal
                if comando_ply1 == 1:
                    comando = ("Ataque Normal")
                    contador_turnos += 1
                    #Ataque
                    pv_pk2 -= random.randint(1, pa_pk1)
                    daño_realizado = pv_pk2 - random.randint(1, pa_pk1)
                    print(f"{pokemon1['nombre_pokemon']} ha atacado a {pokemon2['nombre_pokemon']}")
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk1)
                    registro_ply1.append(este_turno)
                    print(f"{pokemon2['nombre_pokemon']} tiene {pv_pk2} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                #Ataque Especial
                elif comando_ply1 == 2:
                    comando = ("Ataque Especial")
                    contador_turnos += 1
                    #Ataque
                    pv_pk2 -= (random.randint(1, pa_pk1) * 1.5)
                    print(f"{pokemon1['nombre_pokemon']} ha atacado a {pokemon2['nombre_pokemon']}")
                    daño_realizado = pv_pk2 - (random.randint(1, pa_pk1) * 1.5)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk1)
                    registro_ply1.append(este_turno)
                    print(f"{pokemon2['nombre_pokemon']} tiene {pv_pk2} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                #TURNO JUGADOR 2#

                comando_ply2 = int(input(f"""{entrenador2} :
                                    ¿Qué debería hacer {pokemon2['nombre_pokemon']}
                                    (1) Ataque Normal
                                    (2) Ataque Especial"""))
                if comando_ply2 == 1:
                    comando = ("Ataque Normal")
                    contador_turnos += 1
                    #Ataque
                    pv_pk1 -= random.randint(1, pa_pk2)
                    print(f"{pokemon2['nombre_pokemon']} ha atacado a {pokemon1['nombre_pokemon']}")
                    daño_realizado = pv_pk1 - random.randint(1, pa_pk2)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk2)
                    registro_ply2.append(este_turno)
                    print(f"{pokemon1['nombre_pokemon']} tiene {pv_pk1} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                #Ataque Especial
                elif comando_ply2 == 2:
                    comando = ("Ataque Especial")
                    contador_turnos += 1
                    #Ataque
                    pv_pk1 -= (random.randint(1, pa_pk2) * 1.5)
                    print(f"{pokemon2['nombre_pokemon']} ha atacado a {pokemon1['nombre_pokemon']}")
                    daño_realizado = pv_pk1 - (random.randint(1, pa_pk2) * 1.5)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk2)
                    registro_ply2.append(este_turno)
                    print(f"{pokemon1['nombre_pokemon']} tiene {pv_pk1} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass


# RONDA B #
        elif not inicio_ronda:
            contador_turnos = 0

            while pv_pk1 != 0 and pv_pk2 != 0:
                registro_ply1 = []
                registro_ply2 = []
                comando_ply2 = int(input(f"""{entrenador2} :
                                    ¿Qué debería hacer {pokemon2['nombre_pokemon']}?
                                    (1) Ataque Normal
                                    (2) Ataque Especial"""))
                if comando_ply2 == 1:
                    comando = ("Ataque Normal")
                    contador_turnos += 1
                    #Ataque
                    pv_pk1 -= random.randint(1, pa_pk2)
                    print(f"{pokemon2['nombre_pokemon']} ha atacado a {pokemon1['nombre_pokemon']}")
                    daño_realizado = pv_pk1 - random.randint(1, pa_pk2)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk2)
                    registro_ply2.append(este_turno)
                    print(f"{pokemon1['nombre_pokemon']} tiene {pv_pk1} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                #Ataque Especial
                elif comando_ply2 == 2:
                    comando = ("Ataque Especial")
                    contador_turnos += 1
                    #Ataque
                    pv_pk1 -= random.randint(1, pa_pk2)
                    print(f"{pokemon2['nombre_pokemon']} ha atacado a {pokemon1['nombre_pokemon']}")
                    daño_realizado = pv_pk1 - (random.randint(1, pa_pk2)*1.5)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk2)
                    registro_ply2.append(este_turno)
                    print(f"{pokemon1['nombre_pokemon']} tiene {pv_pk1} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                elif comando_ply2 == 3:
                    comando = ("Abandono")
                    entrenador_1['Historial de turnos:'] = registro_ply1
                    entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                    print(f"""{pokemon2['nombre_pokemon']} se retira del combate!\n
                            {entrenador1} Es el ganador!""")
                    break


                comando_ply1 = int(input(f"""{entrenador1} :
                                    ¿Qué debería hacer {pokemon1['nombre_pokemon']}
                                    (1) Ataque Normal
                                    (2) Ataque Especial
                                    (3) Retirarse"""))
                #Ataque Normal
                if comando_ply1 == 1:
                    comando = ("Ataque Normal")
                    contador_turnos += 1
                    #Ataque
                    pv_pk2 -= random.randint(1, pa_pk1)
                    print(f"{pokemon1['nombre_pokemon']} ha atacado a {pokemon2['nombre_pokemon']}")
                    daño_realizado = pv_pk2 - random.randint(1, pa_pk1)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk1)
                    registro_ply1.append(este_turno)
                    print(f"{pokemon2['nombre_pokemon']} tiene {pv_pk2} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                #Ataque Especial
                elif comando_ply1 == 2:
                    comando = ("Ataque Especial")
                    contador_turnos += 1
                    #Ataque
                    pv_pk2 -= (random.randint(1, pa_pk1) * 1.5)
                    print(f"{pokemon1['nombre_pokemon']} ha atacado a {pokemon2['nombre_pokemon']}")
                    daño_realizado = pv_pk2 - (random.randint(1, pa_pk1) * 1.5)
                    #Añade al diccionario de turno realizado
                    este_turno = registrar_logs(contador_turnos, daño_realizado, comando, pv_pk1)
                    registro_ply1.append(este_turno)
                    print(f"{pokemon2['nombre_pokemon']} tiene {pv_pk2} puntos de vida restantes.")
                    if pv_pk2 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon2['nombre_pokemon']} ha caido!\n
                        {entrenador1} Es el ganador!""")
                        break
                    elif pv_pk1 <= 0:
                        entrenador_1['Historial de turnos:'] = registro_ply1
                        entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                        print(f"""{pokemon1['nombre_pokemon']} ha caido!\n
                        {entrenador2} Es el ganador!""")
                        break
                    else:
                        pass

                elif comando_ply1 == 3:
                    comando = ("Abandono")
                    entrenador_1['Historial de turnos:'] = registro_ply1
                    entrenador_2['Historial de turnos:'] = registro_ply2 #Añade logs para consultar
                    print(f"""{pokemon1['nombre_pokemon']} se retira del combate!\n
                            {entrenador2} Es el ganador!""")
                    break

                


def registrar_logs(contador_turnos, daño_realizado, comando, pv_pk):
    registro_turno = {'Turno: ': None,
                                    'Ataque Usado: ': None,
                                    'Daño realizado: ': None,
                                    'Pv de Pokemon restantes:': None,
                                    }
    registro_turno['Turno: '] = contador_turnos
    registro_turno['Daño realizado: '] = daño_realizado
    registro_turno['Ataque Usado: '] = comando
    registro_turno['Pv de Pokemon restantes:'] = pv_pk
    return registro_turno


# Estadisticas #


entrenador_1 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Historial de turnos:': None
                }

entrenador_2 = {'Nombre: ': None,
                'Pokemon Elegido': None,
                'Historial de turnos:': None,
                }


