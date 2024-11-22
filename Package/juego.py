import random
from Package.funciones import *
import os

def jugar(palabra_generada, tupla, usos_comodines, matriz, intentos):
    intentos_actuales = 0
    validacion = False
    while intentos_actuales < intentos and not validacion:
        mostrar_matriz(matriz)
        palabra_ingresada = pedir_palabra("Ingrese una palabra: ", "Ingrese la cantidad de carateres correspondientes",palabra_generada,tupla, usos_comodines)
        
        validacion = verificar_palabra(palabra_ingresada, palabra_generada, matriz,intentos_actuales)
        intentos_actuales += 1
        os.system("cls")
    salida = modificar_puntuacion(validacion, palabra_generada, intentos_actuales)
    return salida

def obtener_palabra(lista_palabras,dificultad):
    while True:
        palabra_obtenida = random.choice(lista_palabras)
        if palabra_obtenida["caracteres"] == dificultad:
            return palabra_obtenida
        
def generar_matriz(palabra_obtenida: dict,intentos):
        matriz = []
        for i in range(intentos):
            matriz_temporal = ["_"] * palabra_obtenida["caracteres"]
            matriz.append(matriz_temporal)
        return matriz

def verificar_palabra(palabra_ingresada: str, palabra_obtenida: dict, matriz: list,intentos):
    validacion = False
    if palabra_obtenida["pais"] == palabra_ingresada:
        validacion = True
        
    for i in range(len(palabra_obtenida["pais"])):
        if palabra_ingresada[i] == palabra_obtenida["pais"][i]:
            matriz[intentos][i] = "\033[32m" + palabra_ingresada[i] + "\033[0m"
        elif palabra_ingresada[i] in palabra_obtenida["pais"]:
            matriz[intentos][i] = "\033[33m" + palabra_ingresada[i] + "\033[0m"
        else:
            matriz[intentos][i] = "\033[31m" + palabra_ingresada[i] + "\033[0m"
        
    
    if validacion:
        return validacion

def modificar_puntuacion(validacion: bool, palabra: dict, intentos_actuales: int):
    puntuacion = 0
    if validacion:
        
        intentos = intentos_actuales - 1
        match palabra["caracteres"]:
            case 5:
                puntuacion += 50
                if intentos > 1:
                    puntuacion -= 10 * intentos
                    
            case 6:
                puntuacion += 80       
                if intentos > 1:
                    puntuacion -= 15 * intentos
            case 7:
                puntuacion += 100
                if intentos > 1:
                    puntuacion -= 20 * intentos
    return puntuacion
                    
def puntuar_por_tiempo(tiempo_total: int, contador_victorias: int, puntuacion: int):
    if tiempo_total / 60 <= 15 and contador_victorias == 5:
        puntuacion += 100
        print("Ganaste 100 puntos por ser un capo y ganar en menos de 15 minutos")
    return puntuacion