#Actividad 1
def imprimir_hola_mundo():
    print("Hola mundo!")

def actividad1():
    imprimir_hola_mundo()

#Actividad 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def actividad2():
    saludar_usuario(input("Ingrese su nombre: "))

#Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

def actividad3():
    nombre = input("Ingrese su nombre ")
    apellido = input("Ingrese su apellido ")
    edad = input("Ingrese su edad ")
    residencia = input("Ingrese su residencia ")
    informacion_personal(nombre,apellido,edad,residencia)

#Actividad  4
def calcular_area_circulo(radio):
    return 3.14 * (radio^2)

def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

def actividad4():
    radio=int(input("Ingrese el radio: "))
    print(f"El area es de {calcular_area_circulo(radio)} y el perimetro es de {calcular_perimetro_circulo(radio)}")

#Actividad 5
def segundos_a_horas(segundos):
    return segundos/3600

def actividad5():
    segundos=int(input("Ingrese los segundos: "))
    print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#Actividad 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero*i}")

def actividad6():
    numero=int(input("Ingrese un numero para la tabla del 1 al 10 "))
    tabla_multiplicar(numero)

#Actividad 7
def operaciones_basicas(a,b):
    return (a+b,a-b,a*b,a/b)

def actividad7():
    numeroA=int(input("Ingrese el numero A: "))
    numeroB=int(input("Ingrese el numero B: "))
    tupla=operaciones_basicas(numeroA,numeroB)
    print(f"Suma {numeroA} + {numeroB} = {tupla[0]}")
    print(f"Resta {numeroA} - {numeroB} = {tupla[1]}")
    print(f"Multiplicacion {numeroA} * {numeroB} = {tupla[2]}")
    print(f"Division {numeroA} / {numeroB} = {tupla[3]}")

#Actividad 8
def calcular_imc(peso,altura):
    return peso/(altura**altura)

def actividad8():
    peso=float(input("Ingree el peso en kg: "))
    altura=float(input("Ingrese la altura en metros: "))
    print(f"el IMC es de {calcular_imc(peso,altura)}")

#Actividad 9
def celcius_a_fahrenheit(celsius):
    return (celsius * (9/5))+32

def actividad9():
    celcius=float(input("Ingrese la temperatura en celcius: "))
    print(f" La temperatura en celcius equivale a {celcius_a_fahrenheit(celcius)} fahrenheit")

#Actividad 10
def calcular_promedio(a,b,c):
    return(a+b+c)/3

def actividad10():
    numero1=int(input("Ingrese el primer numero: "))
    numero2=int(input("Ingrese el segundo numero: "))
    numero3=int(input("Ingrese el tercer numero: "))
    print(f"El promedio es de {calcular_promedio(numero1,numero2,numero3)}")


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
