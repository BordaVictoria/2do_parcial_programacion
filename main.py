import os
import time
from Package.funciones import *
from Package.juego import *
import json
import pygame as pg

pg.init()

colores = {
    "blanco": (255, 255, 255),
    "negro": (0, 0, 0),
    "verde": (0, 225, 0),
    "rojo": (225,0,0),
    "amarillo": (229, 255, 0),
    "marron": (151, 95, 57),
    "gris": (189, 192, 201)
}


def main():
    tupla = ("descubrir continente","descubrir letra", "descubrir comida")
    usos_comodines = [0] *len(tupla)
    palabras = obtener_lista_palabras("words.csv")
    palabras_normalizadas = normalizar_en_diccionario(palabras)
    lista_puntuacion = []
    palabras_adivinadas = 0
    tiempo_rondas = []
    intentos_partidas_perdidas = 0
    intentos = 6
    
    #region Bucle principal del juego
    
    while palabras_adivinadas < 3 or intentos_partidas_perdidas < 3:
        puntuacion = 0
        dificultad = pedir_dificultad("Que dificultad quiere jugar ? 5 / 6 / 7 : ","Porfavor ingrese 5, 6 o 7")
        palabra_generada = obtener_palabra(palabras_normalizadas,dificultad)
        matriz = generar_matriz(palabra_generada,intentos)
        print(palabra_generada)
        #region Bucle de rondas
        tiempo_inicio = time.time()
        
        puntuacion_modificada = jugar(palabra_generada, tupla, usos_comodines, matriz, intentos)
        

        tiempo_final = time.time()
        tiempo_rondas.append(tiempo_final - tiempo_inicio)
        lista_puntuacion.append(puntuacion_modificada)
        #endregion
    
        print(puntuacion_modificada)
        validar_estado(puntuacion_modificada, intentos_partidas_perdidas, palabras_adivinadas)
        mostrar_matriz(matriz)
        os.system("pause")
        os.system("cls")
    #endregion

    guardar_puntuacion(nombre_ingresado,tiempo_rondas,palabras_adivinadas,puntaje_total,tiempo_total)
    os.system("pause")


main()