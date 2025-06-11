import sys
def ejercicio1(numero):
    sys.setrecursionlimit(100000) #Por las dudas si se ingresa un numero muy grande

    def factorial(numero):
        if numero <= 1:
            return 1
        else:
            return numero * factorial(numero-1)
        
    print(factorial(numero))

def ejercicio2(numero):
    def fibonacci(numero):
        
    pass


