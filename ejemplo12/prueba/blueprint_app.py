from flask import Blueprint, render_template, redirect

app_bp = Blueprint("prueba", __name__, template_folder="")

@app_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app_bp.route("/holamundo")
def hola_mundo():
    return render_template("hola.html")

@app_bp.route("/adiosmundo")
def adioss_mundo():
    return render_template("adios.html")

@app_bp.route("/tabla/<segundos>")
def tabla(segundos):
    context = {"segundos": segundos}
    return render_template("tabla.html", context=context)