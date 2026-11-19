def busqueda_binaria(lista, objetivo):
    bajo=0
    alto=len(lista)-1
    medio=(bajo+alto)//2
    intentos=0
    while bajo<=alto:
        intentos=intentos+1
        if lista[medio]==objetivo:
            print("Número encontrado en posición ", medio)
            return intentos
        if objetivo<lista[medio]:
            alto=medio-1
        elif objetivo>lista[medio]:
            bajo=medio+1
        medio=(bajo+alto)//2
    print("Número no encontrado")

lista= [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
objetivo=int(input("Selecciona un número "))
busqueda_binaria(lista, objetivo)