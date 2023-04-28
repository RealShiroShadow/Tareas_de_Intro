
def contarPalabras(pBuscar, pBusqueda):
    conteo = [0 for i in range(len(pBuscar))]
    for indice, palabra in enumerate(pBuscar):
        for busqueda in pBusqueda:
            conteo[indice] += busqueda.split(" ").count(palabra)
    return pBuscar, conteo

def validarTuplaStrings(pTupla):
    if isinstance(pTupla, tuple):
        for i in pTupla:
            if not isinstance(i, str):
                return False
    else:
        return False
    return True

def ESContarPalabras(pBuscar, pBusqueda):
    if validarTuplaStrings(pBuscar) and validarTuplaStrings(pBusqueda):
        palabras, cuenta = contarPalabras(pBuscar, pBusqueda)
        for palabra, cantidad in zip(palabras, cuenta):
            print(f"{palabra}: {cantidad}")
    else:
        print("Se aceptan listas de strings únicamente")

ESContarPalabras(( "calor", "ayer", "el", "mañana"), ("ayer hizo bastante calor", "en el laboratorio hace calor"))

def diferenciaSimetrica(pConjuntos):
    resultado = ""
    for i in str(pConjuntos[0]):
        if i not in str(pConjuntos[1]) and i not in resultado:
            resultado += i
    for i in str(pConjuntos[1]):
        if i not in str(pConjuntos[0]) and i not in resultado:
            resultado += i
    #resultado += "".join([i for i in str(pConjuntos[1]) if i not in str(pConjuntos[0]) and i not in resultado])
    return int(resultado)

print(diferenciaSimetrica((1234,3455)))
