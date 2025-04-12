import random

#Actividad 1
def actividad1():
    for i in range(0,101):
        print(i)

#actividad 2
def actividad2():

    #Validacion que fuerza a ingesar un dato valido para continuar
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero valido")
            continue
        else:
            break
    print(f"El numero contienec {len(str(numero))} letras. ")

#actividad3()
def actividad3():

    #Validacion que fuerza a ingesar un dato valido para continuar
    while True:
        try:
            numero1=int(input("Ingrese el primer numero: "))
            numero2=int(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Ingrese un numero valido")
            continue
        else:
            break

    if numero1 == numero2:
        print("Los numeros son iguales")
    else:
        if numero1 < numero2:
            for i in range(numero1 + 1,numero2):
                print(i)
        else:
            for i in range(numero2 + 1,numero1):
                print(i)

#Actividad 4
def actividad4():
    numero=1
    sumatoria=0
    while numero!=0:
        #Validacion que fuerza a ingesar un dato valido para continuar
        while True:
            try:
                numero=int(input("Ingrese un numero: "))
            except ValueError:
                print("Valor invalido ")
                continue
            else:
                break
        sumatoria+=numero
    print(sumatoria)

#Actividad 5
def actividad5():
    intentos=0
    numIntento=4 #Valor aleatorio para poder ingresar al while, el mismo se va a sobreeescribir
    numero=random.randint(1,10)
    while numIntento!=numero:
        #Validacion que fuerza a ingesar un dato valido para continuar
        while True:
            try:
                numIntento=int(input("Ingrese un numero del 1 al 10: "))
            except ValueError:
                print("No es un numero ")
                continue
            else:
                break
        intentos+=1
        if numIntento==numero:
            print(f"Ud acerto con {intentos} intentos!")

#Actividad 6
def actividad6():
    for i in range(100,0,-2):
        print(i)

#Actividad 7
def actividad7():
    numero=0
    #Validacion que fuerza a ingesar un dato valido para continuar
    while True:
        try:
            numero=int(input("Ingrese un numero entero positivo: "))
        except ValueError:
            print("Valor ingresado invalido")
        else:
            break

    sumatoria=0
    for i in range(0,numero):
        sumatoria+=i
    
    print(f"La suma de todos los nuneros del 0 al {numero} es de  {sumatoria}")


#Actividad 8
def actividad8():
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0 
    numero = 0

    for i in range(0,100):
        while True:
            try:
                numero=int(input("Ingrese un numero: "))
            except ValueError:
                print("Valor invalido, solo numeros ")
            else:
                break
        if numero>=0:
            positivos+=1
        else:
            negativos+=1
        if numero%2==0:
            pares+=1
        else:
            impares+=1
    print(f"Se ingresaron numeros: {positivos} positivos, {negativos} negativos, {pares} pares, {impares} impares")

#Actividad 9
def actividad9():
    sumatoria=0
    elementos=0
    numero=0
    for i in range(0,100):
        while True:
            try:
                numero=int(input("Ingrese un numero: "))
            except ValueError:
                print("Valor invalido, solo numeros ")
            else:
                break
        sumatoria+=numero
        elementos+=1
    
    print(f"El promedio de los {elementos} numeros ingresados es de {sumatoria/elementos}")

#Actividad 10
def actividad10():
    numero=0
    while True:
        try:
            numero=int(input("Ingrese un numero a invertir "))
        except ValueError:
            print("El valor ingresado no es un numero")
        else:
            break
    
    #Reutilizamos la variable, es mas facil trabajar como un arreglo de chars para cambiar el orden
    numero=str(numero)
    invertido=""

    #len(numero)-1 para evitar que se pase del rango dado que los arreglos inician en 0 y no en 1
    #-1, en el limite inferior para permitir acceder al primer elemento del arreglo (numero[0])
    #-1 como ultimo parametro para indicar que se recorrera el arreglo desde el final hacia el principio
    for i in range(len(numero)-1,-1,-1):
        invertido+=numero[i]
    print(f"Numero invertido es {invertido}")

actividad1()
actividad2()
actividad3()
actividad4()
actividad5()
actividad6()
actividad7()
actividad8()
actividad9()
actividad10()
    