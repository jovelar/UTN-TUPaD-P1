def ejercicio1():
    def factorial(n):
        if n == 0:
            return 1
        else:
            print(n)
            factorial(n-1)

    
    factorial(40)


def ejercicio2():
    def fibonacci(n):
        if n-2>=0:
            print(fibonacci(n-1)+fibonacci(n-2))
            fibonacci(n)
        pass
    
    fibonacci(50)

ejercicio2()
