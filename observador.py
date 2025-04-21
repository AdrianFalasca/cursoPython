def contar_vocales(palabra):
    vocales = "aeiou"
    
    for x in vocales:
        contador = 0
        for i in palabra:
            if x == i.lower():
                contador += 1
        print("Hay", contador, x)

input("ingresa un nombre:")        
contar_vocales("a")

input()