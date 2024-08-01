import random

def gera_numeros():
    numeros_gerados = []

    resultado = random.randint(0,99)
    numeros_gerados.append(resultado)

    termo_1_soma = random.randint(0,resultado)
    numeros_gerados.append(termo_1_soma)

    termo_2_soma = resultado - termo_1_soma
    numeros_gerados.append(termo_2_soma)

    termo_qualquer = random.randint(0,99)
    while termo_qualquer in numeros_gerados:
        termo_qualquer = random.randint(0,99)
    numeros_gerados.append(termo_qualquer)

    return numeros_gerados
