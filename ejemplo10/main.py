from estructuras.ListaDoble import ListaDoblementeEnlazada
from estructuras.ListaCircular import ListaCircular

def main():
    
    lista_doble = ListaDoblementeEnlazada()
    lista_doble.agregar_al_final("Mario")
    lista_doble.agregar_al_final("Pablo")
    lista_doble.agregar_al_final("María")
    lista_doble.agregar_al_inicio("Diego")
    lista_doble.agregar_al_inicio("Cristian")

    lista_doble.imprimir()
    print("")
    # -----------------------------------------------

    lista_circular = ListaCircular()
    lista_circular.insertar(1)
    lista_circular.insertar(3)
    lista_circular.insertar(4)
    lista_circular.insertar(2)
    lista_circular.insertar("hola mundo")

    lista_circular.imprimir()

    lista_circular.graficar()


if __name__ == "__main__":
    main()