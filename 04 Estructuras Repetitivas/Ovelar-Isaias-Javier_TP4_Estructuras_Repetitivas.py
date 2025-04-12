import random

#Actividad 1
def actividad1():
    for i in range(0,101):
        print(i)

#actividad 2
def actividad2():
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

    #Validaciones
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
    