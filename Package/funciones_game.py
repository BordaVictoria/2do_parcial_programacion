import pygame as pg

def crear_boton(ventana: pg.Surface, posicion, dimension, texto, fuente, color, color_fondo, bandera=True) -> dict:
    boton = {}
    boton["pantalla"] = ventana
    boton["posicion"] = posicion
    boton["dimension"] = dimension
    boton["Presionado"] = False

    fuente_texto = pg.font.SysFont(fuente[0], fuente[1])
    boton["superficie"] = pg.Surface(dimension)
    boton["superficie"].fill(color_fondo)
    texto_renderizado = fuente_texto.render(texto, True, color)
    texto_rect = texto_renderizado.get_rect(center=(dimension[0] // 2, dimension[1] // 2))
    boton["superficie"].blit(texto_renderizado, texto_rect)

    boton["rectangulo"] = pg.Rect(posicion, dimension)
    if bandera:
        boton["rectangulo"].topleft = boton["posicion"]

    return boton

def dibujar_boton(boton: dict):
    boton["pantalla"].blit(boton["superficie"], boton["rectangulo"])

def mostrar_matriz(ventana: pg.Surface, matriz, fuente, color, color_fondo):
    boton_ancho, boton_alto = 50, 50
    x, y = 200, 100
    for fila in matriz:
        for elemento in fila:
            boton = crear_boton(ventana, (x, y), (boton_ancho, boton_alto), str(elemento), fuente, color, color_fondo, False)
            dibujar_boton(boton)
            x += 50  # Increment x by the button width plus margin to avoid overlap
        x = 200  # Reset x to initial position after each row
        y += 50  # Increment y by the button height plus margin to avoid overlap
