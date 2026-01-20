def promedio(lista):
    suma = 0
    for x in lista:
        suma = suma + x
    return suma / len(lista)


def contar_mayores_o_iguales(valores, umbral):
    c = 0
    for v in valores:
        if v >= umbral:
            c = c + 1
    return c


def clasificar_nota(nota):
    if nota >= 6.0:
        return "Excelente"
    elif nota >= 5.0:
        return "Bueno"
    elif nota >= 4.0:
        return "Suficiente"
    else:
        return "Insuficiente"


def estado_curso(prom, aprobados, total):
    if prom < 4.0:
        return "Riesgo"
    elif (prom >= 5.0) and (aprobados == total):
        return "Sólido"
    else:
        return "Ok"
