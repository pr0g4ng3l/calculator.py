def calculadora(numero1: int,signo: str,numero2: int):
    if signo == "+":
        resultado = numero1 + numero2
        
    elif signo == "-":
        resultado = numero1 - numero2
        
    elif signo == "/":
        resultado = numero1 / numero2
        
    elif signo == "*":
        resultado = numero1 * numero2
              
    else:
        print("Ha ocurrido un error")
        
    return resultado

numero1: int = int(input("Introduce el primer digito: "))
signo: str = input("Introduce la operacion, + para suma, - para resta, / para division, * para multiplicacion: ")
numero2: int = int(input("Introduce el segundo digito: ")) 

resultado = calculadora(numero1, signo, numero2)
print(resultado)

while 1 > 0:
    signo2: str = input("Introduce la siguiente operacion: ")
    nuevo_numero: int = int(input("Introduce el siguiente numero: "))
    
    resultado_final = calculadora(resultado, signo2, nuevo_numero)
    print(resultado_final)
    
    resultado = resultado_final