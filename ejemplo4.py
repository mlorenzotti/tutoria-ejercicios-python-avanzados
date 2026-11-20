def contar_letras(palabra):
    palabra=palabra.replace(" ", "").lower()
    conteo={}
    for letra in palabra: 
        conteo[letra] = conteo.get(letra, 0) + 1
        return conteo

def son_anagramas(palabra1, palabra2):
    return contar_letras(palabra1)==contar_letras(palabra2)
palabra1=input("Ingrese palabra ")
palabra2=input("Ingrese palabra ")

if son_anagramas(palabra1, palabra2):
    print("Son anagramas")
else: 
    print("No son anagramas")
