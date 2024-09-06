from flask import Blueprint, render_template

app_bp = Blueprint("ejemplo", __name__, template_folder="templates")

@app_bp.route("/")
def inicio():
    return render_template("incio.html")


@app_bp.route("/fin")
def fin():
    return render_template("fin.html")

@app_bp.route("/tabla/<segundos>")
def tabla(segundos):
    context = {"segundos": segundos}
    return render_template("tabla.html", context=context)
