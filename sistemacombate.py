import pokedex
import random
import sistemalogs

# IMPORTANTE: CREAR AL MENOS 2 POKEMON ANTES DE COLOCAR
# OPCION 3 EN MENU DEL MAIN, PARA QUE ESTE SISTEMA PUEDA FUNCIONAR.

def tirar_moneda():
    lados = ['C', 'S']
    lado_ganador = random.random(lados)
    if lado_ganador == 'C':
        return 1 # Cara
    return 0 # Sello

def iniciar_jugadores():

    global entrenador_1
    global pokemon_ent1
    global entrenador_2
    global pokemon_ent2
    # Necesarios para no limitar uso en esta funcion y poder usarse en otras.
    # Generalmente es mala práctica usar global en POO, pero en este caso será necesario.

    entrenador_1= input("Entrenador 1 - Ingresa tu nombre: ")
    id_pkm_ent1 = input(f"{entrenador_1}, ingresa la ID del Pokemon que usarás: ")
    entrenador_2 = input("Entrenador 2 - Ingresa tu nombre: ")
    id_pkm_ent2 = input(f"{entrenador_2}, ingresa la ID del Pokemon que usarás: ")

    print(f"""BATALLA POKEMON : ENTRENADOR/A {entrenador_1} V / S ENTRENADOR/A {entrenador_2}
            {entrenador_1} ha elegido a {pokedex.pokedex[id_pkm_ent1.get_nombre]}!
            {entrenador_2} ha elegido a {pokedex.pokedex[id_pkm_ent2.get_nombre]}!""")

def turnos_cara():
    pass

def turnos_sello():
    pass

def verificar_ganador():
    pass

def BATALLA_POKEMON():
    pass








