# Pruebas para las funciones de wordle_utils.py

from wordle_utils import es_palabra_valida

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

test_es_palabra_valida()
print("✅Todas las pruebas pasaron correctamente.")






from wordle_utils import es_palabra_valida
from datetime import datetime
def test_calcula_minutos_y_segundos():
    print("Probando calcula_minutos_y_segundos...")
    assert calcula_minutos_y_segundos(
                datetime(2024,1,1,23,0,0),
                datetime(2024,1,1,23,0,30)) == (0,30)
    assert calcula_minutos_y_segundos(
                datetime(2024,1,1,23,0,0),
                datetime(2024,1,1,23,3,45)) == (3,45)
    assert calcula_minutos_y_segundos(
                datetime(2024,1,1,23,0,0),
                datetime(2024,1,2,0,1,15)) == (61,15)
    
test_calcula_minutos_y_segundos
print("Todas las pruebas pasaron correctamente")



from wordle_utils import quitar_letras
def test_quitar_letras():
    print("Probando quitar_letras")
    assert quitar_letras("casar", "c") == "asar"
    assert quitar_letras("casar", "r") == "casa"
    assert quitar_letras("casar", "z") == "casar"
    assert quitar_letras("aaaaa", "a") == "aaaa" 

test_quitar_letras()
print("Todas las pruebas pasaron correctamente")

from wordle_utils import marcar_verdes
def test_marcar_verdes():
    print("Probando marcar_verdes...")
    assert marcar_verdes("casar", "polio") == ("_____", "casar")
    assert marcar_verdes("casar", "casar") == ("VVVVV", "")
    assert marcar_verdes("casar", "cazar") == ("VV_VV", "s")
    assert marcar_verdes("casar", "secta") == ("_____", "casar")
    assert marcar_verdes("casar", "sacar") == ("_V_VV","cs")
    assert marcar_verdes("casar", "peras") == ("___V_", "csar")

test_marcar_verdes()
print("Todas las pruebas pasaron correctamente")


from wordle_utils import marcar_amarillas
def test_marcar_amarillas():
    print("Probando marcar_amarillos...")
    assert marcar_amarillos("polio", "_____", "casar") == "_____"
    assert marcar_amarillos("casar", "VVVVV", "") == "VVVVV"
    assert marcar_amarillos("cazar", "VV_VV", "s") == "VV_VV"
    assert marcar_amarillos("secta", "_____", "casar") == "A_A_A"
    assert marcar_amarillos("sacar", "_V_VV", "cs") == "AVAVV"
    assert marcar_amarillos("peras", "___V_", "csar") == "__AVA"

test_marcar_amarillas
print("Todas las pruebas pasaron correctamente")
