from classes.Usuario import Usuario
from flask import Flask, Blueprint, render_template, redirect, request
from flask_cors import CORS

blueprints = Blueprint("app", __name__, template_folder="templates")
app = Flask(__name__)
cors = CORS(app)

# variables

lista_registros = []

# ----------------------- RENDERS -------------------------

@blueprints.route("/")
def inicio():
    return render_template("index.html")

@blueprints.route("/formulario")
def formulario():
    return render_template("formulario.html")

@blueprints.route("/registros")
def registros():
    return render_template("registros.html", lista_registros=lista_registros)

# ----------------------- FUNCIONES -----------------------

@app.route("/enviar", methods=["POST"])
def enviar():
    name = request.form["name"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form["password"]

    lista_registros.append(Usuario(name, lastname, email, password))

    return redirect("/formulario")

@app.route("/eliminar/<nombre>", methods=["GET"])
def eliminar(nombre):
    for usuario in lista_registros:
        if usuario.name == nombre:
            lista_registros.remove(usuario)
    return redirect("/registros")


@app.route("/delete/<nombre>", methods=["DELETE"])
def eliminar_endpoint(nombre):
    for usuario in lista_registros:
        if usuario.name == nombre:
            lista_registros.remove(usuario)
            return "Se eliminó exitosamente"
    return "No se encontró el usuario"

@app.route("/edit", methods=["PUT"])
def editar_endpoint():
    nombre = request.json["name"]
    for usuario in lista_registros:
        if usuario.name == nombre:
            usuario.lastname = request.json["lastname"]
            usuario.email = request.json["email"]
            usuario.password = request.json["password"]
        
            return "Se editó exitosamente"
    return "No se encontró el usuario"


app.register_blueprint(blueprints)
if __name__ == "__main__":
    app.run(debug=True)