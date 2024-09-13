from xml.dom import minidom

def main():
    xml = minidom.parse("archivo.xml")
    pizzas = xml.getElementsByTagName("pizza")

    for pizza in pizzas:
        print(pizza.getAttribute("nombre"), pizza.getAttribute("precio"))
        ingredientes = pizza.getElementsByTagName("ingrediente")

        for ingrediente in ingredientes:
            print(" - ", ingrediente.firstChild.data)
        print("")

if __name__ == "__main__":
    main()