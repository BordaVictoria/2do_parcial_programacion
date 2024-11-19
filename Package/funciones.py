import random
import re
import json
#region diccionario / listas
def obtener_lista_palabras(path: str = "palabras.csv") -> list:
    """
    Obtiene una lista de palabras de un archivo csv.

    Args:
        path (str, optional): Path hacia el archivo csv. Defaults to "palabras.csv".

    Returns:
        list: Lista de palabras.
    """    
    lista = []

    with open(path, "r", encoding="utf-8") as archivo:
        archivo.readline().split(",")
        for linea in archivo:
            
            lectura = re.split(",|\n", linea)
            for i in range(len(lectura)):
                lectura[i] = lectura[i].lower()
            lista.append(lectura)
    return lista

def normalizar_en_diccionario(palabras: list) -> dict:
    """
    Normaliza una lista de palabras en un diccionario.

    Args:
        palabras (list): Lista de palabras.

    Returns:
        dict: Diccionario de palabras.
    """    
    diccionario = []

    for palabra in palabras:
        diccionario_temporal = {}
        diccionario_temporal["pais"] = palabra[0]
        diccionario_temporal["continente"] = palabra[2]
        diccionario_temporal["caracteres"] = int(palabra[1])
        diccionario_temporal["comida"] = palabra[3]
        diccionario.append(diccionario_temporal)
    
    return diccionario

#endregion

#region funciones palabras
def verificar_si_existe_la_palabra(palabra: str, palabras: list):
    validacion = False
    for palabra_diccionario in palabras:
        if palabra_diccionario["palabra"] == palabra:
            validacion = True
    if validacion == False:
        print("NO EXISTE LA PALABRA GORREADO")
    return validacion

def mostrar_pista (pista: str, palabra: dict, tupla_pistas: tuple, intentos_comodines: list):
    if pista == tupla_pistas[0]:
        print(palabra["continente"])
    elif pista == tupla_pistas[1]:
        letra_random = random.choice(palabra["pais"])
        indice = palabra["pais"].index(letra_random)
        print(letra_random, " en la posicion ", indice + 1)
    elif pista == tupla_pistas[2]:
        print(palabra["comida"])
    intentos_comodines[tupla_pistas.index(pista)] = 1

def pedir_palabra (mensaje, mensaje_error, palabra, pistas_tupla: tuple, intentos_comodines: list):
    while True :
        palabra_ingresada = input(mensaje).lower()
        if palabra_ingresada in pistas_tupla:
            if intentos_comodines[pistas_tupla.index(palabra_ingresada)] == 0:
                mostrar_pista(palabra_ingresada, palabra, pistas_tupla, intentos_comodines)
            else:
                print("Ya usaste esa pista")
        elif len(palabra["pais"]) == len(palabra_ingresada) and palabra_ingresada.isalpha():
            return palabra_ingresada
        else:
            print(mensaje_error)
    
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def puntuar_por_tiempo(tiempo_total: int, contador_victorias: int, puntuacion: int):
    if tiempo_total / 60 <= 15 and contador_victorias == 5:
        puntuacion += 100
        print("Ganaste 100 puntos por ser un capo y ganar en menos de 15 minutos")
    return puntuacion

def sumar_lista(lista: list):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
#endregion

def pedir_dificultad (mensaje,mensaje_error):
    while True:
        dificultad = input(mensaje)
        try :
            dificultad = int(dificultad)
            if dificultad > 7 or dificultad < 5:
                print(mensaje_error)
            else:
                return dificultad
        except:
            print(mensaje_error)    
            
            
# def guardar_puntuacion (nombre, tiempo_rondas,palabras_adivinadas,puntaje_total,tiempo_total):
    
#     dato = {}
#     dato ["Partida"] = [{"jugador": nombre, "partidas_jugadas": len(tiempo_rondas), "victorias": palabras_adivinadas, "tiempo_promedio": tiempo_total / len(tiempo_rondas), "puntaje_total": puntaje_total }]
#     with open ("puntuaciones.json","a") as archivo :
        
#         json.dump(dato,archivo,indent=4)
#         archivo.write(",")
        
# import json   
def guardar_puntuacion(nombre: str, tiempo_rondas: list, contador_victorias: int, puntuacion: int, tiempo_total: int):
    tiempo_total = sumar_lista(tiempo_rondas)
    puntaje_total = sumar_lista(lista_puntuacion)
    puntaje_total = puntuar_por_tiempo(tiempo_total, palabras_adivinadas, puntaje_total)
    nombre_ingresado = input("Ingrese su nombre: ")
    try:
        with open("puntuaciones.json", "r", encoding="utf-8") as archivo:
            puntuaciones = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        puntuaciones = []

    puntuaciones.append({"nombre": nombre, "partidas_jugadas": len(tiempo_rondas), "contador_victorias": contador_victorias, "puntuacion": puntuacion, "tiempo_promeedio": tiempo_total / len(tiempo_rondas)})

    with open("puntuaciones.json", "w", encoding="utf-8") as archivo:
        json.dump(puntuaciones, archivo, indent=4, ensure_ascii=False)
            

def validar_estado(puntuacion, intentos_partidas_perdidas, palabras_adivinadas):
    if puntuacion > 0:
        print("GANASTE PIPIIII")
        palabras_adivinadas += 1
    else:
        print("PERDISTE CORNETA")
        intentos_partidas_perdidas += 1



    