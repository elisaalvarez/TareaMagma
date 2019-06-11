#THE BOWLING GAME
#Elisa Alvarez
import random
puntaje1=[] #Para almacenar los puntajes del primer tiro
puntaje2=[] #Para almacenar los puntajes del segundo tiro
puntajeT=[] #Para almacenar el puntaje total del turno
puntajeA=[] #Para almacenar el puntaje acumulado
def haceJugada (x):
    tiro1=random.randrange(0,11,1) #Crea el primer tiro
    tiro2=random.randrange(0,11-tiro1,1) #Crea el segundo tiro
    #Almacenar los tiros
    puntaje1.append(tiro1)
    puntaje2.append(tiro2)
    #Acumular el puntaje del turno
    puntajeT.append(tiro1+tiro2)
#Comprueba si hubo strike en la jugada anterior
def hayStrike (p):
    if puntaje1[p-1]==10:
        puntajeT[p-1]+=(puntaje1[p]+puntaje2[p])
        return True
#comprueba si hubo spare en la jugada anterior
def haySpare (p):
    if ((puntaje1[p-1]+puntaje2[p-1])==10)and (puntaje1[p-1]<10):
        puntajeT[p-1]+=puntaje1[p]
        return True
#Crea los puntajes finales
def final ():
    for a in range (len(puntajeT)):
        if a>0:
            puntajeA.append(puntajeT[a]+puntajeA[a-1])
        else:
            puntajeA.append(puntajeT[a])
for x in range (10): #Hacer 10 jugadas de la línea
    haceJugada(x)
    if x>0:
        hayStrike(x)
        haySpare(x)
haceJugada(x) #Hacer la jugada extra
if hayStrike(10): #Verifica si en la última jugada hubo strike
    print("Strike en la última jugada")
    puntajeT.pop()
elif haySpare(10): #Verifica si en la última jugada hubo spare
    print("Spare en la última jugada")
    puntaje2.pop() #Quita el segundo tiro extra
    puntajeT.pop() 
else: #Si no hubo spare o strike se deshecha la jugada extra
    puntaje1.pop()
    puntaje2.pop()
    puntajeT.pop()
final()
print(puntaje1)
print(puntaje2)
print(puntajeA)
print("El puntaje final es: "+str(puntajeA[9]))

