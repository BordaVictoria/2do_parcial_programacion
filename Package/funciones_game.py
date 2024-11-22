import pygame as pg

def crear_boton(ventana, posicion, dimension, texto, fuente, color, color_fondo):
    boton = {}
    boton["pantalla"]= ventana
    boton["posicion"]= posicion
    boton["dimension"]= dimension
    boton["Presionado"] = False
    
    fuente_texto = pg.font.SysFont(fuente[0], fuente[1])
    boton["superficie"]= fuente_texto.render(texto, False, color, color_fondo)
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].topleft = boton["posicion"]
    
    return boton
    
def dibujar_boton(boton):
    boton["pantalla"].blit(boton["superficie"], boton["rectangulo"])
    
def mostrar_matriz(ventana, matriz, fuente, color, color_fondo):
    x, y = 50, 50
    for fila in matriz:
        for elemento in fila:
            boton = crear_boton(ventana, (x, y), (100, 100), str(elemento), fuente, color, color_fondo)
            dibujar_boton(boton)
            x += 50  # Increment x to avoid overlap
        x = 50  # Reset x to initial position after each row
        y += 50  # Increment y to avoid overlap