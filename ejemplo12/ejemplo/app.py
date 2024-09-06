from flask import Flask, request
from app_blueprint import app_bp

app = Flask(__name__)
app.register_blueprint(app_bp)

@app.route("/get", methods=["GET"])
def peticion_get():
    print("Hola mundo")
    return "<h2>Hola mundo</h2>"

@app.route("/post", methods=["POST"])
def peticion_post():
    nombre = request.json['nombre']
    print(nombre)
    return f"<h2>El nombre es: <strong> { nombre } </strong> </h2>"

@app.route("/get/<id>", methods=["GET"])
def preticion_get2(id):
    print(id)
    return f"<p>El ID es <strong> {id}</strong></p>"

if __name__ == "__main__":
    app.run(debug=True)