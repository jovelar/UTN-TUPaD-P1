from collections import deque #Necesario para el punto 7

#Actividad 1

def actividad1():
    precios_frutas={'Banana':1200,'Anana':2500,'Melon':3000,'Uva':1450}

    #agregando 3 nuevas frutas con sus valores
    precios_frutas['Naranja']=1200
    precios_frutas['Manzana']=1500
    precios_frutas['Pera']=2300

    print(precios_frutas)

#Actividad 2
def actividad2():
    precios_frutas={'Banana':1200,'Anana':2500,'Melon':3000,'Uva':1450,'Naranja':1200,'Manzana':1500,'Pera':2300}

    #Actualizando precios
    precios_frutas['Banana']=1330
    precios_frutas['Manzana']=1700
    precios_frutas['Melon']=2800

    print(precios_frutas)

#Actividad 3
def actividad3():
    precios_frutas={'Banana':1200,'Anana':2500,'Melon':3000,'Uva':1450,'Naranja':1200,'Manzana':1500,'Pera':2300}
    listaFrutas=[]
    for key in precios_frutas:
        listaFrutas.append(key)

    print(listaFrutas)

#Actividad 4

class Persona:
    def __init__(self,nombre,pais,edad):
        self.nombre=nombre
        self.pais=pais
        self.edad=edad
    
    def saludar(self):
        print(f"!Hola, soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")

def actividad4():
    pepe=Persona('Lucio','Jupiter',34)
    pepe.saludar()


#Actividad 5
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    
    def calcular_area(self):
        print(f"Area:{(self.radio**self.radio)*3.14}")
    
    def calcular_perimetro(self):
        print(f"Perimetro: {(2*3.14)*self.radio}")



def actividad5():
    circulo=Circulo(4)
    circulo.calcular_area()
    circulo.calcular_perimetro()
    

#Actividad 6
def actividad6():
    dic={'(':')','{':'}','[':']'}
    string="({[]})"
    indexA=0
    indexB=len(string)-1 #Se resta 1 por que los indices inician en 0
    balanceado=True #Se asume inicialmente que el string se encuentra balanceado, al primer error se vuelve false (short-circuit)
  

    #Compara usando 2 indices, indexA comienza por el principio mientras que indexB por el final
    #Busca la primer letra indicada por indexA y la busca en el diccionario, luego compara el valor de la key
    #contra la letra indicada por indexB, ambos indices no deben superarse el uno al otro
    while indexA<=indexB and balanceado==True:
        letra=string[indexA]

        #Se usa try catch por si la key no se encontrara
        try:
            if dic[letra]!=string[indexB]:
                balanceado=False
            indexA+=1;
            indexB-=1;
        except KeyError:
            balanceado=False
    return balanceado


#Actividad 7
class Cliente:

    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni}"

class Cola:
    
    def __init__(self):
        self.elementos=deque()
    
    def encolar(self,elemento):
        self.elementos.append(elemento)
    
    def desencolar(self):
        elemento=None
        if len(self.elementos)!=0:
            elemento=self.elementos.popleft()
        return elemento
    
    def primero(self):
        primero=None
        if len(self.elementos)!=0:
            primero=self.elementos[0]
        return primero
    
    def colaVacia(self):
        estado=False
        if len(self.elementos)==0:
            estado=True
        
        return estado
    
    #Metodos para facilitar las opearaciones
    def agregarClientes(self,cliente):
        self.encolar(cliente)

    def atenderClientes(self):
        if self.colaVacia() is False:
            print(f"Atendiendo cliente {self.primero()} ")
            self.desencolar()
        pass

def actividad7():
    banco=Cola()
    banco.agregarClientes(Cliente('Julio','Gimenez',30303032))
    banco.agregarClientes(Cliente('Pepe','Mujica',1234567))
    banco.agregarClientes(Cliente('Jorge','Larrata',121212121))
    banco.agregarClientes(Cliente('Miauricio','Macri',4444444))

    banco.atenderClientes()
    banco.atenderClientes()
    banco.atenderClientes()
    banco.atenderClientes()
    banco.atenderClientes()

#Actividad 8
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.lista=None

    def insertarAlPrincipio(self,dato):
        nuevo=Nodo(dato)
        nuevo.siguiente=self.lista
        self.lista=nuevo
    
    def insertarAlFinal(self,dato):
        nuevo=Nodo(dato)
        if self.lista==None:
            self.lista=nuevo
        else:
            iterador=self.lista
            while iterador.siguiente is not None:
                iterador=iterador.siguiente
            iterador.siguiente=nuevo

    def mostrar(self):
        if self.lista is not None:
            iterador=self.lista
            while iterador:
                print(iterador.dato)
                iterador=iterador.siguiente
        else:
            print("Lista Vacia!")

def Actividad8():
    listaSemana=ListaEnlazada()
    listaSemana.insertarAlPrincipio('Lunes')
    listaSemana.insertarAlPrincipio('Martes')
    listaSemana.insertarAlPrincipio('Miercoles')
    listaSemana.insertarAlPrincipio('Jueves')
    listaSemana.insertarAlPrincipio('Viernes')

    listaSemana.mostrar()


#Actividad 9

def invertirLista(lista):
    listaInvertida=ListaEnlazada()
    iterador=lista.lista

    while iterador:
        listaInvertida.insertarAlPrincipio(iterador.dato)
        iterador=iterador.siguiente
    return listaInvertida

def Actividad9():
    listaSemana=ListaEnlazada()
    listaSemana.insertarAlPrincipio('Lunes')
    listaSemana.insertarAlPrincipio('Martes')
    listaSemana.insertarAlPrincipio('Miercoles')
    listaSemana.insertarAlPrincipio('Jueves')
    listaSemana.insertarAlPrincipio('Viernes')

    listaInvertida=invertirLista(listaSemana)

    listaInvertida.mostrar()

actividad1()
actividad2()
actividad3()
actividad4()
actividad5()
actividad6()
actividad7()
Actividad8()
Actividad9()