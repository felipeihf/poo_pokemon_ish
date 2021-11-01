import pokedex
import random
import sistemalogs

# IMPORTANTE: CREAR AL MENOS 2 POKEMON ANTES DE COLOCAR
# OPCION 3 EN MENU DEL MAIN, PARA QUE ESTE SISTEMA PUEDA FUNCIONAR.

global turno_actual
global entrenador_1
global entrenador_2
#Necesarios para no limitar uso en esta funcion y poder usarse en otras.
#Generalmente es mala práctica usar global en POO, pero en este caso será necesario
#Con el fin de hacer las fases del combate mas fluidas y no generar una declaracion tan larga.

def tirar_moneda():
    lados = ['C', 'S']
    lado_ganador = random.random(lados)
    if lado_ganador == 'C':
        return 1 # Cara
    return 0 # Sello

def iniciar_jugadores():
    global pkm1
    global pkm2
    global pkm1_pv
    global pkm2_pv
    global entrenador_1
    global entrenador_2

    entrenador_1 = input("Entrenador 1 - Ingresa tu nombre: ")
    id_pkm_ent1 = input(f"{entrenador_1}, ingresa la ID del Pokemon que usarás: ")
    entrenador_2 = input("Entrenador 2 - Ingresa tu nombre: ")
    id_pkm_ent2 = input(f"{entrenador_2}, ingresa la ID del Pokemon que usarás: ")

    pkm1 = pokedex.pokedex[id_pkm_ent1]
    pkm1_pv = pokedex.pokedex[id_pkm_ent1].get_puntosvida
    pkm2 = pokedex.pokedex[id_pkm_ent2]
    pkm2_pv = pokedex.pokedex[id_pkm_ent2].get_puntosvida

    print(f"""BATALLA POKEMON : ENTRENADOR/A {entrenador_1} V / S ENTRENADOR/A {entrenador_2}
            {entrenador_1} ha elegido a {pokedex.pokedex[id_pkm_ent1.get_nombre]}!
            {entrenador_2} ha elegido a {pokedex.pokedex[id_pkm_ent2.get_nombre]}!""")

def determinar_ventaja():
# que retorne quien tiene la ventaja de los 2 pokemon
    pass


def turnos_cara():
    turno_jugador1()
    #Agregar turno a registro de turnos, sumar+1 contador turnos
    verificar_ganador(pkm1_pv, pkm2_pv)
    turno_jugador2()
    #Agregar turno a registro de turnos, sumar+1 contador turnos
    verificar_ganador(pkm1_pv, pkm2_pv)
    #Volver a turno jugador1

    pass

def turnos_sello():
    turno_jugador2()
    #Agregar turno a registro de turnos, sumar +1 contador turnos
    verificar_ganador(pkm1_pv, pkm2_pv)
    turno_jugador1()
    #Agregar turno a registro de turnos, sumar+1 contador turnos
    verificar_ganador(pkm1_pv, pkm2_pv)
    #Volver a turno jugador1

def turno_jugador1():
    comando_ply1 = int(input(f"""{entrenador_1} :
                                    ¿Qué debería hacer {pkm1.get_nombre}
                                    (1) Ataque Normal
                                    (2) Ataque Especial
                                    (3) Retirarse"""))
    pass


def turno_jugador2():
    comando_ply1 = int(input(f"""{entrenador_2} :
                                    ¿Qué debería hacer {pkm2.get_nombre}
                                    (1) Ataque Normal
                                    (2) Ataque Especial
                                    (3) Retirarse"""))
    pass

def verificar_ganador(pkm1_pv, pkm2_pv):
    if pkm1_pv <= 0:
        #Añade logs de turnos para consultar
        print(f"""{pkm2.get_nombre} ha caido!\n
        {entrenador_1} Es el ganador!""")

    elif pkm2_pv <= 0:
        print(f"""{pkm1.get_nombre} ha caido!\n
        {entrenador_2} Es el ganador!""")

    else:
        print("Empate(?)")

turno_actual = 0

def BATALLA_POKEMON():

    while pkm1_pv != 0 or pkm2_pv != 0:
        iniciar_jugadores()
        #Hacer elegir Cara o Sello
        tirar_moneda()
        #Si sale cara:
        determinar_ventaja()
        turnos_cara()
        #Si sale sello
        determinar_ventaja()
        turnos_sello()

    pass








