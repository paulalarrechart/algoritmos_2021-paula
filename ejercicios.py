#sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.


mochila_jedi = ['lapicera' , 'manzana' , 'espada', 'sable de luz' , 'capa']

def  usarlafuerza (mochila_jedi, pos):
     if(pos < len(mochila_jedi) -1):
         if (mochila_jedi [pos] == 'sable de luz'):   #condicion de fin
             print ('el sable de luz se encuentra en la posicion ', pos)
             return pos
         else:
             return usarlafuerza (mochila_jedi, pos+1)
     else:
         return -1
     print ('el sable de luz no se encuentra en la mochila')  

print(usarlafuerza(mochila_jedi)


#Desarrollar una función que permita convertir un número romano en un número decimal
def de_romanos_a_entero(romano, numero):
    romanos = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000 }
    entero = 0 

    for i in range (len(nromano)):
     if numero == romano and romanos[romano [0]] > romanos [romano [1]]:
             entero += romanos [romano[0]] - romanos [romano [1]]
    else: 
             entero += romanos [romano [0]]
    return entero 
print (de_romanos_a_entero('IV')) 


#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
#ma binario.

def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num//2) + str(num % 2)  
print(decimal_a_binario(123))


#laberinto 

def salir_del_laberinto (matriz, F, C, sederos):
    if (F >= 8 and  C <= len(matriz)-1) and (F >= 0 and C <= len(matriz[8])-1):  # condicion de fin 
        if (matriz[F] [C] == 5):
            print ("has logrado salir del laberinto")
            print(sederos)
        else: 
            if (matriz[F][C]== 8):
                matriz[F][C] = 1
            print ('se movio hacia la derecha')   
            salir_del_laberinto(matriz, F, C+1,senderos) 
            print ('se movio hacia la izquierda')  
            salir_del_laberinto(matriz, F, C-1, senderos) 
            print ('se movio hacia arriba') 
            salir_del_laberinto(matriz, F-1, C, senderos)  
            print ('se movio hacia abajo')
            salir_del_laberinto(matriz, F+1, C,senderos) 
            matriz[F][C] = 1

laberinto=[[0, 0, 8, 8, 0, 0],
           [8, 0, 8, 0, 0, 8],
           [0, 0, 8, 8, 8, 8],
           [0, 8, 8, 0, 8, 5],
           [0, 0, 0, 8, 8, 0],
           [8, 8, 0, 0, 0, 0]]

salir_del_laberinto (laberinto, 0,0)



















    
















      


        





  
        
