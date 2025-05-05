import os

def actividad1():
    lista=list(range(1,100))

    print(lista)

def actividad2():
    marcas=['Audi','Mercedez','Fiat','Dodge','Ford','Chevolet']
    print(marcas[-2])

def actividad3():
    lista=[]
    lista.append('Dolar')
    lista.append('Yen')
    lista.append('Yuan')

def actividad4():
    animales=["perro","gato","conejo","pez"]
    animales[1]="loro"
    animales[-1]="oso"
    print(animales)

#Actividad 5
#Elimina el numero mas grande del arreglo numeros

def actividad6():
    lista=list(range(10,31,5))
    for i in range(0,2):
        print(lista[i])

def actividad7():
    autos=["sedan","polo","suran","gol"]
    autos[1]="pato"
    autos[2]="paloma"

def actividad8():
    lista=[]
    lista.append(5*2)
    lista.append(10*2)
    lista.append(15*2)
    print(lista)

def actividad9():
    compras=[["pan","Leche"],["arroz","fideos","salsa"],["agua"]]

    #A
    compras[2].append("Jugo")
    #B
    index=compras[1].index("fideos")
    compras[1][index]="Tallarines"
    #C
    compras[0].remove("pan")
    #D
    print("Compras luego de modificar")
    print(compras)

def actividad10():
    lista_anidada=[15,True,[25.5,57.9,30.6],False]
    print(lista_anidada)



#Mostrando los ejercicios

#Actividad 1
actividad1()
pausa=input("Presione [Enter] para continuar")

#Limpieza de pantalla
os.system("cls")

#Actividad 2
actividad2()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 3
actividad3()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 4
actividad4()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 6
actividad6()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 7
actividad7()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad8
actividad8()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 9
actividad9()
pausa=input("Presione [Enter] para continuar")
os.system("cls")

#Actividad 10
actividad10()
pausa=input("Presione [Enter] para continuar")
os.system("cls")