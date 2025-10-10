from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    return len(cadena) == 5 and cadena.isalpha()



def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
 
    tiempo_total_partida = (fin-inicio).total_seconds()
    minutos = tiempo_total_partida // 60
    segundos = tiempo_total_partida % 60

    lista_minutos_segundos = (minutos, segundos)
    return lista_minutos_segundos

    

def quitar_letras(cadena: str, caracter: str) -> str:
    res = ""
    encontrado = False
    # Para cada caracter "c" de cadena:
        # Si "c" es distinto de "caracter" o "encontrado"
            # Añadirlo a res
    for c in cadena:
        if c == caracter and not encontrado:
          pass #---
        else:
            res += 1    
    return res          



def marcar_verdes(palabra_secreta: str, intento: str) -> str:
    verdes = ""
    restantes = palabra_secreta

    for v in range(len(palabra_secreta(0,4))):
        if palabra_secreta[v] == intento:
            verdes += "V"
            restantes = quitar_letras(palabra_secreta, v)
        else:
            verdes += "_" 
    return verdes, restantes


def marcar_amarillas(intento: str, verdes: str, restantes: str) -> str:
    colores = ""
    for v in range(len(verdes)):
        if verdes[v] == intento:
            colores += "V"
        else:
            if intento[v] in restantes:
                cadena += "A"
                restantes = quitar_letras(restantes, v)
            else:
                cadena += "_"
    return colores





def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    


