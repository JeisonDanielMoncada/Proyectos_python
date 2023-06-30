a = 2
b = 2.3
n = str(a)
c = str(b)
h = (a + b )
f= int(h)
print("La suma de", n , "+" , c , "es igual a" , h , "pero si lo aproximamos es", f)
"""
Los tipos de datos enteros para Python 3 no presentan limite de tamaño
Los datos flotantes tienen un limite de tamaño de 53 bits
"""
p=0
n=0
print ("ingresa un numero entero")
n = int(input())
while n >= 0:
    if  n % 2 == 0:
        p = p + n
        n -= 1
    else:
        n -= 1
print("La suma de los pares del numero ingreso es ", p)
