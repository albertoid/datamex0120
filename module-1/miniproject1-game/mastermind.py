import random


codigo =[]
tirada =[]
solucion=[]
columna =[]

for i in range(4): codigo.append(0)
for i in range(4): tirada.append(0)
for i in range(4): solucion.append(False)
for i in range(4): columna.append(False)
running = True
dificultad = 'Facil'
nivel = 6
inicio = False

#flujo del juego
#print(codigo)
print('*****Mastermind*****')
print('Descifre una combinación de 4 números')

#cliclo principal
while running == True:

    while inicio == False:#La variable inicio arranca al juego, por la posibilida de solicitar las reglas
        print('Escriba la dificultad de las siguiente opciones: Facil - Medio - Dificil.\nEscriba "Reglas" para conocer las reglas del juego')
        dificultad = input()
    
        if dificultad == 'Dificil' or dificultad == 'dificil':
            nivel = 10 
            inicio = True
        elif dificultad == 'Medio' or dificultad == 'medio':
            nivel = 7
            inicio = True
        elif dificultad == 'Reglas':
            print("Mastermind es un juego de habilidad y lógica que consiste en descubrir una secuencia de números oculta.")
            print('Este juego normalmente esta diseñado para jugarse con esferas de colores, pero para fines prácticos')
            print('sustituimos las esferas por numeros.')
            print('En cada secuencia ingresara se regresaran dos pistas: La primera es la cantidad de números en la secuencia')
            print('colocados de forma correcta dentro de la secuenca. La segunda es la cantidad de números colocados  en la')
            print('secuencia que existen dentro de ella pero que están en un lugar incorrecto.')
            print('Se cuenta con 10 oportunidades para descubrir la secuencia y en caso de encontrarla el juego te decreta')
            print('ganador\n')    
        else:
            dificultad = 'facil'
            nivel = 5
            inicio = True
    
    print('Ha seleccionado dificultad {}, la clave a descifrar tienen numeros del 0 al {}. Los números pueden repetirse'.format(dificultad, nivel))
    
    #Generacion de la clave
    for i in range(4): codigo[i] = random.randrange(nivel)
    
    for i in range(10):
    
        inputok = False #Inicializacion de la comprobacion de entrada
    
        while inputok == False:
            print('Intento número',i+1,'de 10')
            temp = input()
            if str.isnumeric(temp) and int(temp) < 10000 and int(temp) >= 0:#Comprobacion de la entrada numerica y dentro del rango
                inputok = True
            elif temp == 'trampa':
                print(codigo)
            else:
                print('La entrada debe ser una combinacion de 4 numeros, intente otra vez')
    
    
        #Generacion de la cadena de 4 numeros en numeros conmenos de 4 digitos que son validos
        temp_str=str(temp)
    
        for i in range(4-len(temp_str)):
            temp_str='0'+temp_str
    
        #Generacion de lista de 4 digitos
        for i in range(4):
            tirada[i]=int(temp_str[i])
        
        #Entrada valida - comparaciones
        
        # Pistas de valor y lugar correcto
        numok_lugok = 0
    
        for i in range(4):
            if codigo[i] == tirada[i]: 
                numok_lugok =numok_lugok + 1
                solucion[i] = True
            else:
                    solucion[i] = False
         
        # Pista de valores corretos en lugar incorrecto
        numok_lugnok=0
        for i in range(4): columna[i]=False 
    
        for x in range(4):
            for y in range (4):
                #print(codigo[x], ' - ' ,tirada[y])
                if x!=y and solucion[x] == False and columna[y] == False:
                    if codigo[x] == tirada[y]:
                        numok_lugnok = numok_lugnok +1
                        solucion[x] = True
                        columna[y] = True
                        #print('Aqui')
                        #print('-')
        print(numok_lugok, 'bien ubicado', numok_lugnok, 'mal ubicados')
    
        if numok_lugok == 4: 
            print('------\nGanaste! el código era: ', codigo)
            break
    
    if numok_lugok < 4:
        print('------\nPerdiste :( la combinación era:', codigo )
            
    print('Para jugar otra vez escribe "si"; para terminar solo da enter o escribe cualquier cosa')
    continuar = input()
        
    if continuar == 'Si' or continuar == 'si':
        running = True
    else:
        print('Gracias por jugar Mastermind para Python')
        running = False
        break
    