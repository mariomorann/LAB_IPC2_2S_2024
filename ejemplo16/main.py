import re


cadena = "Pablo Moran Mario, Jose, Mario"

prueba_findall = re.findall(r"[a-zA-Z]+", cadena)
print(prueba_findall)

prueba_search = re.search(r"[a-zA-Z]", cadena)
print(prueba_search.start())

prueba_split = re.split(", ", cadena)
print(prueba_split)

prueba_sub = re.sub("Mario", "Hola", cadena)
print(prueba_sub)