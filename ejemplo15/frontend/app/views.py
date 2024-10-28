from django.shortcuts import render
import requests
import xmltodict
import re

import plotly.graph_objs as go
import plotly.offline as pyo

contenido_archivo = ""

# Create your views here.
def index(request):
    global contenido_archivo

    if request.FILES:
        archivo = request.FILES['archivo']
        contenido_archivo = archivo.read().decode("utf-8")
        if contenido_archivo != "":
            json_archivo = xmltodict.parse(contenido_archivo)
            response = requests.post("http://localhost:8001/cargarArchivo", json=json_archivo)
            res = response.json()
            print(res["message"])
    
    context={"contenido": contenido_archivo}
    return render(request, "index.html",context=context)

def ver(request):
    if contenido_archivo:
        response = requests.get("http://localhost:8001/obtenerArchivo")
        #res = response.json()
        res = response.text

        

        return render(request, "ver.html", context={"contenido": res})
    
    return render(request, "ver.html", context={"contenido": ""})

def grafica(request):

    categorias = ['A', 'B', 'C', 'D', 'E', 'F']
    suma_total = [15, 27, 31, 7, 20, 18]

    data = go.Bar(y=suma_total, x=categorias)
    
    layout = go.Layout(
        title="Sumatoria de votos por Categoría",
        xaxis={"title": "Categoría"},
        yaxis={"title": "Suma de votos"}
    )

    fig = go.Figure(data=[data], layout=layout)
    plot_div = pyo.plot(fig, include_plotlyjs=False, output_type='div')

    return render(request, "grafica.html", context={"plot_div": plot_div})