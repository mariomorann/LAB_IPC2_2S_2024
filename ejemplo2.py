


def suma(num1, num2):
    return num1 + num2


def main():
    opcion = "0"
    while opcion != "3":
        print(" ================= MENU =================")
        print(" 1. ver hola mundo")
        print(" 2. sumar")
        print(" 3. salir")
        print(" =========================================")
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                print("hola mundo")
            case "2":
                try:
                    num1 = int(input("Escribe el primer numero: "))
                    num2 = int(input("Escribe el segundo numero: "))
                    resultado = suma(num1, num2)
                    print("Resultado: ", resultado)
                except Exception:
                    print("Debe ingresar numeros")
            case "3":
                print("adios mundo")
                break
            case _:
                print("Opción inválida")
        
    



if __name__ == "__main__":
    main()