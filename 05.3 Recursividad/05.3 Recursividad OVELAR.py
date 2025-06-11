#Las funciones estan definidas dentro de otras funciones, para que sea mas ordenado y no
#queden funciones solucion en cada punto por un lado y funciones con nombre del ejercicio
#por otro

def ejercicio1(numero):
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            print(n)
            factorial(n-1)

    
    factorial(numero)


def ejercicio2(numero):
    
    def fibonacci(n):
        if n-2>=0:
            print(fibonacci(n-1)+fibonacci(n-2))
            fibonacci(n)
        pass
    
    fibonacci(numero)


def ejercicio3(numero,exp):
    
    #resuelto con un ternario
    def potenciaRec(n,m):
        return 1 if m==0 else n * potenciaRec(n,m-1)
    
    print(potenciaRec(numero,exp))

def ejercicio4(numero_argumento):
    #resuelto con un ternario
    def cadenaRecursiva(numero):
        return "0" if numero==0 else cadenaRecursiva(numero//2) + str(numero%2)
        
    print(cadenaRecursiva(numero_argumento))

def ejercicio5(palabra_argumento):
    posicion1=0
    posicion2=len(palabra_argumento)-1
    def es_palindromo(palabra, pos1, pos2):
        if pos1 >= pos2:
            return True
        if palabra[pos1] != palabra[pos2]:
            return False
        return es_palindromo(palabra, pos1 + 1, pos2 - 1)
    print(es_palindromo(palabra_argumento,posicion1,posicion2))
    
def ejercicio6(numero_parametro):
    def suma_digitos(numero):
        return numero if numero < 10 else (numero%10) + suma_digitos(numero//10)
    
    print(f"{suma_digitos(numero_parametro)}")


def ejercicio7(parametro):
    
    def calcula_piramide(niveles):
        return 1 if niveles ==1 else niveles + calcula_piramide(niveles-1)
    
    print(calcula_piramide(parametro))

ejercicio7(4)
    
                
            
    
        
        
