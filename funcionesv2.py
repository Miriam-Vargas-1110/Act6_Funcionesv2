print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_cd(c,d):
    r=c-d
    return r

def multi_ef(e,f):
    m=e*f
    return m

def divi_gh(g,h):
    d=g/h
    return d

#llamada a funciones
print("Calculando suma")
n1=int(input("Ingresa el primer Numero para sumar "))
n2=int(input("Ingresa el segundo Numero para sumar "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
print("\n")

print("Calculando resta")
n3=int(input("Ingresa el primer Numero para restar "))
n4=int(input("Ingresa el segundo Numero para restar "))
resta=resta_cd(n3,n4)
print(f"la resta de {n3} - {n4} es {resta}")
print("\n")

print("Calculando multiplicacion")
n5=int(input("Ingresa el primer Numero para multiplicar "))
n6=int(input("Ingresa el segundo Numero para multiplicar "))
multip=multi_ef(n5,n6)
print(f"la multiplicacion de {n5} * {n6} es {multip}")
print("\n")

print("Calculando divicion")
n7=int(input("Ingresa el primer Numero para dividir "))
n8=int(input("Ingresa el segundo Numero para dividir "))
divi=divi_gh(n7,n8)
print(f"la divicion de {n7} / {n8} es {divi}")
