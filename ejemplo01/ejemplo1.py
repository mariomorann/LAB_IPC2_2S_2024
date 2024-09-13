# hola mundo
# variables
# aritmetica
# logicos
# casteos
# typeof
# input
# condicionales
# listas
# ciclos
# metodos
# funciones


print("hola mundo")

var1 = 5 # int
variable2 = 2.5  # float
variable3 = "string" # string
var4 = True # bool

suma = var1 + variable2
resta = var1 - variable2
multiplicacion = var1 * variable2
division = var1 / variable2

#print(suma)
#print(resta)
#print(multiplicacion)
#print(division)

op_1 = var1 == 1
op_2 = var1 != 2
op_3 = var1 < 2
op_4 = var1 <= 2
op_5 = var1 > 2
op_6 = var1 >= 2

op1 = True and True
op2 = True or False
op3 = not op1

print(op_1)
print(op_2)
print(op_3)
print(op_4)
print(op_5)
print(op_6)
print("")
print(op1)
print(op2)
print(op3)

numero = "10"

suma = int(numero) + 1

print("Resultado: " + str(suma))
print(f"Resultado: {suma}")
print("Resultado:", suma)

print("")
#edad = int(input("Escriba su edad: "))
edad = 18

if edad >= 18:
    print("Es mayor de edad")
elif edad >= 14:
    print("Es adolscente")
else:
    print("Es un niño")

print("")
match edad:
    case 22:
        print("la edad es 22")

    case 21:
        print("la edad es 21")
    case _:
        print(f"la edad es {edad}")

print("")

lista = []
lista.append("Mario")
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)

#print(lista)
#print(lista.pop())
#print(lista)
#print(lista.remove(2))
#print(len(lista))

for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("")

print("")
for item in lista:
    print(item, end=", ")

print("")
for c in "string":
    print(c)

print("")
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

def holamundo(nombre):
    print("Hola,", nombre)

holamundo("Mario")

def suma(num1, num2):
    return num1 + num2

print(suma(9, 6))

try:
    print("numero " + 1)
except Exception:
    print("Hubo un error")