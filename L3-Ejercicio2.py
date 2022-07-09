valido = False 

while not valido :
    Peso = input("Introduzca su peso en Kg:")
    if   Peso.isnumeric() : valido =True
    else : print('Peso no válido')

valido = False
while not valido :
    Estatura = input("Introduzca su estatura en metros:")
    try: 
        float(Estatura) 
        valido = True
    except:
            valido = False
            print('Estatura no válida')

ic = str(round( int(Peso) / (float(Estatura) **2),2))

print('Su indice de masa corporal es: ' + ic) 
