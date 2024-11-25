import os
import time
from Package.funciones import *
from Package.juego import *
import pygame as pg
from Package.funciones_pygame import *

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

def main_juego():
    pg.init()
    reloj = pg.time.Clock()
    tamaño_ventana = (700, 400)
    ventana = pg.display.set_mode(tamaño_ventana)
    pg.display.set_caption("Palabrini")
    fuente = ("Arial", 20)
    fuente_matriz = ("Arial", 40)
    dificultad = [5,6,7]
    intentos = 6
    palabras = obtener_lista_palabras("words.csv")
    palabras_normalizadas = normalizar_en_diccionario(palabras)
    palabra_generada = obtener_palabra(palabras_normalizadas,dificultad[0])
    matriz = generar_matriz(palabra_generada,intentos)
    bandera_juego = True
    boton_modos = []
    posicion_botones_x = 100
    posicion_botones_y = 0
    palabra_obtenida = ""
    for i in range(3):
        boton = crear_boton(ventana, (posicion_botones_x, posicion_botones_y), (200, 100), f"{5+i} caracteres", fuente, colores["negro"], colores["blanco"])
        boton_modos.append(boton)
        posicion_botones_x += 150
    while bandera_juego:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                bandera_juego = False
            if evento.type == pg.MOUSEBUTTONDOWN:
                if boton_modos[i]["rectangulo"].collidepoint(evento.pos):
                    matriz_pantalla = boton_modos[i]["texto"]
                    palabra_generada = obtener_palabra(palabras_normalizadas,matriz_pantalla)
                    matriz = generar_matriz(palabra_generada,intentos)
                    mostrar_matriz_p(ventana,matriz,fuente,"blue","grey")
        
        for i in range(3):
            dibujar_boton(boton_modos[i])
        
        ventana.fill(colores["blanco"])
        
            
        
        
                
        reloj.tick(20)
        pg.display.update()
    
    
    
    pg.quit()
    
    
main_juego()