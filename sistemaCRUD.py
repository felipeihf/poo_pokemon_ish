from fabricapokemon import *
from pokedex import pokedex, pokedex_espejo
import json
import os


def crear_pokemon():

    nombre = input("Ingresa el nombre: ")
    pv = int(input("Ingrese puntos de vida: "))
    pa = int(input("Ingrese puntos de ataque: "))
    tipo = input("Ingrese tipo de Pokemon (Agua/Fuego/Hierba): ").lower()
    id = input("Ingrese un id disponible en Pokedex para registrarlo:")
    for key in pokedex:
        if pokedex[key] == '':
            if tipo == 'hierba':
                pokedex[id] = TipoHierba(nombre, id, pv, pa, tipo, 'fuego', 'agua')
                pokedex_espejo[id] = pokedex[id].nombre
            elif tipo == 'fuego':
                pokedex[id] = TipoFuego(nombre, id, pv, pa, tipo, 'agua', 'hierba')
                pokedex_espejo[id] = pokedex[id].nombre
            elif tipo == 'agua':
                pokedex[id] = TipoFuego(nombre, id, pv, pa, tipo, 'hierba', 'fuego')
                pokedex_espejo[id] = pokedex[id].nombre
            else:
                print("Error: Tipo de Pokemon no válido. ")
        else:
            print("Error: La ID solicitada se encuentra ocupada.")

def leer_pokemon():
    print(json.dumps(pokedex_espejo, indent=1))
    os.system('cls')
    elige_pkm = input("Ingresa el id del Pokemon que quieras revisar: ")
    print(json.dumps(pokedex[elige_pkm].__dict__, indent=1))


def actualizar_pokemon():
    os.system('cls')
    id_pokemon = input("Ingrese id del Pokemon que quiere modificar: ")
    if id_pokemon in pokedex:
        opcion_actualizar = int(input("""Ingrese opción a modificar
                                    (1) Nombre
                                    (2) Puntos Ataque
                                    (3) Puntos de Vida"""))

        if opcion_actualizar == 1:
            nuevo_name = input("Ingrese el nuevo nombre: ")
            pokedex[id_pokemon].set_nombre(nuevo_name)
            pokedex_espejo[id_pokemon] = nuevo_name
            os.system('cls')
            print(json.dumps(pokedex[id_pokemon].__dict__, indent=1))
            print("Actualizado con exito")

        elif opcion_actualizar == 2:
            nuevo_pa = int(input("Ingrese los nuevos PA: "))
            pokedex[id_pokemon].set_puntosataque(nuevo_pa)
            os.system('cls')
            print(json.dumps(pokedex[id_pokemon].__dict__, indent=1))
            print("Actualizado con exito")

        elif opcion_actualizar == 3:
            nuevo_pv = int(input("Ingrese los nuevos PV: "))
            pokedex[id_pokemon].set_puntosvida(nuevo_pv)
            os.system('cls')
            print(json.dumps(pokedex[id_pokemon].__dict__, indent=1))
            print("Actualizado con exito")
    else:
        print("El Pokemon no está registrado en la Pokedex. ")

def borrar_pokemon():

    id = int(input("Ingrese el ID del Pokemon a borrar: "))
    if id in pokedex:
        pokedex[id] = ''
        os.system('cls')
        print(json.dumps(pokedex_espejo, indent=1))
        print("Pokemon borrado exitosamente.")
    else:
        print("Error: Pokemon a borrar no existe en la memoria.")


