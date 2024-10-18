from flask import Flask, request, jsonify
import dicttoxml

app = Flask(__name__)

archivo_cargado = None

@app.route("/cargarArchivo", methods=["POST"])
def cargar_archivo():
    global archivo_cargado
    
    archivo_cargado = request.json

    # convertir el diccionario a un xml
    xml = dicttoxml.dicttoxml(archivo_cargado)

    return jsonify({"message": "La carga se realizó con exito."})

@app.route("/obtenerArchivo", methods=["GET"])
def obtener_archivo():
    return jsonify(archivo_cargado)

if __name__ == "__main__":
    app.run(debug=True, port=8001)
