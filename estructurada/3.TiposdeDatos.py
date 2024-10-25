if __name__ == '__main__':
    #Tipos de dstos básicos
    entro = 42                          #int
    decimal = 3.14                      #float
    complejo = 2 + 3j                   #complex
    booleano = True
    cadena = "Hola, Python!"
    binario = bytes([50, 100, 150])     #bytes

    print("Tipos básicos:")
    print("Entero:", entro)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Booleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario, "\n")

    #Estructuras de datos avanzadas
    lista = [1, 2, 3, "Cuatro"]
    tupla = (5, 6, 7, "ocho")
    conjunto = {9, 10, "once", "doce"}
    diccionario = {"clave1": "valor1", "clave2": 20}

    print("Estructuras avanzadas:")
    print("Lista:", lista)
    print("Tupla:", tupla)
    print("Conjunto:",conjunto )
    print("Diccionario:", diccionario)

    #Otros tipos de especiales
    nulo = None             # NoneType
    rango = range(3)        # range (equivale a [0]

    print("Tipos especiales:")
    print("Nulo:", nulo)
    print("Rango:",list(rango)) #Convertimos a lista

    #Ejemplo de iteracion con el tipo de range
    print("\nIterando sobre el rango: ")
    for numero in rango:
        print(numero)




