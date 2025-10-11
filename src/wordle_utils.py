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
          encontrado = True
        else:
            res += c    
    return res          



def marcar_verdes(palabra_secreta: str, intento: str) -> str:
    """
    Compara el intento con la palabra secreta para encontrar las letras correctas
    en la posición correcta (verdes).

    Devuelve:
        - Una cadena string con "V" para las letras verdes y "_" para el resto.
        - Una cadena string con las letras de la palabra secreta que no fueron verdes.
    """

    verdes = ""
    restantes = ""

    for v in range(len(palabra_secreta)):
        if palabra_secreta[v] == intento[v]:
            verdes += "V"
        else:
            verdes += "_" 
            restantes += palabra_secreta[v]

    return verdes, restantes


def marcar_amarillas(intento: str, verdes: str, restantes: str) -> str:
    """
    Usa el resultado de los verdes para marcar las letras que están en la
    palabra pero en la posición incorrecta (amarillas).
    """

    colores = ""

    for v in range(len(verdes)):
        if verdes[v] == "V":
            colores += "V"
        else:
            if intento[v] in restantes:
                colores += "A"
                restantes = quitar_letras(restantes, v)
            else:
                colores += "_"
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

    # 1: Identificar las letras verdes y obtener las letras restantes.
    verdes, restantes = marcar_verdes(palabra_secreta, intento)

    # 2: Usar el resultado anterior para marcar las amarillas.
    pistas_completas = marcar_amarillas(intento, verdes, restantes)

    return pistas_completas
    


