from listas.Lista import Lista
from clases.Pizza import Pizza
from xml.dom import minidom

def main():
    lista_pizzas = Lista()

    xml = minidom.parse("archivo.xml")
    pizzas = xml.getElementsByTagName("pizza")

    for pizza in pizzas:
        nuevaPizza = Pizza(pizza.getAttribute("nombre"), pizza.getAttribute("precio"))

        ingredientes = pizza.getElementsByTagName("ingrediente")

        for ingrediente in ingredientes:
            nuevaPizza.lista_ingredientes.append(ingrediente.firstChild.data)

        lista_pizzas.insertar(nuevaPizza)
    
    lista_pizzas.getInfo()
    
    lista_pizzas.eliminar("Barbacoa")

    lista_pizzas.getInfo()


if __name__ == "__main__":
    main()