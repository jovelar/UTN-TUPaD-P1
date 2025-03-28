
#Actividad 1
def a1():
    print("hola mundo!")

#Actividad 2
def a2():
    nombre=input("ingrese su nombre: ")
    print(f"hola {nombre}")

#Actividad 3
def a3():
    nombre = input("Ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese s lugar de residencia: ")
    print(f"Hola soy {apellido} {nombre} tengo {edad} anios y vivo en {residencia}")

#Actividad 4
def a4():
    radio = input("Ingrese el radio del circulo: ")
    print(f"El area de un circulo con radio {radio} es de {3.14*(float(radio)**2)} y su perimetro es de {2*3.14*float(radio)}")

#Actividad 5
def a5():
    tiempo = input("Ingrese el tiempo en segundos: ")
    print(f"El tiempo ingresado equivale a {round(float(tiempo)/3600,2)} horas ")

#Actividad 6
def a6(): 
    numero = input("Ingrese un numero: ")
    for i in range(1,11,1):
        print(f"{numero} x {i} = {i*int(numero)} ")

#Actividad 7
def a7(): 
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(f"{numero1} + {numero2} = {numero1+numero2}")
    print(f"{numero1} - {numero2} = {numero1-numero2}")
    print(f"{numero1} * {numero2} = {numero1*numero2}")
    print(f"{numero1} / {numero2} = {numero1/numero2}")

#Actividad 8
def a8():
    altura=int(input("Ingrese su altura en centimetros: "))
    peso=float(input("Ingres su peso en kilos: "))
    print(f"Su IMC es de {round(peso/((altura/100)**2),2)}")

#Actividad 9
def a9():
    tempCelcius=float(input("Ingrese la temperatura en celsius: "))
    print(f"La temperatura ingresada ({tempCelcius}) en celsius equivale a {round((9/5*tempCelcius)+32,2)} grados Fahrenheit")

#Actividad 10
def a10():
    num1 = input("Ingrese el primer numero: ")
    num2 = input("Ingrese el segundo numero: ")
    num3 = input("Ingrese el tercer numero: ")
    print(f"El promedio es de {round((int(num1)+int(num2)+int(num3))/3,2)}")

a1()
a2()
a3()
a4()
a5()
a6()
a7()
a8()
a9()
a10()