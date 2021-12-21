###Definir funcion

def triangulo(a,m,b,x):
    u = 0
    if(x>a and x<=m):
        u = (x - a)/(m - a)
    elif(x>m and x<=b):
        u = (b - x) / (b - m)
    else:
        u = 0
    return u

VV = float(input("Ingresar velocidad del viento: "))
####Medición del viento
MP = triangulo(0,0,3,VV)
P  = triangulo(0,3,6,VV)
M  = triangulo(3,6,9,VV)
G  = triangulo(6,9,12,VV)
MG = triangulo(9,12,12,VV)

##Definir la posición de los singleton para la salida
NM  = 0
MPP = 8.75
MM = 17.5
MUG = 26.25
MGG = 35

##Fusificacion
Denominador = MP + P + M + G + MG
if(Denominador == 0):
    pr = 0
else:
    pr = (P*MPP + M*MM + G*MUG + MG*MGG)/Denominador
print('MP = {} P = {} M = {} G = {} MG = {} Posición de Referencia {}'.format(MP,P,M,G,MG,pr))
